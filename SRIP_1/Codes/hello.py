import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

CHANNELS = 2
swidth = 4
Change_RATE = 2
T = 10
bits = int(sys.argv[3])
freq = int(sys.argv[2])
T = int(sys.argv[4])
audio = sys.argv[1]
#print(source)
q = 0.5
Q = 1/10
A = 1 # amplitude of signal # quatization stepsize
N = 2000
spf = wave.open(audio, 'rb')
CHANNELS=spf.getnchannels()
swidth = spf.getsampwidth()
RATE=spf.getframerate()
print(RATE)
Byte = spf.getsampwidth()
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
spf.close()
