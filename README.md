# My flask base app
Template for flask API

## RUN
docker build -t flask-base-app .
docker run --name flask-api -d -p 8080:8080 -v $PWD/:/app flask-base-app