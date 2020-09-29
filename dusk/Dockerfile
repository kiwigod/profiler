FROM php:7.2

ADD . /app

RUN apt-get update > /dev/null 2>&1
# RUN apt-get install -y libzip-dev zlib1g-dev wget zip unzip time procps > dev/null 2>&1
RUN apt-get install -y time procps > dev/null 2>&1
# RUN apt-get install -y libnss3 libatk-bridge2.0-0 libx11-xcb1 libxcb-dri3-0 libdrm-dev libgbm1 libasound2 libxss1 libgtk-3-0 > /dev/null 2>&1

# RUN docker-php-ext-install zip

# RUN /app/install_composer.sh
RUN apt install -y /app/google-chrome_amd64.deb

WORKDIR /app/dusk

# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result-internal.log 2>&1"]
