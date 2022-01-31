# Dockerfile
FROM python:3.8
COPY deploy/requirements.txt /
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/main.py"]