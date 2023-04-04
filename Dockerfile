FROM python:3.11

ADD main.py .

RUN pip install poker

CMD [ "python", "./main.py" ]
