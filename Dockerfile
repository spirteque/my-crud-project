FROM python:3.12-alpine3.20

COPY . /my-crud-project
WORKDIR /my-crud-project

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
