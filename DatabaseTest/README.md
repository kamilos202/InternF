## InternF

# Prerequisites:
Docker v18.09.9
Docker-compose version 3
Django >2.0.7
Python 3.7.4
MySQL 5.7

# Steps to run the project (Linux):

First, Install Docker.

Clone this repository:

	$ git clone https://github.com/kamilos202/InternF.git

Go to the project directory:

	$ cd InternF

Build docker-compose.yml:

	$ sudo docker-compose build
	$ sudo docker-compose up -d

Make sure that container is running

	$ sudo docker ps

To see requests to the app type:

	$ sudo docker-compose logs
