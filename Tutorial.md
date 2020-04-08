Steps:
Ensure python3 is installed

Create GitHub repo
Clone Github repo locally
Create  pipenv
    pipenv install
Install Django zappa and zappa-django-utils to new pipenv
    pipenv install django zappa

Activate pipenv
    pipenv shell

Create new Django project
    django-admin startproject mis6384

Test the new project
    cd mis6384
    python manage.py runserver

Create new Django app
    python manage.py startapp outreach

Create the initial database
    python manage.py migrate

Define models
Define views
Define paths

Include app in project and execute DB migration

Create django superuser

Add app to admin portal

Create new AWS account
Create zappa user account for AWS
Create team user accounts
Configure Zappa to use AWS account
Install zappa s3 DB backend
