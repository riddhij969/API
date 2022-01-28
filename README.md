# Django Rest Framework API

# Description
    This API uses GET/POST/PUT/DELETE request to communicate and HTTP response codes to indenticate status and errors. 
    All responses come in standard JSON. All requests must include a content-type of application/json and the body must be valid JSON.
    This API consists users.
    By default Django REST Framework will produce a response like:

    {
        "id": 1,
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "company_name": "Chanay, Jeffrey A Esq",
        "age": 48,
        "city": "Brighton",
        "state": "MI",
        "zip": 48116,
        "email": "josephine_darakjy@darakjy.org",
        "web": "http://www.chanayjeffreyaesq.com"
    },

# Prerequisites:

    . Python3
    . Pycharm
    . Django
    . Django REST Framework  
  
# Installation

    . pip install django
    . pip install djangorestframework
    . pip install mysqlclient
    . pip install oauth2
    . pip install requests
    . pip install django-heroku
    . pip install gunicorn
  
# Configure MySQL Database
  
    Open your settings.py file and make changes.

    'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'your schema name',   (In my case schema name is users)
          'USER': 'your user name',     (In my case user name is root)
          'PASSWORD': 'your user password',
          'HOST': 'localhost',
          'PORT': '3306',
      }

# Running/ Development

    . startproject
    . startapp
    . createsuperuser
    . python manage.py makemigrations
    . python manage.py migrate
    . python manage.py runserver
    . visit your API at http://127.0.0.1:8000/
    . For admin - http://127.0.0.1:8000/admin/
    . My user name - Riddhi
    . My user password - Rj@123456
    
   ![admin](https://user-images.githubusercontent.com/69605346/151615945-aa66433c-c138-42d4-a43c-980e759dc9a0.png)


   
    . For API View - http://127.0.0.1:8000/api/users/
    
   ![users list](https://user-images.githubusercontent.com/69605346/151615348-91cb960c-873f-4083-930b-ebdf71e8ff5e.png)

  
# Deploying
  
    . Create a Heroku account
    . Create a Heroku application
    . heroku login
    . git init
    . heroku git:remote -a <AppName>
    . git add .
    . git commit -m "first commit"
    . git push heroku master


# Postman Collection:

    <The request type>

    GET | POST | PUT | DELETE    
  
    The get() method sends a GET request to the specified url.
  ![Get](https://user-images.githubusercontent.com/69605346/151616795-b2c2c7d1-d1c5-42c8-a2c3-c74ed62bac41.png)

 
    The post() method is used to create a new user into the collection of users.
  ![Post data](https://user-images.githubusercontent.com/69605346/151617294-c70c2615-bbd0-4d71-aabb-3d033a25f29d.png)
  ![Post](https://user-images.githubusercontent.com/69605346/151617318-1c1bcc32-208a-4e0f-933f-3c37907f48f7.png)


  
    The put() method is used to update existing user.
  ![Put Data](https://user-images.githubusercontent.com/69605346/151617941-e6b47835-b11c-4ab5-9ad4-3e3696ac8145.png)
  ![Put](https://user-images.githubusercontent.com/69605346/151617971-ba913d21-9038-485a-b09c-19cff5cb3445.png)



    The delete() method is used to delete existing user.
  ![Delete](https://user-images.githubusercontent.com/69605346/96030508-b5459500-0e79-11eb-8b7a-c6b4dfa5231f.png)
  ![Delete Data](https://user-images.githubusercontent.com/69605346/151618603-b0e11838-2b88-401f-aece-df27bcf0e08a.png)
  ![Delete Confirm](https://user-images.githubusercontent.com/69605346/151618635-b3a6d254-64b2-4cb9-86a6-dbb0aed1b5a5.png)
  ![Delete](https://user-images.githubusercontent.com/69605346/151618788-71ec77e0-f946-4a40-9d29-7825c7a1fee4.png)

  
# Result

  ![Database](https://user-images.githubusercontent.com/69605346/96032084-d1e2cc80-0e7b-11eb-936e-da5b833a1def.png)
