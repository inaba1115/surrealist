import logging
from pathlib import Path

import numpy as np

from .wav_io import SAMPLE_RATE, read_wav

logger = logging.getLogger(__name__)


def load_sounds(sounds_dir: str) -> dict[str, list[np.ndarray]]:
    """Directory structure is similar to that used by TidalCycles.

    .
    ├─bd
    │   ├── 00_bd.wav
    │   ├── 01_bd.wav
    ...
    ├─sn
    │   ├── 00_sn.wav
    │   ├── 01_sn.wav
    ...

    """
    sounds_dir_expanded = Path(sounds_dir).expanduser()
    sounds = sorted(list(sounds_dir_expanded.glob("*/*.wav")))
    return __load(sounds, str(sounds_dir_expanded))


def __load(sounds: list[Path], sounds_dir: str) -> dict[str, list[np.ndarray]]:
    ret: dict[str, list[np.ndarray]] = {}
    for sound in sounds:
        name = str(sound.relative_to(sounds_dir).parent)
        if name not in ret:
            ret[name] = []

        wav = read_wav(str(sound))

        i = len(ret[name])
        sec = wav.shape[0] / SAMPLE_RATE
        file_name = sound.relative_to(sounds_dir)
        logger.info(f"{name}:{i}, {sec:.3f} sec, {file_name}")

        ret[name].append(wav)
    return ret
