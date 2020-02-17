# InternF

Steps to run the projects:

First, Install Docker, docker-compose.

Clone this repository:
```
$ git clone https://github.com/kamilos202/InternF.git
```
Go to the project directory:
```
$ cd InternF
```
Build docker-compose.yml:
```
 $ sudo docker-compose build
 $ sudo docker-compose run app python manage.py migrate
 $ sudo docker-compose up -d
```
Make sure that container is running
```
 $ sudo docker ps
```
To see requests to the app type:
```
 $ sudo docker-compose logs
```

Go to the website:

# localhost:8000/echo
# localhost:8000/random

# Prerequisites:
Docker v18.09.9
Docker-compose version 3
Django >2.0.7
Python 3.7.4
postgres db



