class Bird:

    def __init__(self):
        print('bird is ready')

    def whoIsthis(self):
        print('bird')
    
    def swim(self):
        print('swim faster')

class Penguin(Bird):

    def __init__ (self):
        super().__init__()
        print('penguin IS READY')
    
    def whoIsthis(self):
        print('penguin')

    def run (self):
        print('Runfaster')

peggy = Penguin()
peggy.whoIsthis
peggy.swim()
peggy.run