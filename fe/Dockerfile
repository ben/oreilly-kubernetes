FROM nginx
ENTRYPOINT ["nginx", "-g", "daemon off;"]
EXPOSE 8000

COPY dev /app-dev
COPY prod /app-prod

# Production by default
COPY nginx-prod.conf /etc/nginx/nginx.conf
# use "-c /etc/nginx/nginx-dev.conf" as a command to serve dev assets
COPY nginx-dev.conf /etc/nginx/nginx-dev.conf
