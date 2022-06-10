FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

COPY ./model.tflite /code/model.tflite

COPY models.py /code/models.py

COPY ./umkm.csv /code/umkm.csv

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]