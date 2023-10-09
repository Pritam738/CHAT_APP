FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PATH="/home/user/.local/bin:${PATH}"

# Install sqlite3 on Alpine
RUN apk add --no-cache sqlite

WORKDIR /chat

RUN adduser -D user && chown -R user:user /chat
USER user

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./chat /chat
