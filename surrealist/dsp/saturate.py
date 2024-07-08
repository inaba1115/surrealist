import numpy as np

gain = 3.0


def saturate(sound_data: np.ndarray, mix: float) -> np.ndarray:
    mix = max(mix, 0.0)
    mix = min(mix, 1.0)
    if mix == 0.0:
        return sound_data

    dry = sound_data
    wet = np.tanh(sound_data * gain)

    ret = dry * (1 - mix) + (wet * mix)
    return np.clip(ret, a_min=-1, a_max=1)
