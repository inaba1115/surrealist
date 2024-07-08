from __future__ import annotations

import dataclasses


def _round(v: float) -> float:
    return round(v, 7)


@dataclasses.dataclass
class State:
    _timestamp: float = 0.0
    _length: float = 0.0
    _offset: float = 0.0
    _speed: float = 1.0
    _loop: float = 0.0  # 0.0 < sec (0.0 is disabled)
    _stutter: float = 1.0  # 1.0 < count
    _saturate: float = 0.0  # 0.0 <= mix <= 1.0
    _distort: float = 0.0  # 0.0 <= mix <= 1.0
    _down: float = 1.0  # 0.0 < rate <= 1.0
    _amp: float = 1.0  # 0.0 <= gain <= 2.0

    def timestamp(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._timestamp = _round(ret._timestamp + float(s[1:]))
        elif s.startswith("-"):
            ret._timestamp = _round(ret._timestamp - float(s[1:]))
        elif s.startswith("*"):
            ret._timestamp = _round(ret._timestamp * float(s[1:]))
        elif s.startswith("/"):
            ret._timestamp = _round(ret._timestamp / float(s[1:]))
        else:
            ret._timestamp = _round(float(s))
        return ret

    def length(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._length = _round(ret._length + float(s[1:]))
        elif s.startswith("-"):
            ret._length = _round(ret._length - float(s[1:]))
        elif s.startswith("*"):
            ret._length = _round(ret._length * float(s[1:]))
        elif s.startswith("/"):
            ret._length = _round(ret._length / float(s[1:]))
        else:
            ret._length = _round(float(s))
        return ret

    def offset(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._offset = _round(ret._offset + float(s[1:]))
        elif s.startswith("-"):
            ret._offset = _round(ret._offset - float(s[1:]))
        elif s.startswith("*"):
            ret._offset = _round(ret._offset * float(s[1:]))
        elif s.startswith("/"):
            ret._offset = _round(ret._offset / float(s[1:]))
        else:
            ret._offset = _round(float(s))
        return ret

    def speed(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._speed = _round(ret._speed + float(s[1:]))
        elif s.startswith("-"):
            ret._speed = _round(ret._speed - float(s[1:]))
        elif s.startswith("*"):
            ret._speed = _round(ret._speed * float(s[1:]))
        elif s.startswith("/"):
            ret._speed = _round(ret._speed / float(s[1:]))
        else:
            ret._speed = _round(float(s))
        return ret

    def loop(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._loop = _round(ret._loop + float(s[1:]))
        elif s.startswith("-"):
            ret._loop = _round(ret._loop - float(s[1:]))
        elif s.startswith("*"):
            ret._loop = _round(ret._loop * float(s[1:]))
        elif s.startswith("/"):
            ret._loop = _round(ret._loop / float(s[1:]))
        else:
            ret._loop = _round(float(s))
        return ret

    def stutter(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._stutter = _round(ret._stutter + float(s[1:]))
        elif s.startswith("-"):
            ret._stutter = _round(ret._stutter - float(s[1:]))
        elif s.startswith("*"):
            ret._stutter = _round(ret._stutter * float(s[1:]))
        elif s.startswith("/"):
            ret._stutter = _round(ret._stutter / float(s[1:]))
        else:
            ret._stutter = _round(float(s))
        return ret

    def saturate(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._saturate = _round(ret._saturate + float(s[1:]))
        elif s.startswith("-"):
            ret._saturate = _round(ret._saturate - float(s[1:]))
        elif s.startswith("*"):
            ret._saturate = _round(ret._saturate * float(s[1:]))
        elif s.startswith("/"):
            ret._saturate = _round(ret._saturate / float(s[1:]))
        else:
            ret._saturate = _round(float(s))
        return ret

    def distort(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._distort = _round(ret._distort + float(s[1:]))
        elif s.startswith("-"):
            ret._distort = _round(ret._distort - float(s[1:]))
        elif s.startswith("*"):
            ret._distort = _round(ret._distort * float(s[1:]))
        elif s.startswith("/"):
            ret._distort = _round(ret._distort / float(s[1:]))
        else:
            ret._distort = _round(float(s))
        return ret

    def down(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._down = _round(ret._down + float(s[1:]))
        elif s.startswith("-"):
            ret._down = _round(ret._down - float(s[1:]))
        elif s.startswith("*"):
            ret._down = _round(ret._down * float(s[1:]))
        elif s.startswith("/"):
            ret._down = _round(ret._down / float(s[1:]))
        else:
            ret._down = _round(float(s))
        return ret

    def amp(self, s: str) -> State:
        ret = dataclasses.replace(self)
        if s.startswith("+"):
            ret._amp = _round(ret._amp + float(s[1:]))
        elif s.startswith("-"):
            ret._amp = _round(ret._amp - float(s[1:]))
        elif s.startswith("*"):
            ret._amp = _round(ret._amp * float(s[1:]))
        elif s.startswith("/"):
            ret._amp = _round(ret._amp / float(s[1:]))
        else:
            ret._amp = _round(float(s))
        return ret
