from fractions import Fraction

import music21

from major.pitch import Pitch
from major.degree import Degree
from major.type import Type


class Note(Pitch):
    def __init__(self, octave_offset: int, major_degree: Degree, quarter_length: Fraction):
        super().__init__(octave_offset, major_degree)
        self.quarter_length = quarter_length

    def to_note(self, major: Type, base_octave: int) -> music21.note.Note:
        n = music21.note.Note(self.to_pitch(major, base_octave))
        n.quarterLength = self.quarter_length
        return n
