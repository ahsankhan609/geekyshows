# How to Make Django Application

## Create a new Django Project with the following steps

- [VirtualEnvironmentWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- pip install virtualenvwrapper-win
- mkvirtualenv virtual_environment_name
- workon virtual_environment_name ( to activate after deactivaiton)
- django-admin startproject *project_name* (usually prefered name is 'config') for easiness later on
- cd *project_name*
- python manage.py startapp *app_name*
- go to settings.py in the main project folder and add the *app_name* to the *INSTALLED_APPS['app_name']*

## Create function Based views

- go to *views.py* of the *app_name* where we need to write business logic.
- then *import djnago.http import HttpResponse* and then make functions
- then go to *settings.py* in the main project forlder
- then write import statement - *from app_name import views*
- find *urlpatterns=[]* in the *settings.py* file
- here we define our url like this - *path('url_name/',views.function_name_from_applicaiton)*
- if we have multiple applications then it will be difficult to manage URLS, so we will make alias for that purpose
- let's say we have *app_name_1* and *app_name_2, so when we import views from both applications then Django will be confused that how this will be handeld.
- so we make alias like this - *from app_name_1 import views as app1_views* & *from app_name_2 import views as app2_views*

### to make project more independent we will make urls in each application, so that we could use them in multiple applications

- we will use *include()* function in main applicaitons urls file in *url_pattern=[]*
- first of all make *urls.py* file in the application folder
- *path('url_name',include('app_name.urls')),*
- use this url to open - localhost:8000/app_name/function_name

### if we are making templates folder inside the main project folder

- go to *settings.py* of the main project folder
- add these two lines of code
- TEMPLATE_DIR = os.path.join(BASE_DIR , 'templates')
- the make 2 folders in the main project folder, named *templates* & 'static'. these are for HTML and CSS templates
- but if we make templates folder inside the application folder, then no need to add them in the *settings.py* file
- so if we have to make any HTML file realted to the app's then we make that app folder name inside templates folder, and then place related HTML files inside that, but if we make any HTML file realted to the main project then only place them inside the templates folder.
- then create the views.py file in the main project(config) folder and add its URL's inside the main project(condig) urls.py file. and add this code to import the views.py file - *from . import views*
- another approach is to make another *app* named *core* or *main_site*, then deal this app as main project. then we don;t need to make any views.py file in side the main project folder

### Static Folder

- make a static folder inside the main project folder. then go to *settings.py*
- STATIC_DIR = os.path.join(BASE_DIR , 'static')
- STATICFILES_DIRS = [STATIC_DIR]
- static/css/main.css
- static/js/main.js
- static/images/main.jpg
- then open HTML file and write this code above. - {% load static %}
- `<link href='{% static "css/main.css" %}'>`

### Filters for Django templates

- [Web Reference](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#built-in-filter-reference)
- *{{ }}* we will add variable in this format
- we will use *|* symbol for using *filters* with *variables* - e.g {{name|upper}} - it will make *NAME*

### Prepare base.html file

- make `base.html` in the `core_app` inside `templates/core/base.html`
- copy the repeated html code
- copy the `<title>` tag
- write this code inside `<title>` tag to make it dynamic across others - `<title>{% block title %} Default Value {% endblock title %}</title>`
- `{% block content %}{% endblock content %}`
- then in all other HTML pages we use these code - `{% extends 'core/base.html' %}`
- `<title>{% block title %} Home Page {% endblock title %}</title>`
- If we need to import default value as well we use - `<title>{% block title %}{block.super} Home Page {% endblock title %}</title>`
- `{% block content %}` I am new Home Page. `{% endblock content %}`

### Prepare URL for href tag

- use `{% url 'url_name' %}` - `'url_name'` is the name that we give in the urls.py file of the application/project

### use include tag to include other HTML page - we will use this approach to show any dynamically generated results,such as *ML recommedation system*

- let's say we have a *top course page*, so we will use it as follows:
- make top_pages.html page
- then use this code - `{% include template_folder_name/top_pages.html %}` to include that page into any page
- we can pass any custom value as well in it. like this -`{% include template_folder_name/top_pages.html with p='PHP' %}`
- then that variable name *p* will be shown on *top_pages.html* as django variable`{{ p }}`, to get its value in the main page
- and if i just want to show the 1 value in variable then i wil use like this - `{% include template_folder_name/top_pages.html with p='PHP' only %}`

## Changing Default Message Template `settings.py`

![Default Message Levels](static/notes_images/dj_messages_level.png)
![Default Message Options](static/notes_images/change_default_message_options.png)
