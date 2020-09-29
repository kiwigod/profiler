FROM node:11.15

ADD . /app

RUN apt-get update > /dev/null 2>&1
RUN apt-get install -y time procps > /dev/null 2>&1

# Firefox addition
RUN apt-get install -y libgtk-3-0 libdbus-glib-1-2 > /dev/null 2>&1

WORKDIR /tmp

# Install Firefox
RUN wget -q https://ftp.mozilla.org/pub/firefox/releases/80.0.1/linux-x86_64/en-US/firefox-80.0.1.tar.bz2 -O firefox-80.tar.bz2
RUN tar xjf firefox-80.tar.bz2
RUN mkdir -p /browsers
RUN mv firefox /browsers/
RUN ln -s /browsers/firefox/firefox /usr/local/bin/firefox

# Install Firefox driver
RUN wget -q https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz -O geckodriver.tar.gz
RUN tar xzf geckodriver.tar.gz
RUN mv geckodriver /usr/local/bin/

# Install chrome
RUN apt install -y /app/google-chrome_amd64.deb > /dev/null 2>&1

# Install chrome driver
RUN wget -q https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip -O chromedriver.zip
RUN unzip chromedriver.zip
RUN mv chromedriver /usr/local/bin/

WORKDIR /app
# CMD "/app/start.sh"

CMD ["/bin/sh", "-c", "(/usr/bin/time /app/test.sh) >> /app/result-firefox.log 2>&1"]
