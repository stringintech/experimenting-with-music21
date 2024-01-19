import enum


class Degree(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

    @property
    def semitones(self):
        if self is Degree.ONE:
            return 0
        if self is Degree.TWO:
            return 2
        if self is Degree.THREE:
            return 4
        if self is Degree.FOUR:
            return 5
        if self is Degree.FIVE:
            return 7
        if self is Degree.SIX:
            return 9
        if self is Degree.SEVEN:
            return 11
