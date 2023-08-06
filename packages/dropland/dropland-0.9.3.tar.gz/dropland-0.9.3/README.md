Dropland
========

Mini-framework for building a backend servers for web-services using SQLAlchemy, Databases, Redis, RabbitMQ and APScheduler


How to build
------------

- Create a Python virtual environment.

    ``pyenv local 3.9.0``

    ``pip install --upgrade pip``

    ``poetry env use $(pyenv which python)``

    ``pip install poetry``


- Install the project

    ``poetry install --no-root --extras "extras"``


Where extras may be in: `sqla`, `db`, `redis`, `rmq`, `sqlite`, `pg`, `mysql`, `scheduler`, `fastapi`, `test`


- Start the docker environment for development

    ``docker-compose up -d``


- Run tests

    ``poetry run pytest``


- Stop the docker environment

    ``docker-compose down``


- Uninstall the project

    ``pip uninstall dropland -y``
