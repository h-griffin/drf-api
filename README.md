# Django rest framework with docker

> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir tree_api_project

Use poetry to initialize folder 

> $ cd `tree_api_project`
> $ poetry init -n
> $ poetry add django
> $ poetry add --dev black
> $ poetry shell

> $ django-admin startproject tree_api_project .
> $ python manage.py startapp trees

> $ Python manage.py runserver
    
> $ Python manage.py createsuperuser

**tree_api_project/settings.py**
- INSTALLED_APPS
- REST_FRAMEWORK

**trees/models.py**
- tree model class

> $ make migrations
> $ migrate

**trees/tests.py**
- set up test data
- test tree content

**tree_api_project/urls.py**
- ```path('api/v1/trees/', include('trees.urls')),```

**trees/urls.py**
- ```path('<int:pk>/', TreesDetail.as_view(), name='trees_detail'),```

**trees/serializers.py**
- model info

**trees/views.py**
- ```ListCreateAPIView```
- ```RetrieveUpdateDestroyAPIView```

> $ runserver

**touch Dockerfile**

**touch docker-compose.yml**


> $ docker-compose up

> $ docker-compose down

**tree_api_project/settings.py**
- ```ALLOWED_HOSTS = [ '0.0.0.0', ]```
