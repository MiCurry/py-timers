import time

class PyTimers:
    """ A small timer class in a similar vain as MPAS timers. Probably no the most efficent, but
    its easy to use. """

    def __init__(self):
        self.timers = {}

    def finalize(self):
        """ Stop all timers and report all of them """
        print("Timing report:")
        print("{:30.30} {:}".format('Name', 'Elapsed Time'))
        print("-"*45)
        for name in self.timers.keys(): # Stop all timers
            if self.timers[name][1] == None:
                self.stop_timer(name)

        for name in self.timers.keys(): # Print report
            self.report(name)

    def add_timer(self, name, start=True):
        if start:
            self.timers[name] = [time.time(), None]
        else:
            self.timers[name] = [None, None]

    def start_timer(self, name):
        if name in self.timers:
            self.timers[name][0] = time.time()
        else:
            raise KeyError('Timer {0} was not found'.format(name)) 

    def stop_timer(self, name):
        if name in self.timers:
            self.timers[name][1] = time.time()
        else:
            raise KeyError('Timer {0} was not found'.format(name)) 

    def report(self, name):
        """ Print out the curent elapse time of a clock """
        if name in self.timers:
            if self.timers[name][1] == None: # Finish this clock
                self.timers[name][1] = time.time()

            if self.timers[name][0] == None:
                print(name, ":\t This timer was never started",sep='')
            else:
                elapseTime = self.timers[name][1] - self.timers[name][0]
                print("{:30.30} {:f}".format(name, elapseTime))
                #print(name, ":\t", self.timers[name][1] - self.timers[name][0], sep='')
        else:
            raise KeyError("Timer '{0}' was not found".format(name)) 
