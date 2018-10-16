import signal

class GracefulKiller:
    kill_now = False
    def __init__(self, logger=None, shutdown_function=None):
        self.logger = logger
        self.shutdown_function = shutdown_function
        signal.signal(signal.SIGINT,  self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    def exit_gracefully(self, signum, frame):
        print()
        if self.logger:
            self.logger.info("shutting down")
        self.kill_now = True
        if self.shutdown_function:
            self.shutdown_function()
