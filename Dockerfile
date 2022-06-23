FROM python:3.8-slim

# hadolint ignore=DL3008
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update \
    && apt-get install --no-install-recommends -y  cmake gcc g++ build-essential \
    && pip install --no-cache-dir pip==20.3.1 \
    && pip install --no-cache-dir poetry==1.1.4 \
    && rm -rf /tmp/* /usr/share/doc/* /var/cache/* /var/lib/apt/lists/* /var/tmp/*

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml /app/

WORKDIR /app/
RUN poetry install --no-dev

COPY ./ /app/
CMD [ "poetry", "run" ]