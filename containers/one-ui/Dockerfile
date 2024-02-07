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
    chmod +x one-admin.sh && \
    bash one-admin.sh init --prod --front

EXPOSE 3000


FROM nginx
LABEL authors="Yu Lu"

# ARG UID
# ARG GID
# ARG USERNAME

# ENV UID ${UID}
# ENV GID ${GID}
# ENV USERNAME ${USERNAME}

# RUN addgroup -g ${GID} ${USERNAME} && \
#     adduser -u ${UID} -G ${USERNAME} -D ${USERNAME}

# COPY containers/one-server/conf.d/one.conf /etc/nginx/conf.d/default.conf

# RUN touch /var/run/nginx.pid && \
#   chown -R nginx:nginx /var/run/nginx.pid && \
#   chown -R nginx:nginx /var/cache/nginx

# USER nginx

COPY containers/one-server/conf.d/nginx.conf /etc/nginx/nginx.conf

RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid && \
    chown -R nginx:nginx /var/cache/nginx

USER nginx

CMD ["nginx"]
