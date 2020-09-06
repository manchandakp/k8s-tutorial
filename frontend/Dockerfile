FROM node:14.8.0-alpine3.10 AS builder

WORKDIR /usr/src/app

COPY ./project/package.json ./
RUN npm install --silent

COPY ./project/ ./
RUN npm run-script build

FROM nginx:alpine

COPY --from=builder /usr/src/app/build/ /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
