FROM python:3.9-alpine

WORKDIR /action
COPY ./src .

ENTRYPOINT [ "python" ]
CMD [ "/action/main.py" ]