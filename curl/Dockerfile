FROM php:7.2

ADD . /app
WORKDIR /app

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y time procps > /dev/null 2>&1

# CMD ["/app/start.sh"] # start container in busy loop

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result.log 2>&1"]
