from rtlsdr import RtlSdr
import dmrutils

reciever = RtlSdr()

reciever.sample_rate = 2.048e6 #hz
reciever.center_freq = 70e6    #hz
reciever.freq_correcetion = 60 #PPM
reciever.gain = 'auto'

print(reciever.read.samples(1024))