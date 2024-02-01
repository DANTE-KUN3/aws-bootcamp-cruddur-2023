FROM python:3.10-slim-buster

WORKDIR /backend-flask
# Install dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev postgresql-client \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]