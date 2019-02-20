# Fast Api Docker

From this https://github.com/tiangolo/uwsgi-nginx-flask-docker, I found this

https://github.com/tiangolo/fastapi

---

Using the Dockerfile

```ssh
docker container stop flask-server-container && docker container rm -f flask-server-container && docker image rm flask-server-image

docker build -t flask-server-image ./ && docker run -d --name flask-server-container -p 5000:80 flask-server-image

```

Using docker-compose file

```ssh

docker-compose up

```
