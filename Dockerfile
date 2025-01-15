FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip


WORKDIR /app


COPY . .

RUN pip install -r requirements.txt

USER app


CMD ["python", "manage.py", "runserver"]

