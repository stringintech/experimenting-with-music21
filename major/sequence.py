import music21

from major.type import Type
from major.note import Note
from major.degree import Degree


class Sequence:
    notes: list[Note]

    def __init__(self, notes=None):
        if notes is None:
            notes = []
        self.notes = notes

    def append(self, note: Note):
        self.notes.append(note)

    @property
    def lowest_degree(self) -> Degree:
        d = Degree.SEVEN
        for note in self.notes:
            if not note.rest and note.major_degree.value < d.value:
                d = note.major_degree
        return d

    @property
    def lowest_degree_lowest_octave(self) -> int:
        o = None
        d = self.lowest_degree
        for note in self.notes:
            if not note.rest and note.major_degree == d and (o is None or note.octave_offset < o):
                o = note.octave_offset
        return o

    def to_notes(self, major: Type, base_octave: int) -> list[music21.note.Note]:
        octave_offset_correction = self.lowest_degree_lowest_octave
        notes = []
        for note in self.notes:
            if not note.rest:
                note.octave_offset -= octave_offset_correction
            notes.append(note.to_note(major, base_octave))
        return notes

