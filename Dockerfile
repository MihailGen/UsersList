FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash yt && chmod 777 /opt /run

WORKDIR /app

RUN mkdir /app/static && chown -R app:app /yt && chmod 755 /app

COPY --chown=app:app . .

RUN pip install -r requirements.txt

USER app

CMD ["python manage.py runserver"]
