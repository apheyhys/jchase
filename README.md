# Django-Rest React Blog
Multi Page Application with dynamic content loading
line-by-line filling from txt file,
dynamic content loading

### Stack:
- Django
- Ajax
- Bootstrap
- Docker / Docker-Compose 
- Nginx

# Usage

***docker*** and ***docker-compose*** must be installed on your computer.

## Configurations
- Create ***.env*** for Django in dir jchase/jchase/.env. For an example look at the file programsonline_backend/programsonline_backend/.env.example
- Create ***.env.db*** for Database in dir db-env/.env.db. For an example look at the file db-env/.env.example

## Run Project

### Run project for development environment 

```
docker-compose up
```

### Run project for production environment 

This script will also start your containers. In case you down your containers, you can restart them by following command,

```
docker-compose -f docker-compose.prod.yml up
```