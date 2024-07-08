import numpy as np

from ..dsp_utils import samples_to_time, time_to_samples


def loop(sound_data: np.ndarray, sec: float) -> np.ndarray:
    sound_sec = samples_to_time(sound_data.shape[0])

    sec = max(sec, 0.0)
    sec = min(sec, sound_sec)
    if sec == 0.0:
        return sound_data
    if sec == sound_sec:
        return sound_data

    step_samp = time_to_samples(sec)
    i = 0
    while True:
        if i > sound_data.shape[0]:
            return sound_data
        size = min(step_samp, sound_data.shape[0] - i)
        sound_data[i : i + size] = sound_data[0:size]
        i += step_samp
