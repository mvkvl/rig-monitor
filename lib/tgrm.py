import os
import telegram
from telegram.error import NetworkError, Unauthorized

class TelegramSender:
    def __init__(self, token=None, chat=None, logger=None):
        self.logger = logger
        self.token  = token if token else os.environ.get('TELEGRAM_TOKEN', '<default value>')
        self.chat   = chat  if chat  else os.environ.get('TELEGRAM_CHAT' , '<default value>')
        self.bot    = telegram.Bot(self.token)

    def send(self, message, symbol):
        if symbol:  text = "{} {}".format(symbol.decode('unicode-escape'), message)
        else:       text = message
        try:
            self.bot.sendMessage(self.chat, text, parse_mode='html')
        except (NetworkError, Unauthorized) as err:
            if self.logger:
                self.logger.error(str(err))
