FROM node:11.15

ADD . /app

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y time procps > /dev/null 2>&1

WORKDIR /tmp
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -O phantomjs.tar.bz2
RUN tar xjf phantomjs.tar.bz2
RUN mv /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin

RUN npm install -g casperjs

WORKDIR /app

# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result.log 2>&1"]
