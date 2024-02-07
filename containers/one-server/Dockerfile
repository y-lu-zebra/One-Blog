FROM nginx
LABEL authors="Yu Lu"

ARG UID
ARG GID

ENV UID ${UID}
ENV GID ${GID}

COPY containers/one-server/conf.d/nginx.conf /etc/nginx/nginx.conf

RUN usermod -u ${UID} nginx && \
    groupmod -g ${GID} nginx && \
    touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid && \
    chown -R nginx:nginx /var/cache/nginx

CMD ["nginx"]
