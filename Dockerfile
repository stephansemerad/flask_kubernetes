FROM python:3.7

RUN mdkir /app
WORKDIR /app/
ADD . /app/

RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]