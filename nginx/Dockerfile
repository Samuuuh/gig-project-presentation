FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN apk add certbot certbot-nginx

COPY nginx.conf /etc/nginx/conf.d
#RUN certbot --nginx --non-interactive --agree-tos -m diogosamuelfernandes@outlook.com -d samuh.tech
