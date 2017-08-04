FROM python:3.6.0-alpine
RUN pip install flask pymongo
ADD python/ /src
WORKDIR /src
EXPOSE  5000
ENTRYPOINT ["python3", "app.py"]
