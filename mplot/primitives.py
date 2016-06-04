"""primitives objects
definitions:
pitch : C4, F#3, B2
pitch class :
"""

from collections import namedtuple


valid_pitch_class_names = set([
    'Ab', 'A', 'A#',
    'Bb', 'B', 'B#',
    'Cb', 'C', 'C#',
    'Db', 'D', 'D#',
    'Eb', 'E', 'E#',
    'Fb', 'F', 'F#',
    'Gb', 'G', 'G#',
])

Interval = namedtuple('Interval', ['short', 'long'])

named_intervals = [
    Interval('U', 'unisson'),
    Interval('b2', 'minor 2nd'),
    Interval('2', 'major 2nd'),
    Interval('b3', 'minor 3rd'),
    Interval('3', 'major 3rd'),
    Interval('4', '4rth'),
    Interval('T', 'triton'),
    Interval('5', '5th'),
    Interval('b6', 'minor 6th'),
    Interval('6', 'major 6th'),
    Interval('b7', 'minor 7th'),
    Interval('7', 'major 7th'),
    Interval('8', 'octave'),
    Interval('b9', 'minor 9th'),
    Interval('9', 'major 9th'),
    Interval('b10', 'minor 10th'),
    Interval('10', 'major 10th'),
    Interval('11', '11th'),
    Interval('TT', 'upper triton'),
    Interval('12', '12th'),
    Interval('b13', 'minor 10th'),
    Interval('13', 'major 13th'),
]


class PitchClass():
    """A pitch class like C, F#, B, ...
    """

    def __init__(self, pitch_class_name):
        if pitch_class_name in valid_pitch_class_names:
            self.pitch_class = pitch_class_name
        else:
            raise ValueError, "invalid pitch class name: {}".format(pitch_class_name)

    def __str__(self):
        return self.pitch_class


class Interval():
    """an interval
    """

    def validate_interval(self, interval):
        return interval

    def __init__(self, interval):
        self.interval = self.validate_interval(interval)

    def __str__(self):
        return str(self.interval)

    def name(self, name_type='short'):
        """try to name the interval, short and long form available
        """

        try:
            if self.interval < 0:
                raise IndexError
            interval = named_intervals[self.interval]
            if name_type == 'long':
                return interval.long
            elif name_type == 'short':
                return interval.short
            else:
                raise TypeError("wrong name type : " + str(name_type))
        except IndexError:
            return str(self)


class AbsoluteInterval(Interval):
    """a positive interval
    """

    def validate_interval(self, interval):
        return abs(interval)


class IntervalClass(Interval):
    """an interval reduced inside an octave
    """

    def validate_interval(self, interval):
        return interval % 12
