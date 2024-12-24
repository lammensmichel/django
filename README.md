# web service with python django and  postgres

## swagger url 

 http://localhost:8000/swagger/

## migrate

### for init
docker exec -it  django-web-1 python manage.py migrate --fake sessions zero
docker exec -it  django-web-1 python manage.py migrate
### for app
docker exec -it  django-web-1 python manage.py makemigrations
docker exec -it  django-web-1 python manage.py migrate

##create admin
docker exec -it  django-web-1 python manage.py createsuperuser

user : root password toor

## create app

docker exec -it  django-web-1 python manage.py startapp todo

## run test 

docker exec -it  django-web-1 python manage.py test


## install requirements 

docker exec -it  django-web-1 pip install -r requirements.txt

## exemple url 

http://localhost:8000/hello/mimi 
