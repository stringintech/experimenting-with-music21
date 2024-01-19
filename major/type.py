import music21
import enum


class Type(enum.Enum):
    C = 0
    G = 1
    F = 2

    @property
    def first_degree_pitch(self):
        symbol = ""
        if self is Type.C:
            symbol = "C"
        elif self is Type.G:
            symbol = "G"
        elif self is Type.F:
            symbol = "F"
        else:
            raise ValueError("invalid major type")
        return music21.pitch.Pitch(symbol+"0")
