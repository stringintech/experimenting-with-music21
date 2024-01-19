from fractions import Fraction

import music21

from major.pitch import Pitch
from major.degree import Degree
from major.type import Type


class Note(Pitch):
    def __init__(self, octave_offset: int | None, major_degree: Degree | None, rest: bool, quarter_length: Fraction):
        super().__init__(octave_offset, major_degree)
        self.quarter_length = quarter_length
        self.rest = rest

    @staticmethod
    def new(octave_offset: int, major_degree: Degree, quarter_length: Fraction):
        return Note(octave_offset, major_degree, False, quarter_length)

    @staticmethod
    def new_rest(quarter_length: Fraction):
        return Note(None, None, True, quarter_length)

    def to_note(self, major: Type, base_octave: int) -> music21.note.Note:
        n = music21.note.Note(self.to_pitch(major, base_octave)) \
            if not self.rest else music21.note.Rest()
        n.quarterLength = self.quarter_length
        return n

    def to_pitch(self, major: Type, base_octave: int) -> music21.pitch.Pitch:
        if self.rest:
            raise TypeError("cannot get rest note's pitch")
        return super().to_pitch(major, base_octave)
