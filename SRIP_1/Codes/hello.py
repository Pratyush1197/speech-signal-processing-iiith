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

wf = wave.open(audio, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(freq)
wf.writeframes(signal)
wf.close()

def uniform_midtread_quantizer(x, Q):
    # limiter
    x = np.copy(x)

    idx = np.where(np.abs(x) >= 1)
    x[idx] = np.sign(x[idx])
    # linear uniform quantization
    xQ = Q * np.floor(x/Q + 1/2)

    return xQ

def plot_signals(x, xQ, T):
    e = xQ - x
    plt.figure(figsize=(10,6))
    plt.plot(xQ, label=r'quantized signal $x_Q[k]$')
    plt.xlabel(r'$k$')
    plt.axis([0, N, -T, T])
    plt.grid()
    plt.savefig('my_plot.png')

def plot_signalss(x, xQ, T):
    e = xQ - x
    plt.figure(figsize=(10,6))
    plt.plot(signal, label=r'quantized signal $x_Q[k]$')
    plt.xlabel(r'$k$')
    plt.axis([0, N, -T, T])
    plt.grid()
    plt.savefig('my_plot.png')

# generate signal
x = signal
# quantize signal
xQ = uniform_midtread_quantizer(x, Q)
# plot signals
if (bits < 3):
    plot_signals(x, xQ, T)
else:
    plot_signalss(x, xQ, T)    


