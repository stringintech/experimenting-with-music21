import music21

from major.type import Type
from major.note import Note


class Sequence:
    notes: list[Note]

    def __init__(self, notes=None):
        if notes is None:
            notes = []
        self.notes = notes

    def append(self, note: Note):
        self.notes.append(note)

    def to_notes(self, major: Type, base_octave: int) -> list[music21.note.Note]:
        notes = []
        for note in self.notes:
            notes.append(note.to_note(major, base_octave))
        return notes

