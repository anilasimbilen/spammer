import time
from pynput.keyboard import Controller
from progressbar import Progressbar

class Spammer:
    def __init__(self, text="Sample Text", spamc=1, init_delay=5, is_splitted=False, suffix="\n", single_delay=0):
        self.text = text
        self.spamc = spamc
        self.init_delay = init_delay
        self.is_splitted = is_splitted
        self.suffix = suffix
        self.single_delay = single_delay
        self.keyboard = Controller()
    
    def run(self):
        prg = Progressbar()
        prg.run(self._sprun, self.init_delay)
    def _sprun(self):
        for count in range(self.spamc):
            if(self.is_splitted):
                splitted = self.text.split(" ")
                for x in splitted:
                    self.keyboard.type(x)
                    self.keyboard.type(self.suffix)
            else:
                self.keyboard.type(self.text)
                self.keyboard.type(self.suffix)
            time.sleep(self.single_delay)