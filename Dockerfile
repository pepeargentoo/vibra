FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "app/main.py"]
