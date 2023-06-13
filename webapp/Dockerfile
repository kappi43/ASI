ARG BASE_IMAGE=python:3.9-slim
FROM $BASE_IMAGE as runtime-environment

# install project requirements
COPY webapp/src/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# add kedro user
ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker

WORKDIR /home/kedro_docker
USER kedro_docker

# copy the whole project except what is in .dockerignore
ARG KEDRO_UID=999
ARG KEDRO_GID=0
COPY --chown=${KEDRO_UID}:${KEDRO_GID} ./webapp .

ENV MODEL_NAME="mlflowModel.pkl"

EXPOSE 5000

CMD flask --app webapp run --host=0.0.0.0 --port=5000
