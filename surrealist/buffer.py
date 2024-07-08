import copy

import numpy as np

from .data import Data
from .event import Event
from .sounds_loader import load_sounds
from .wav_io import play_data, write_wav


class RenderedBuffer:
    def __init__(self, data: np.ndarray) -> None:
        self.__data = data

    def write(self, out_dir: str) -> None:
        write_wav(self.__data, out_dir)

    def play(self) -> None:
        play_data(self.__data)


class EventBuffer:
    def __init__(self) -> None:
        self._events: list[Event] = []

    def append(self, event: Event) -> None:
        self._events.append(copy.deepcopy(event))

    def render(self, sounds_dir: str) -> RenderedBuffer:
        sounds = load_sounds(sounds_dir)

        data = Data()
        for event in self._events:
            event_data = event.render(sounds)
            if event_data is None:
                continue  # rest note

            data.write(event.state._timestamp, event_data)

        return RenderedBuffer(np.clip(data.get(), a_min=-1, a_max=1))
