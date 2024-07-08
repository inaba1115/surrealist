import math

import librosa
import numpy as np

from .wav_io import CHANNEL_NUM, SAMPLE_RATE


def time_to_samples(sec: float) -> int:
    return int(librosa.time_to_samples(times=sec, sr=SAMPLE_RATE))


def samples_to_time(samples: int) -> float:
    return float(librosa.samples_to_time(samples=samples, sr=SAMPLE_RATE))


def alloc_data(samples: int) -> np.ndarray:
    return np.zeros(shape=(samples, CHANNEL_NUM), dtype=np.float32)


def mag2db(mag: float) -> float:
    return 20 * math.log10(mag)


def db2mag(db: float) -> float:
    return math.pow(10, db / 20)
