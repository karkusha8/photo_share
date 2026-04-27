FROM python:3.12-slim

WORKDIR /app

# install poetry
COPY pyproject.toml poetry.lock* /app/
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# copy project
COPY . /app

# run migrations + start app
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000