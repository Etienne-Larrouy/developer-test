FROM node:18.13.0-alpine AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

EXPOSE 80

FROM nginx:latest
COPY --from=build /app/dist/odds-app /usr/share/nginx/html
COPY --from=build /app/conf/nginx.conf /etc/nginx/conf.d/default.conf
