FROM node:20
LABEL authors="Yu Lu"

WORKDIR /code
COPY ../.. .

RUN chmod +x one-admin.sh && \
    bash one-admin.sh init --prod --front

EXPOSE 3000
