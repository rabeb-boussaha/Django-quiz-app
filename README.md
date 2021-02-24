![](https://miro.medium.com/max/2160/0*5Cke19b5MtU2WL5i.png)

# Django quiz web app

A simple quiz web app based on Django and SqlLite 

<img alt="GitHub followers" src="https://img.shields.io/github/followers/kalifiabillal?color=yellow&label=kalifiabillal&style=for-the-badge">   <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/kalifiabillal/Android-Arduino-Automotive?style=for-the-badge">   <img alt="Visual Studio App Center (Minimum) OS Version" src="https://img.shields.io/visual-studio-app-center/releases/osver/kalifiabillal/Android-Arduino-Automotive/a87b9e745655355612fff4418953e0c3f7074250?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Kalifiabillal/Android-Arduino-Automotive?color=green&style=for-the-badge">   <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/y/kalifiabillal/Android-Arduino-Automotive?style=for-the-badge">

## Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/sswapnil2/django-quiz-web-app.git`<br>
  `cd django-quiz-web-app`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
4) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

4) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 

