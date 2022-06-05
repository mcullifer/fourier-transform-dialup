import scipy.io.wavfile as wavfile
import scipy.signal as signal

def read_audio(file_path):
    samplerate, data = wavfile.read(file_path,mmap=True)
    return samplerate, data

def short_time_fourier(data, samplerate, window):
    spectrum = signal.stft(
                            x = data, 
                            fs = samplerate,
                            window = window,
                            nperseg = window.size,
                            return_onesided = True,
                            boundary = 'zeros',
                            padded = True)
    return spectrum

