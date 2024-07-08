from dataclasses import dataclass

import numpy as np

from .dsp import amp, distort, down, loop, saturate, speed, stutter
from .dsp_utils import alloc_data, time_to_samples
from .state import State


@dataclass
class Event:
    cmd: str
    state: State

    def render(self, sounds: dict[str, list[np.ndarray]]) -> np.ndarray | None:
        if self.cmd == "~":
            return None

        if ":" not in self.cmd:
            s, n = self.cmd, "0"
        else:
            s, n = self.cmd.split(":")
        sound_data = sounds[s][int(n)]

        sound_data = self.__trim(sound_data)

        sound_data = speed(sound_data, self.state._speed)
        sound_data = loop(sound_data, self.state._loop)
        sound_data = stutter(sound_data, self.state._stutter)
        sound_data = saturate(sound_data, self.state._saturate)
        sound_data = distort(sound_data, self.state._distort)
        sound_data = down(sound_data, self.state._down)
        sound_data = amp(sound_data, self.state._amp)

        return sound_data

    def __trim(self, sound_data: np.ndarray) -> np.ndarray:
        if self.state._length > 0.0:
            length_samp = time_to_samples(self.state._length)
        else:
            length_samp = sound_data.shape[0]

        offset_samp = time_to_samples(self.state._offset) % sound_data.shape[0]

        data = alloc_data(length_samp)
        size = min(sound_data.shape[0] - offset_samp, length_samp)
        data[0:size] = sound_data[offset_samp : offset_samp + size]
        return data
