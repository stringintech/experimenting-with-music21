from major.degree import Degree
from major.type import Type


class Pitch:
    def __init__(self, octave_offset: int, major_degree: Degree):
        self.octave_offset = octave_offset
        self.major_degree = major_degree

    def to_pitch(self, major: Type, base_octave: int):
        semitones = 12 * (base_octave + self.octave_offset) + self.major_degree.semitones
        return major.first_degree_pitch.transpose(semitones)
