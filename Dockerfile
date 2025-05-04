FROM python:3.9
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code
CMD ["python", "app.py"]