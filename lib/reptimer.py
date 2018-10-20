import threading
import os, time
import logger

logger = logger.instance(__name__, os.environ.get('LOG_REPTIMER', 'ERROR'))

class RepeatedTimer(object):
    # https://stackoverflow.com/questions/18018033/how-to-stop-a-looping-thread-in-python

    actionThread = None
    stopEvent    = None

    def __init__(self, interval, function, args=[]):
        self.interval = interval
        self.action = function
        self.args = args

    def handle(self, stopEvent, action, args, interval):
        cnt = interval
        while not stopEvent.is_set():
            if cnt >= interval:
                try:
                    action(*args)
                except Exception as ex:
                    print (ex)
                    # self.stop()   # QUESTION
                    break
                cnt = 0
            cnt += 1
            if interval > 0:
                time.sleep(1)

    def start(self):
        self.stopEvent    = threading.Event()
        self.actionThread = threading.Thread(target=self.handle, args=(self.stopEvent, self.action, self.args, self.interval))
        self.actionThread.start()

    def stop(self):
        if self.actionThread:
            if self.actionThread.isAlive():
                self.stopEvent.set()
                self.actionThread.join()
        self.actionThread = None
        self.stopEvent    = None


if __name__ == '__main__':

    def action(t):
        print ("running ({})".format(t))

    timer = RepeatedTimer(1.0, action, ["test"])
    timer.start()
    print("S T A R T E D")
    time.sleep(5)
    print("T E R M I N A T I N G")
    timer.stop()
