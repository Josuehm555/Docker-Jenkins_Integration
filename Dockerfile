FROM python:3.9.6
ADD . /tarea
WORKDIR /tarea
RUN pip install -r requirements.txt
CMD ["python","./app.py"]