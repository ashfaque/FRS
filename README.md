# FRS
Face Recognition System for Students' Attendance using Django &amp; ML

![Banner](https://www.invixium.com/wp-content/uploads/2021/04/ixm-titan-banner.jpg)

### Run with
`uvicorn FRS.asgi:application --reload --host 0.0.0.0 --port 8888  --use-colors --log-level info`

### Run these commands first
    python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic

> https://github.com/fabiocaccamo/django-admin-interface
`python manage.py loaddata admin_interface_theme_bootstrap.json`

Django Admin: 127.0.0.1:8888/admin
Username: admin
Password: admin