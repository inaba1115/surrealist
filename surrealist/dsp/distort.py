import numpy as np

gain = 8.0
a_min = -0.25
a_max = 1.0


def distort(sound_data: np.ndarray, mix: float) -> np.ndarray:
    mix = max(mix, 0.0)
    mix = min(mix, 1.0)
    if mix == 0.0:
        return sound_data

    dry = sound_data
    wet = np.clip(sound_data * gain, a_min=a_min, a_max=a_max)

    ret = dry * (1 - mix) + (wet * mix)
    return np.clip(ret, a_min=-1, a_max=1)
