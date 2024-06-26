FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt


COPY ./ .
EXPOSE 9888

CMD [ "python", "app.py"]