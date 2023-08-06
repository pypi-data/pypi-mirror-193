from collections import defaultdict
from dataclasses import dataclass, field
from types import ClassMethodDescriptorType, FunctionType, GetSetDescriptorType, MappingProxyType, MemberDescriptorType, \
    MethodDescriptorType, MethodType, MethodWrapperType, WrapperDescriptorType
from typing import Any, Dict, Mapping, Optional, Protocol, Sequence, Set

from .base import AbstractModel
from .relationship import Relationship


@dataclass
class FieldsCache:
    priv: Set[str] = field(default_factory=set)
    pub: Set[str] = field(default_factory=set)
    ser: Set[str] = field(default_factory=set)


class ModelFieldsMixin(Protocol):
    class Meta:
        private_fields: Set[str] = set()
        public_fields: Set[str] = set()
        serializable_fields: Set[str] = set()
        non_serializable_fields: Set[str] = set()
        relationships: Dict[str, Relationship] = dict()
        _fields_cache: Dict[str, FieldsCache] = dict()

    @classmethod
    def _fields_cache_key(cls):
        return '.'.join([cls.__module__, cls.__qualname__])

    # noinspection PyProtectedMember
    @classmethod
    def _calculate_fields(cls):
        private_types = (
            type, FunctionType, MethodType, MappingProxyType,
            WrapperDescriptorType, MethodWrapperType, MethodDescriptorType,
            ClassMethodDescriptorType, GetSetDescriptorType, MemberDescriptorType
        )

        private_fields, public_fields, serializable_fields = set(), set(), set()
        relationship_keys = cls.Meta.relationships.keys()

        for attr in dir(cls):
            value = getattr(cls, attr)
            if isinstance(value, private_types) or attr[0] == '_':
                private_fields.add(attr)
            elif not isinstance(value, private_types):
                if not isinstance(value, property) and attr not in relationship_keys:
                    serializable_fields.add(attr)
                public_fields.add(attr)

        private_fields.update(cls.Meta.private_fields)
        private_fields.difference_update(cls.Meta.public_fields)
        public_fields.update(cls.Meta.public_fields)
        public_fields.difference_update(cls.Meta.private_fields)
        serializable_fields.update(cls.Meta.serializable_fields)
        serializable_fields.difference_update(cls.Meta.non_serializable_fields)
        cls.Meta._fields_cache[cls._fields_cache_key()] = \
            FieldsCache(priv=private_fields, pub=public_fields, ser=serializable_fields)

    # noinspection PyProtectedMember
    @classmethod
    def drop_fields_cache(cls):
        key = cls._fields_cache_key()
        cls.Meta._fields_cache.pop(key, None)

    # noinspection PyProtectedMember
    @classmethod
    def get_private_fields(cls) -> Set[str]:
        key = cls._fields_cache_key()
        if key not in cls.Meta._fields_cache:
            cls._calculate_fields()
        return cls.Meta._fields_cache[key].priv

    # noinspection PyProtectedMember
    @classmethod
    def get_public_fields(cls) -> Set[str]:
        key = cls._fields_cache_key()
        if key not in cls.Meta._fields_cache:
            cls._calculate_fields()
        return cls.Meta._fields_cache[key].pub

    @classmethod
    def get_fields(cls) -> Set[str]:
        return cls.get_public_fields()

    def get_values(
        self, only_fields: Sequence[str] = None,
            exclude_fields: Sequence[str] = None) -> Mapping[str, Any]:
        public_fields = self.get_public_fields()
        only_fields = set(only_fields) if only_fields else set()
        exclude_fields = set(exclude_fields) if exclude_fields else set()

        return {
            name: getattr(self, name) for name in public_fields
            if hasattr(self, name) and (not only_fields or name in only_fields)
            and (not exclude_fields or name not in exclude_fields)
        }

    @classmethod
    async def _build_rela(
            cls, instance: AbstractModel, load_fields: Optional[Set[str]] = None, **kwargs) -> Optional[AbstractModel]:
        res = await cls._build_relationships([instance], load_fields, **kwargs)
        return res[0]

    @classmethod
    async def _build_rela_list(
        cls, objects: Sequence[AbstractModel], load_fields: Optional[Set[str]] = None, **kwargs) \
            -> Sequence[AbstractModel]:
        return await cls._build_relationships(objects, load_fields, **kwargs)

    @classmethod
    async def _build_relationships(
        cls, objects: Sequence[AbstractModel], load_fields: Optional[Set[str]] = None, **kwargs) \
            -> Sequence[AbstractModel]:
        deps_ids: Dict[str, Dict[Any, Set[Any]]] = defaultdict(lambda: defaultdict(set))
        deps_values: Dict[str, Dict[Any, Any]] = defaultdict(dict)
        rela_map = cls.Meta.relationships.items()
        load_all = load_fields is None

        for instance in objects:
            if instance is None:
                continue

            for dep_key, relationship in rela_map:
                if not load_all and dep_key not in load_fields:
                    continue

                dep_key_value = relationship.get_key(instance)

                if relationship.single:
                    dep_key_value = [dep_key_value]

                deps_ids[dep_key][instance.get_id_value()].update(set(dep_key_value))

        for dep_key, relationship in rela_map:
            if not load_all and dep_key not in load_fields:
                continue

            dep_keys = set()
            for v in deps_ids[dep_key].values():
                dep_keys.update(v)
            model_class = relationship.get_model()
            dep_values = await model_class.get_any(list(dep_keys), **kwargs)

            for k, v in zip(dep_keys, dep_values):
                deps_values[dep_key][k] = v

        for instance in objects:
            if instance is None:
                continue

            for dep_key, relationship in rela_map:
                if not load_all and dep_key not in load_fields:
                    continue

                dep_key_values = list(deps_ids[dep_key][instance.get_id_value()])

                if relationship.single:
                    dep_key_value = dep_key_values[0] if len(dep_key_values) > 0 else dep_key_values
                    dep_value = deps_values[dep_key][dep_key_value]
                    setattr(instance, dep_key, dep_value)
                else:
                    dep_values = [deps_values[dep_key][k] for k in dep_key_values]
                    setattr(instance, dep_key, dep_values)

        return objects
