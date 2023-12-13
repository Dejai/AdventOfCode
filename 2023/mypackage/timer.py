import time

class MyTimer:
    def __init__(self, save=False):
        self.Start = None
        self.End = None
        self.Save = save

    def start(self):
        self.Start = time.time()
        print("Timer started at: {}".format(self.Start))

    def stop(self):
        self.End = time.time()
        print("Timer stopped at: {}".format(self.End))
        print(self.getRunTime())
        if self.Save:
            self.save()

    def getRunTime(self):
        return "Run time: {}".format((self.End - self.Start))

    def print(self):
        print(self.getRunTime())

    def save(self):
        with open("./runTime.txt", "a+") as output:
            output.write(self.getRunTime() + "\n")