# build stage
FROM node:lts-alpine
WORKDIR /app
COPY . .
RUN npm install
# RUN npm run build
CMD ["npm", "run", "serve"]

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]