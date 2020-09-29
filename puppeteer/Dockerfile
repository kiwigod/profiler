FROM node:11.15

ADD . /app

WORKDIR /tmp

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y time procps libnss3 libatk-bridge2.0-0 libx11-xcb1 libxcb-dri3-0 libdrm-dev libgbm1 libasound2 libxss1 libgtk-3-0 > /dev/null 2>&1

# Additional package for firefox
RUN apt-get install -y libdbus-glib-1-2 > /dev/null 2>&1

# Setup Firefox nightly
RUN wget -q https://ftp.mozilla.org/pub/firefox/nightly/2020/09/2020-09-08-21-52-55-mozilla-central/firefox-82.0a1.en-US.linux-x86_64.tar.bz2 -O firefox_nightly.tar.bz2
RUN tar xjf firefox_nightly.tar.bz2
RUN mkdir -p /browsers
RUN mv firefox /browsers/
RUN ln -s /browsers/firefox/firefox /usr/local/bin/firefox

# # install chromium
RUN apt install -y chromium > /dev/null 2>&1

WORKDIR /app

# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result-chromium.log 2>&1"]
