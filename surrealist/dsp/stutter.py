import numpy as np


def stutter(sound_data: np.ndarray, count: float) -> np.ndarray:
    count = max(count, 1.0)
    count = min(count, 100000.0)
    if count == 1.0:
        return sound_data

    step_samp = int(sound_data.shape[0] / count)
    i = 0
    while True:
        if i > sound_data.shape[0]:
            return sound_data
        size = min(step_samp, sound_data.shape[0] - i)
        sound_data[i : i + size] = sound_data[0:size]
        i += step_samp
