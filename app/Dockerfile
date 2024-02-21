FROM python:3.8-slim
LABEL maintainer="Your Name <your.email@example.com>"

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "app.py"]
