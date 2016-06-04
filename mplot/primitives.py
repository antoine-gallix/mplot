"""primitives objects
definitions:
pitch : C4, F#3, B2
pitch class :
"""

from collections import namedtuple

# ---------------------Intervals---------------------
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


class Interval():
    """an interval
    """

    def prepare_interval(self, interval):
        # change incoming int to correct int
        return interval

    def set_interval(self, interval):
        if isinstance(interval, int):
            self.interval = self.prepare_interval(interval)
        elif isinstance(interval, Interval):
            self.interval = self.prepare_interval(interval.interval)
        else:
            raise TypeError(
                "type must be one of {}".format(["int", "Interval"]))

    def __init__(self, interval):
        # the internal represantation of the interval is an integer
        self.set_interval(interval)

    def __str__(self):
        return str(self.interval)

    def __eq__(self, interval):
        # two intervals are equal if they have the same internal interger
        # representation
        if not isinstance(interval, Interval):
            raise NotImplemented
        return self.interval == interval.interval

    def __hash__(self):
        # intervals are identified by their internal integer representation
        return self.interval

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

    def prepare_interval(self, interval):
        return abs(interval)


class IntervalClass(Interval):
    """an interval reduced inside an octave
    """

    def prepare_interval(self, interval):
        return interval % 12


class IntervalSet():
    internal_interval_class = Interval

    def validate_interval(self, interval):
        if not isinstance(interval, self.internal_interval_class):
            # try conversion
            return self.internal_interval_class(interval)

            raise TypeError("interval must have type " +
                            str(self.internal_interval_class))
        return interval

    def __init__(self):
        self._set = set([])

    def add(self, interval):
        validated = self.validate_interval(interval)
        self._set.add(validated)

    def __str__(self):
        return str([str(e) for e in self._set])

    def __eq__(self, other_interval_set):
        if not isinstance(other_interval_set, IntervalSet):
            raise TypeError(
                "IntervalSet can only compare to another IntervalSet")
        return self._set == other_interval_set._set


class IntervalClassSet(IntervalSet):
    internal_interval_class = IntervalClass

# ---------------------Pitches---------------------

valid_pitch_class_names = set([
    'Ab', 'A', 'A#',
    'Bb', 'B', 'B#',
    'Cb', 'C', 'C#',
    'Db', 'D', 'D#',
    'Eb', 'E', 'E#',
    'Fb', 'F', 'F#',
    'Gb', 'G', 'G#',
])


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
