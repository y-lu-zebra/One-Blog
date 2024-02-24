FROM postgres:15
LABEL authors="Yu Lu"

ARG UID
ARG GID

ENV UID ${UID}
ENV GID ${GID}

RUN usermod -u ${UID} postgres && \
    groupmod -g ${GID} postgres
