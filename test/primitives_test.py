import context
context.set_path()
from pytest import raises
from mplot.primitives import PitchClass, Interval, AbsoluteInterval, IntervalClass, IntervalSet, IntervalClassSet


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
from copy import deepcopy


def test_interval_set_wrong_addition():
    ints = IntervalSet()
    with raises(TypeError):
        ints.add("1000")


def test_add_integer_to_interval_set():
    ints = IntervalSet()
    ints.add(1000)
    ints2 = IntervalSet()
    ints2.add(Interval(1000))
    assert ints == ints2


def test_add_same_interval_to_set():
    reference = IntervalSet()
    reference.add(Interval(4))
    reference.add(Interval(5))
    ints = deepcopy(reference)
    # add something already present in the set
    ints.add(Interval(5))
    assert reference == ints
    # change order of addition
    ints_unord = IntervalSet()
    ints_unord.add(Interval(5))
    ints_unord.add(Interval(4))
    assert reference == ints_unord

# ---------------------IntervalClassSet---------------------


def test_interval_class_set_wrap_additions():
    ins = IntervalClassSet()
    ins.add(Interval(4))
    ins.add(Interval(-1))
    ins2 = IntervalClassSet()
    ins2.add(Interval(4))
    ins2.add(Interval(11))
    assert ins == ins2
