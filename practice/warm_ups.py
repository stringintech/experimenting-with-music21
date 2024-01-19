from fractions import Fraction

from major import Sequence, Degree, Note


def create_step_sequence(note_len: Fraction, rest_len: Fraction) -> Sequence:
    seq = Sequence()
    rest = Note.new_rest(rest_len)
    for d in [Degree.ONE, Degree.TWO, Degree.THREE, Degree.FOUR,
              Degree.FIVE, Degree.SIX, Degree.SEVEN]:
        seq.append(Note.new(0, d, note_len))
        seq.append(rest)
    for _ in range(2):
        seq.append(Note.new(1, Degree.ONE, note_len))
        seq.append(rest)
    for d in [Degree.SEVEN, Degree.SIX, Degree.FIVE, Degree.FOUR,
              Degree.THREE, Degree.TWO, Degree.ONE]:
        seq.append(Note.new(0, d, note_len))
        seq.append(rest)
    return seq


def create_arpeggio_sequence() -> Sequence:
    pass


def create_gravity_sequence() -> Sequence:
    pass


def create_tendency_sequence() -> Sequence:
    pass
