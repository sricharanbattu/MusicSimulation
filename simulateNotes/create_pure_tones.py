import numpy as np
import matplotlib
import matplotlib.pyplot as plt

K = 1000;

def getFrequency(note):
    A4 = 440;
    n = len(note);
    assert(n==2 or n==3);
    #write the values of the tones
    diction1 = {'C': -9, 'D': -7, 'E': -5, 'F': -4,'G':-2,'A':0, 'B':2};
    diction2 = {'#':1, 'b':-1};
    
    
    assert(note[0] in diction1);
    if n==3:
        assert(note[1]=='#' or note[1]=='b');
     
    dif = (int(note[-1]) -4)*12 + diction1[note[0]];
    if n==3:
        dif += diction2[note[1]];
        
    return A4*(2**(dif/12));


def createAudioPureFrequency(freq, Fs=16*K, interval=2, phase=0):
    assert Fs >= 2*freq, "Aliasing occuring";
    length = int(Fs*interval);
    n = np.linspace(0, length, length );
    signal_x = np.cos(2*np.pi*(freq/Fs)*n + phase);
    return signal_x