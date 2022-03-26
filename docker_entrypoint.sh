#!/bin/sh

RED='\033[0;31m'
NC='\033[0m'    # No Color
printf "${RED}  printing pwd : ${NC} \n"

pwd
ls -al

python3 manage.py makemigrations
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input


# gunicorn SSIL_SSO_MS.wsgi:application --bind  0.0.0.0:8000
uvicorn FRS.asgi:application --reload --host 0.0.0.0 --port 8000 --use-colors --log-level info

#shebang
#!/bin/sh



