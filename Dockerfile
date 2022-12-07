FROM python:3.10 as base

# Perform common operations

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY pyproject.toml poetry.toml /app/
WORKDIR /app
RUN poetry install
COPY todo_app /app/todo_app

# Configure for production

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

# Configure for development

FROM base as development
ENTRYPOINT poetry run flask run --host 0.0.0.0 