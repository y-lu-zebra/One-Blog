FROM node:20
LABEL authors="Yu Lu"

WORKDIR /code
COPY ../.. .

ARG UID
ARG GID

ENV UID ${UID}
ENV GID ${GID}

RUN usermod -u ${UID} node && \
    groupmod -g ${GID} node && \
    chmod +x admin.sh && \
    bash admin.sh init --prod --front

EXPOSE 3000
