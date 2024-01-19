import music21.meter

from major import Sequence, Type


def create_playable(seq: Sequence, tempo: int, time_sig: str, major_type: Type,
                    base_octave: int) -> music21.stream.Stream:
    s = music21.stream.Stream()
    s.append(music21.tempo.MetronomeMark(number=tempo))
    s.append(music21.meter.TimeSignature(time_sig))
    s.append(seq.to_notes(major_type, base_octave))
    return s


def create_representable(title: str, seq: Sequence, time_sig: str, major_type: Type, base_octave: int,
                         clef: music21.clef.Clef) -> music21.stream.Stream:
    s = music21.stream.Stream()
    s.insert(0, music21.metadata.Metadata())
    s.metadata.title = title
    s.metadata.composer = ''
    s.append(music21.meter.TimeSignature(time_sig))
    s.append(clef)
    s.append(seq.to_notes(major_type, base_octave))
    return s
