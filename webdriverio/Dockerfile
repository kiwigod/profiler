FROM node:11.15

ADD . /app

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y time procps > /dev/null 2>&1

WORKDIR /app

# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result.log 2>&1"]
