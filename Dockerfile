# for Raspberry Pi
FROM mvkvl/circus-armhf

# for x86_64 PC
# FROM mvkvl/circus


MAINTAINER kami <kami@slink.ws>

ENV DEBIAN_FRONTEND noninteractive

RUN \
 apt-get update && apt-get -y upgrade     && \
 apt-get install -y --no-install-recommends  \
             gcc python3.5-dev libffi-dev    \
             libssl-dev                   && \
#
 pip3 install PyYAML urllib3 docutils     && \
 pip3 install influxdb                    && \
 pip3 install pysnmp                      && \
 pip3 install python-daemon               && \
 pip3 install python-telegram-bot         && \
 pip3 install RPi.GPIO                    && \
#
 apt-get remove -y gcc python3.5-dev         \
                   libffi-dev                \
                   libssl-dev             && \
 apt-get autoremove -y                    && \
 apt-get clean                            && \
 rm -rf /var/lib/apt/lists/*              && \
 echo "Done!"

CMD ["circusd", "/etc/circus.conf"]
