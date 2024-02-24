FROM python:3.11
LABEL authors="Yu Lu"

RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY ../.. .

ARG UID
ARG GID
ARG USERNAME

ENV UID ${UID}
ENV GID ${GID}
ENV USERNAME ${USERNAME}

RUN groupadd -g ${GID} ${USERNAME} && \
    useradd -u ${UID} -g ${USERNAME} -m ${USERNAME} && \
    chmod +x one-admin.sh && \
    bash one-admin.sh init --prod --back

EXPOSE 8000
