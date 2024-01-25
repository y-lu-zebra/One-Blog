FROM python:3.11
LABEL authors="Yu Lu"

RUN apt-get update \
        && apt-get upgrade \
        && apt-get install -y --no-install-recommends \
                postgresql-client \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir /code
WORKDIR /code
COPY ../.. .
RUN chmod +x one-admin.sh \
        && bash one-admin.sh init --prod --back

EXPOSE 8000

#CMD ["bash", "one-admin.sh", "start", "--back"]
