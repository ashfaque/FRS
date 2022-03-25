# To remove dangling <none> images use -----> docker rmi $(docker images -f "dangling=true" -q)
# ---------------------------------------------------------------------------------------------

FROM python:3.6.8-slim-stretch

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

# Running project using uvicorn with logging.
# critical/fatal: the crucial part of the application is not working, so a total failure. [OR] Severe error that will prevent the application from continuing.
# error: Error events that might still allow the application to continue running. [OR] Record of critical errors that are encountered.
# warning: Event that may result in future problems/errors.
# info: day-to-day operation as "proof" that program is performing its function as designed.
# debug: Fine-grained informational events that are most useful to debug an application. [OR] information important for troubleshooting, and usually suppressed in normal day-to-day operation.
# trace: finer-grained informational events than the DEBUG. [OR] Fine-grained debug message, typically capturing the flow through the application.

# --log-level <str>: Options: 'critical', 'error', 'warning', 'info', 'debug', 'trace'. Default: 'info'.
CMD [ "uvicorn", "FRS.asgi:application", "--reload", "--host", "0.0.0.0", "--port", "8000", "--use-colors", "--log-level", "info" ]
