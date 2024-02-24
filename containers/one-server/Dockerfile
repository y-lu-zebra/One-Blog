FROM nginx
LABEL authors="Yu Lu"

ARG UID
ARG GID

ENV UID ${UID}
ENV GID ${GID}

RUN usermod -u ${UID} nginx && \
    groupmod -g ${GID} nginx && \
    adduser nginx sudo && \
    touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /usr/share/nginx/html

CMD ["nginx"]
