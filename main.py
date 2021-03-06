from signal_processing import *
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def main():
    # Read file
    file_path = "sounds\RockWeller_56k.wav"
    samplerate, signal = read_audio(file_path)
    signal = (signal / 128) - 1

    # Short time fourier transform
    window = np.hanning(951)
    f, t, Zxx = short_time_fourier(signal, samplerate, window)
    Zxx_abs = np.abs(Zxx)
    

    # Clean up df to remove extreme values
    df = pd.DataFrame(Zxx_abs)
    df = df.iloc[: , 1:]
    
    # Plot
    fig = go.Figure(data=[go.Surface(z=df.values, x=t, y=f)])
    fig.update_layout(title="Dialup Modem Handshake Short Time Fourier Transform")
    fig.write_html("graphs\graph.html")
    fig.write_image("graphs\graph.png", scale=2)

if __name__ == "__main__":
    main()
