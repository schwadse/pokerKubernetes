FROM python:3.11

ADD main.py .

RUN pip install poker
RUN pip install "fastapi[all]"

CMD [ "python", "./main.py" ]
