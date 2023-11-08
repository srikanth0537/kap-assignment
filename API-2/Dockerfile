FROM python:3.8


WORKDIR /flask-app


COPY requirements.txt /flask-app/


RUN pip install -r requirements.txt --no-cache-dir


COPY . /flask-app/


CMD ["python", "app2.py"]

