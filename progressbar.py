import time
import sys

class Progressbar:
    def __init__(self):
        return
    def run(self, cb, secs):
        toolbar_width = 40
        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
        for i in range(toolbar_width):
            time.sleep(secs / 40)
            # update the bar
            sys.stdout.write("-")
            sys.stdout.flush()
        cb()
        sys.stdout.write("]\n") # this ends the progress bar
        print("done...")