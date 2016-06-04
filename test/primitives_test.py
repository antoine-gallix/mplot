import context
context.set_path()
from pytest import raises
from mplot.primitives import PitchClass, Interval, AbsoluteInterval, IntervalClass, IntervalSet


# ---------------------pitch class---------------------


def test_valid_pitch_class():
    PitchClass('A')


def test_wrong_pitch_class():
    with raises(ValueError):
        PitchClass('Z')


# --------------------interval----------------------

def test_correct_small_interval():
    i = Interval(3)
    assert(str(i) == '3')
    assert(i.name() == 'b3')
    assert(i.name('long') == 'minor 3rd')
    with raises(TypeError):
        i.name('mille')


def test_big_interval():
    i = Interval(30)
    assert(str(i) == '30')
    assert(i.name() == '30')


def test_negative_small_interval():
    i = Interval(-5)
    assert(str(i) == '-5')
    assert(i.name() == '-5')


def test_negative_interval():
    i = Interval(-30)
    assert(str(i) == '-30')
    assert(i.name() == '-30')


def test_non_int_interval():
    with raises(TypeError):
        Interval("mille")


def test_interval_equality():
    assert Interval(4) == Interval(4)
    assert Interval(4) != Interval(5)

# --------------------AbsoluteInterval----------------------


def test_correct_absolute_interval():
    i = AbsoluteInterval(3)
    assert(str(i) == '3')
    assert(i.name() == 'b3')
    assert(i.name('long') == 'minor 3rd')


def test_negative_absolute_interval():
    """negative absolute interval is forbidden
    """
    i = AbsoluteInterval(-3)
    assert(str(i) == '3')
    assert(i.name() == 'b3')
    assert(i.name('long') == 'minor 3rd')

# --------------------IntervalClass----------------------


def test_interval_class():
    """interval out of range should wrap
    """

    i = IntervalClass(14)
    assert(str(i) == '2')
    i = IntervalClass(-2)
    assert(str(i) == '10')

# ---------------------IntervalSet---------------------


def test_interval_set_wrong_addition():
    ints = IntervalSet()
    with raises(TypeError):
        ints.add(1000)
