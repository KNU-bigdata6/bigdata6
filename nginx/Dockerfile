# Dockerfile

FROM nginx:1.17.8


RUN mkdir /var/cache/nginx/temp
RUN mkdir /var/cache/nginx/cache
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

COPY proxy_params /etc/nginx/proxy_params
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/default.conf
RUN mkdir /var/log/nginx/default/
