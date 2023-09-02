FROM debian:bullseye-slim

ARG FIP140_IMAGE=debian:bullseye-slim-fips-140-3

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install --no-cache-dir liboqs

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]
