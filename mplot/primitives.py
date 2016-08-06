"""primitives objects
definitions:
pitch : C4, F#3, B2
pitch class :
"""

from collections import namedtuple
from data_structures import CircularList

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
        # transformation of the integer that represents the interval, child
        # class override this functions
        return interval

    def __init__(self, interval):
        # the internal represantation of the interval is an integer
        # acceptable initial values are integers or Interval objects
        if isinstance(interval, int):
            # set internal interval from int
            self.interval = self.prepare_interval(interval)
        elif isinstance(interval, Interval):
            # set internal interval from other Interval
            self.interval = self.prepare_interval(interval.interval)
        else:
            raise TypeError(
                "type must be one of {}".format(["int", "Interval"]))

    def __str__(self):
        return str(self.interval)

    def __eq__(self, interval):
        # two intervals are equal if they have the same internal interger
        # representation
        if isinstance(interval, Interval):
            # compare to other Interval
            return self.interval == interval.interval
        elif isinstance(interval, int):
            # compare to int
            return self.interval == interval
        else:
            raise NotImplementedError(
                "Interval compare only to other Interval or int")

    def __hash__(self):
        # intervals are identified by their internal integer representation
        return self.interval

    def as_int(self):
        # integer representation of the interval
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
    """a set of intervals, to represent scales and chords relative to a central point
    """

    internal_interval_class = Interval

    def validate_interval(self, interval):
        if not isinstance(interval, self.internal_interval_class):
            # try conversion
            try:
                return self.internal_interval_class(interval)
            except TypeError:
                raise TypeError("interval must have type " +
                                str(self.internal_interval_class))
        return interval

    def __init__(self):
        self._set = set([])

    def add(self, interval):
        """add an interval to the set
        """
        validated = self.validate_interval(interval)
        self._set.add(validated)

    def __str__(self):
        return str([str(e) for e in self._set])

    def __eq__(self, other_interval_set):
        """comparison of two interval sets
        """

        if not isinstance(other_interval_set, IntervalSet):
            raise TypeError(
                "IntervalSet can only compare to another IntervalSet")
        return self._set == other_interval_set._set


class IntervalClassSet(IntervalSet):
    """a set of intervals inside an octave
    """
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

pitch_class_circle = CircularList([
    ['A'],
    ['Bb', 'A#'],
    ['B', 'Cb'],
    ['C', 'B#'],
    ['C#', 'Db'],
    ['D'],
    ['D#', 'Eb'],
    ['E', 'Fb'],
    ['F', 'E#'],
    ['F#', 'Gb'],
    ['G'],
    ['Ab', 'G#'],
])


class PitchClass():
    """A pitch class like C, F#, B, ...
    Internal state is the name itself if validated.
    """

    def __init__(self, pitch_class_name):
        """pitch class must be initialized with a valid pitch class name.
        Invalid pitch name leads to a ValueError.
        """
        if self._validate(pitch_class_name):
            self.pitch_class = pitch_class_name
        else:
            raise ValueError, "invalid pitch class name: {}".format(pitch_class_name)

    def __str__(self):
        """str conversion is the name itself
        """
        return self.pitch_class

    def _validate(self, pitch_class_name):

        return pitch_class_name in valid_pitch_class_names

    def _locate(self, pitch_class_name):
        """locate a pitch class in the pitch class circle
        """
        for l, pitch_class in pitch_class_circle.enumerate():
            if pitch_class_name in pitch_class:
                return l
        raise ValueError, "invalid pitch class name: {}".format(pitch_class_name)

    def _location(self):
        return self._locate(self.pitch_class)

    def add_interval(self, interval):
        """add an interval to the pitch class. a pitch class wraps. ex: PitchClass(G) + Interval(2) = PitchClass(A)
        """
        new_location = self._location() + interval.as_int()
        return PitchClass(pitch_class_circle[new_location][0])

    def __add__(self, thing):
        if isinstance(thing, Interval):
            return self.add_interval(thing)
        else:
            raise TypeError('substracted value shall be an Interval')

    def __sub__(self, interval):
        """add an interval to the pitch class. a pitch class wraps. ex: PitchClass(A) - Interval(2) = PitchClass(G)
        """
        new_location = self._location() - interval.as_int()
        return PitchClass(pitch_class_circle[new_location][0])

    def __eq__(self, pitchclass):
        return self._location() == pitchclass._location()


class Pitch(PitchClass):
    """An absolute pitch like A4, Db6
    """
    pass


class PitchClassSet():
    """a set of pitch class, like the theorical notes of a chord or a scale
    """
    pass


class PitchSet():
    """a set of pitch class, like a real chord of scale
    """
    pass
