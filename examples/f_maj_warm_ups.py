import music21.clef

import major
import practice

if __name__ == '__main__':
    warm_ups = [
        {
            "title": "f maj step",
            "seq": practice.warm_ups.create_step_sequence(1),
            "time_sig": "2/4",
            "play_oct": 3
        },
        {
            "title": "f maj arpeggio",
            "seq": practice.warm_ups.create_arpeggio_sequence(1),
            "time_sig": "4/4",
            "play_oct": 3
        },
        {
            "title": "f maj gravity",
            "seq": practice.warm_ups.create_gravity_sequence(1),
            "time_sig": "4/4",
            "play_oct": 4
        },
        {
            "title": "f maj tendency",
            "seq": practice.warm_ups.create_tendency_sequence(1),
            "time_sig": "4/4",
            "play_oct": 3
        }
    ]

    for w in warm_ups:
        title = w["title"]
        filename = title.replace(" ", "-")
        seq = w["seq"]
        time_sig = w["time_sig"]
        play_oct = w["play_oct"]
        s = practice.stream.create_playable(seq, 50, time_sig, major.Type.F, play_oct)
        s.write("midi", fp="./out/{0}.midi".format(filename))
        s = practice.stream.create_representable(title, seq, time_sig, major.Type.F, play_oct - 1,
                                                 music21.clef.BassClef())
        s.write("musicxml.pdf", fp="./out/{0}.pdf".format(filename))
