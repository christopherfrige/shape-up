FROM python:3.12.8-slim
RUN apt-get update && apt-get -y install libffi-dev wget unzip

ENV DEPLOY_PATH=/var/www/shape-up
RUN mkdir -p $DEPLOY_PATH
WORKDIR $DEPLOY_PATH

COPY pyproject.toml $DEPLOY_PATH/pyproject.toml
COPY poetry.lock $DEPLOY_PATH/poetry.lock

RUN pip install -U pip && pip install -U setuptools && pip install poetry
RUN poetry install --no-interaction --without dev

COPY . $DEPLOY_PATH/.

EXPOSE 8000
