import librosa
import numpy as np

from ..wav_io import SAMPLE_RATE


def down(sound_data: np.ndarray, rate: float) -> np.ndarray:
    rate = max(rate, 0.0001)
    rate = min(rate, 1.0)
    if rate == 1.0:
        return sound_data

    target_sr = int(SAMPLE_RATE * rate)
    down_data = librosa.resample(y=sound_data, orig_sr=SAMPLE_RATE, target_sr=target_sr, res_type="linear", axis=0)
    up_data = librosa.resample(y=down_data, orig_sr=target_sr, target_sr=SAMPLE_RATE, res_type="linear", axis=0)
    up_data = up_data[: min(sound_data.shape[0], up_data.shape[0])]
    return up_data
