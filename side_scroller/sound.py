"""Music module."""
from random import randint
from itertools import accumulate
import pyxel


class Sound:
    """A class to provide music and sound."""

    def __init__(self):
        self.sound_speed = 26

        drums = self.convert_drums("b_h_s_HH b_b_shHH", speed=self.sound_speed)
        pyxel.sound(0).set(**drums)

        bass_line = (
            "e0e0rrrrre0"
            "g0g0d1d1rrd1e1"
            "e0e0rrrrre0"
            "g0g0d1d1f#0f#0g0g0"
            "e0e0rrrrre0"
            "g0g0d1d1rrd1e1"
            "e0re0re1re1r"
            "g0g0d1d1f#0f#0g0g0"
            "e0e0rrrrre0"
            "g0g0d1d1rrd1e1"
            "e0e0rrrrre0"
            "g0g0d1d1f#0f#0g0g0"
            "e0e0rrrrre0"
            "g0g0d1d1rrd1e1"
            "g1f#1e1d1b0a0g0f#0"
            "g0g0d1d1f#0f#0g0g0"
        )

        pyxel.sound(1).set(
            note=bass_line, tone="t", volume="7", effect="n", speed=self.sound_speed
        )
        pyxel.sound(2).set(
            note=bass_line, tone="s", volume="3", effect="f", speed=self.sound_speed
        )
        self.octave_shift(2)

        pyxel.sound(3).set(
            note="a1a2a3a4a4", tone="s", volume="2", effect="nnnnf", speed=7
        )

        pyxel.sound(4).set(
            note="", tone="s", volume="2", effect="n", speed=4
        )

        pyxel.sound(63).set(
            note="r" * 16, tone="s", volume="1", effect="n", speed=self.sound_speed
        )

    def start_music(self):
        self.background = 1
        pyxel.play(ch=0, snd=[0] * 15 + [63], loop=True)
        pyxel.play(ch=1, snd=1, loop=True)
        pyxel.play(ch=2, snd=2, loop=True)

    def sfx_pickup(self):
        pyxel.play(ch=3, snd=3)

    def sfx_jump(self):
        rand_ints = [randint(1,10) for _ in range(10)]
        rand_notes = list(accumulate(rand_ints))
        pyxel.sound(4).note = rand_notes
        pyxel.play(ch=3, snd=4)

    @staticmethod
    def octave_shift(snd, octaves=1):
        """Shift the notes of the given sound by the given amount of octaves."""

        note_shift = 12 * octaves
        pyxel.sound(snd).note = [i + note_shift if i != -1 else -1 for i in pyxel.sound(snd).note]

    @staticmethod
    def convert_drums(drum_string, speed=20):
        """Convert drum string to pyxel arguments to set a sound.
        
        Defines drum noises, and converts a simplified drum string into a full
        set of note, volume, tone, etc., which can be passed using the ** syntax
        to the pyxel.sound.set method.

        >>> convert_drums("b_s_ bbs_")
        {"note": "f0ra4rf0f0a4r",
         "tone": "n",
         "volume": "60206620",
         "effect": "f",
         "speed": 20}

        """

        noises = {}

        # Define drums

        noises["b"] = {"note": "f0", "tone": "n", "volume": "6", "effect": "f"}
        noises["s"] = {"note": "b3", "tone": "n", "volume": "2", "effect": "f"}
        noises["H"] = {"note": "b4", "tone": "n", "volume": "1", "effect": "n"}
        noises["h"] = {"note": "b4", "tone": "n", "volume": "1", "effect": "f"}
        noises["_"] = {"note": "r", "tone": "n", "volume": "0", "effect": "f"}

        # Construct output dict

        output = {"note": "", "tone": "", "volume": "", "effect": ""}

        for noise in drum_string.replace(" ", ""):
            for key in output:
                output[key] += noises[noise][key]

        output["speed"] = speed
        return output

