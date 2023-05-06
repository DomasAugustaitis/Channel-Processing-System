import numpy as np

class channel_processor:

    A, B, C, X, Y = [], [], [], [], []
    m, c, b = None, None, None

    def __init__(self, channels_dir = "./", parameters_dir = "./") -> None:
        # Read channels
        f = open(channels_dir + "channels.txt", "r")
        channels = f.read().split(", ")
        channels[-1] = channels[-1].strip()
        channels[1:] = [float(chan) for chan in channels[1:]]
        if channels[0] == "X": self.X = channels[1:]
        elif channels[0] == "Y": self.Y = channels[1:]
        elif channels[0] == "A": self.A = channels[1:]
        elif channels[0] == "B": self.B = channels[1:]
        elif channels[0] == "C": self.C = channels[1:]
        f.close()

        #Read parameters
        f = open(parameters_dir + "parameters.txt", "r")
        for line in f.readlines():
            param = line.split(", ")
            if param[0] == "m": self.m = float(param[1].strip())
            elif param[0] == "c": self.c = float(param[1].strip())
            elif param[0] == "b": self.b = float(param[1].strip())

    #Y = mX + c
    def func1(self):
        self.Y = [self.m * X + self.c for X in self.X]

    #B = A + Y
    #b = mean(B)
    def func2(self):
        for i in range(len(self.A)):
            self.B.append(self.A[i] + self.Y[i])
        self.b = np.mean(self.B)

    #A = 1 / X
    def func3(self):
        self.A = [1 / X for X in self.X]

    #C = X + b
    def func4(self):
        self.C = [self.b + X for X in self.X]

        
        

        