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
  ![Delete Data](https://user-images.githubusercontent.com/69605346/151618603-b0e11838-2b88-401f-aece-df27bcf0e08a.png)
  ![Delete Confirm](https://user-images.githubusercontent.com/69605346/151618635-b3a6d254-64b2-4cb9-86a6-dbb0aed1b5a5.png)
  ![Delete](https://user-images.githubusercontent.com/69605346/151618788-71ec77e0-f946-4a40-9d29-7825c7a1fee4.png)

  
# Result with Database

  ![Database](https://user-images.githubusercontent.com/69605346/151619326-8b376260-7458-4015-adc0-d60f82ccafc2.png)
  
 
# Pagination

  ![Screenshot (593)](https://user-images.githubusercontent.com/69605346/151621402-d4a40c68-188f-45e4-bb8b-35a6cde7c13e.png)
![Screenshot (594)](https://user-images.githubusercontent.com/69605346/151621406-b6c73075-a1ef-45f8-825a-8011205c07a2.png)
![Screenshot (597)](https://user-images.githubusercontent.com/69605346/151621411-5137d3ed-d78c-4c88-80dc-5ec735f08b37.png)
![Screenshot (604)](https://user-images.githubusercontent.com/69605346/151621412-6937b34c-cccd-4d6e-aa35-dd0798734375.png)
![Screenshot (605)](https://user-images.githubusercontent.com/69605346/151621415-e268463b-ce4c-4070-a368-25e30b7b4818.png)
![Screenshot (606)](https://user-images.githubusercontent.com/69605346/151621417-4df896a9-14c7-4de5-8225-caadfadac6c4.png)
![Screenshot (607)](https://user-images.githubusercontent.com/69605346/151621421-71edaed4-54f8-40e0-9822-c243983ab11a.png)
![Screenshot (608)](https://user-images.githubusercontent.com/69605346/151621423-b86c43ee-b8d5-4534-a1d1-a00741eef244.png)
![Screenshot (609)](https://user-images.githubusercontent.com/69605346/151621424-d4327738-4f22-40c7-beeb-e1218264d8ec.png)
![Screenshot (610)](https://user-images.githubusercontent.com/69605346/151621425-df0bff4c-cccb-40e7-aca5-d333148c43b4.png)
![Screenshot (611)](https://user-images.githubusercontent.com/69605346/151621428-e1384712-8dec-4d86-943b-3aae02e6843c.png)
![Screenshot (612)](https://user-images.githubusercontent.com/69605346/151621429-2418d5a1-9d90-4464-9502-4fa4b76bc143.png)
![Screenshot (613)](https://user-images.githubusercontent.com/69605346/151621430-240f6388-6b43-49b0-bdfc-a8b87db5aa66.png)
![Screenshot (614)](https://user-images.githubusercontent.com/69605346/151621431-7ab21198-63b8-4491-af82-156005226a61.png)
![users list](https://user-images.githubusercontent.com/69605346/151621436-eab5f206-5f62-4528-8368-9503a0ad7efd.png)

