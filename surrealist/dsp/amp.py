import numpy as np


def amp(sound_data: np.ndarray, gain: float) -> np.ndarray:
    gain = max(gain, 0.0)
    gain = min(gain, 2.0)
    if gain == 1.0:
        return sound_data

    return np.clip(sound_data * gain, a_min=-1, a_max=1)
