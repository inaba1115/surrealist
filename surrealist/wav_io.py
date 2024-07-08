import time
from pathlib import Path

import librosa
import numpy as np
import sounddevice as sd  # type: ignore
from scipy.io import wavfile  # type: ignore

SAMPLE_RATE = 44100
CHANNEL_NUM = 2
OUT_FILE = "{}.wav"


def read_wav(filename: str) -> np.ndarray:
    y, _ = librosa.load(filename, sr=SAMPLE_RATE, dtype=np.float32, mono=False)
    y = y.T
    if y.shape[1] != CHANNEL_NUM:
        raise
    return y


def write_wav(data: np.ndarray, out_dir: str) -> None:
    filename = Path(out_dir).expanduser() / OUT_FILE.format(int(time.time()))
    wavfile.write(filename=filename, rate=SAMPLE_RATE, data=data)


def play_data(data: np.ndarray) -> None:
    sd.play(data, SAMPLE_RATE)
    sd.wait()
