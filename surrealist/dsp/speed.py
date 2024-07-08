import librosa
import numpy as np

from ..wav_io import SAMPLE_RATE


def speed(sound_data: np.ndarray, rate: float) -> np.ndarray:
    if rate == 1.0:
        return sound_data
    if rate == -1.0:
        return sound_data[::-1]

    rate_abs = abs(rate)
    rate_abs = max(rate_abs, 0.1)
    rate_abs = min(rate_abs, 100)

    target_sr = int(SAMPLE_RATE / rate_abs)
    resample_data = librosa.resample(y=sound_data, orig_sr=SAMPLE_RATE, target_sr=target_sr, res_type="linear", axis=0)
    resample_data = resample_data[: min(sound_data.shape[0], resample_data.shape[0])]

    if rate < 0:
        resample_data = resample_data[::-1]

    return resample_data
