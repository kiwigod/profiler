FROM php:7.2

ADD . /app

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y wget zip unzip time procps > dev/null 2>&1

WORKDIR /app

RUN /app/install_composer.sh

# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result.log 2>&1"]
