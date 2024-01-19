from fractions import Fraction

from major import Sequence, Degree, Note


def create_step_sequence(note_len: float) -> Sequence:
    seq = Sequence()
    f = Fraction.from_float(note_len)
    rest = Note.new_rest(f)
    for d in [Degree.ONE, Degree.TWO, Degree.THREE, Degree.FOUR,
              Degree.FIVE, Degree.SIX, Degree.SEVEN]:
        seq.append(rest)
        seq.append(Note.new(0, d, f))
    for _ in range(2):
        seq.append(rest)
        seq.append(Note.new(1, Degree.ONE, f))
    for d in [Degree.SEVEN, Degree.SIX, Degree.FIVE, Degree.FOUR,
              Degree.THREE, Degree.TWO, Degree.ONE]:
        seq.append(rest)
        seq.append(Note.new(0, d, f))
    return seq


def create_arpeggio_sequence(note_len: float) -> Sequence:
    seq = Sequence()
    f = Fraction.from_float(note_len)

    notes = [
        Note.new(0, Degree.ONE, f),
        Note.new(0, Degree.THREE, f),
        Note.new(0, Degree.FIVE, f),
        Note.new(1, Degree.ONE, f),

        Note.new_rest(f),
        Note.new(1, Degree.ONE, f),
        Note.new(1, Degree.THREE, f),
        Note.new(1, Degree.FIVE, f),
    ]
    
    r = range(len(notes))
    for i in list(r) + list(reversed(r)):
        seq.append(notes[i])
    return seq


def create_gravity_sequence(note_len: float) -> Sequence:
    base_f = Fraction.from_float(note_len)
    double_f = Fraction.from_float(2*note_len)
    rest = Note.new_rest(base_f)

    seq = Sequence()

    seq.append(rest)
    seq.append(Note.new(1, Degree.ONE, double_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.TWO, base_f))
    seq.append(Note.new(1, Degree.ONE, double_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.THREE, base_f))
    seq.append(Note.new(1, Degree.TWO, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.FOUR, base_f))
    seq.append(Note.new(1, Degree.THREE, base_f))
    seq.append(Note.new(1, Degree.TWO, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))

    seq.append(rest)
    seq.append(Note.new(1, Degree.ONE, double_f))
    seq.append(rest)

    seq.append(Note.new(0, Degree.SEVEN, base_f))
    seq.append(Note.new(1, Degree.ONE, double_f))
    seq.append(rest)

    seq.append(Note.new(0, Degree.SIX, base_f))
    seq.append(Note.new(0, Degree.SEVEN, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))
    seq.append(rest)

    seq.append(Note.new(0, Degree.FIVE, base_f))
    seq.append(Note.new(0, Degree.SIX, base_f))
    seq.append(Note.new(0, Degree.SEVEN, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))

    return seq


def create_tendency_sequence(note_len: float) -> Sequence:
    base_f = Fraction.from_float(note_len)
    double_f = Fraction.from_float(2 * note_len)
    rest = Note.new_rest(double_f)

    seq = Sequence()

    seq.append(Note.new(1, Degree.ONE, double_f))
    seq.append(rest)

    seq.append(Note.new(0, Degree.SEVEN, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.TWO, base_f))
    seq.append(Note.new(1, Degree.ONE, base_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.THREE, base_f))
    seq.append(Note.new(1, Degree.FOUR, base_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.FIVE, base_f))
    seq.append(Note.new(1, Degree.SIX, base_f))
    seq.append(rest)

    seq.append(Note.new(1, Degree.SEVEN, base_f))
    seq.append(Note.new(2, Degree.ONE, base_f))
    seq.append(rest)

    seq.append(Note.new(2, Degree.TWO, base_f))
    seq.append(Note.new(2, Degree.ONE, base_f))
    seq.append(rest)

    return seq
