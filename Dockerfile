# 
FROM python:3.12.3
# 
WORKDIR /code
# 
COPY ./src/requirements.txt /code/src/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/src/requirements.txt
# 
COPY ./app /code/app
# 