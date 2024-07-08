import numpy as np

from .dsp_utils import alloc_data, time_to_samples


class Data:
    def __init__(self, init_cap_sec: float = 10.0) -> None:
        self.__len_samp = 0
        self.__cap_samp = time_to_samples(init_cap_sec)
        self.__data = alloc_data(self.__cap_samp)

    def __stretch(self, samp: int) -> None:
        self.__len_samp = samp

        if samp > self.__cap_samp:
            self.__cap_samp = int(samp * 1.5)
            data = alloc_data(self.__cap_samp)
            data[0 : self.__data.shape[0]] = self.__data
            self.__data = data

    def write(self, timestamp: float, sound_data: np.ndarray) -> None:
        start_samp = time_to_samples(timestamp)
        end_samp = start_samp + sound_data.shape[0]
        if end_samp > self.__len_samp:
            self.__stretch(end_samp)
        self.__data[start_samp:end_samp] += sound_data

    def get(self) -> np.ndarray:
        return self.__data[: self.__len_samp]
