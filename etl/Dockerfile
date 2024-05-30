# Use the official Python image from the Docker Hub
FROM python:3.12.3

WORKDIR /code
# 
COPY . /code/etl
# 
RUN pip install --no-cache-dir --upgrade -r /code/etl/requirements.txt
CMD tail -f /dev/null
# 