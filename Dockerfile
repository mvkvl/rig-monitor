FROM mvkvl/circus
MAINTAINER kami <kami@slink.ws>

# apt install pysnmp
RUN \
 pip3 install PyYAML urllib3 docutils     && \
 pip3 install python-daemon pysnmp        && \
 pip3 install influxdb circus-web         && \
 pip3 install python-telegram-bot

CMD ["circusd", "/etc/circus.conf"]
