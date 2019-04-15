FROM node:lts-alpine

WORKDIR /

COPY package.json ./
COPY yarn.lock ./

RUN yarn global add @vue/cli
RUN yarn install

COPY . .

RUN yarn build

EXPOSE 8080

CMD ["yarn", "serve-dockercompose"]
