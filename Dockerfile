FROM debian:latest
RUN apt-get update && apt-get install -y texlive-latex-base texlive-xetex latex-cjk-japanese --no-install-recommends && apt-get clean && rm -rf /usr/share/doc/*
ADD https://github.com/googlei18n/noto-cjk/raw/master/NotoSansMonoCJKjp-Bold.otf /usr/share/fonts
ADD https://github.com/googlei18n/noto-cjk/blob/master/NotoSansMonoCJKkr-Regular.otf /usr/share/fonts
ADD https://github.com/googlei18n/noto-fonts/raw/master/hinted/NotoSerif-Regular.ttf /usr/share/fonts
VOLUME /work
WORKDIR /work
