FROM node:16.20.2-buster as build

WORKDIR /app

COPY . .

RUN npm install --global yarn --force

CMD ["yarn"]
CMD ["yarn", "start"]