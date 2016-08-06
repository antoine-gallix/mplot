import context
context.set_path()
from pytest import raises
from mplot.primitives import PitchClass, Interval, AbsoluteInterval, IntervalClass, IntervalSet, IntervalClassSet, Pitch


# ---------------------pitch---------------------


# ---------------------pitch class---------------------

def test_valid_pitch_class():
    PitchClass('A')
    PitchClass('D#')
    PitchClass('Gb')


def test_wrong_pitch_class():
    with raises(ValueError):
        PitchClass('Z')


def test_string():
    p = PitchClass('A')
    assert 'A' == str(p)


def test_location():
    p = PitchClass('A')
    p._location() == 0


def test_add_interval():
    p = PitchClass('A')
    i = Interval(3)
    raised = p + i
    assert raised == PitchClass('C')


def test_add_interval_type_error():
    p = PitchClass('A')
    i = 3
    with raises(TypeError):
        p + i


def test_add_negative_interval_wrap():
    p = PitchClass('A')
    i = Interval(-3)
    raised = p + i
    assert raised == PitchClass('F#')


def test_add_interval_wrap():
    p = PitchClass('F')
    i = Interval(7)
    raised = p + i
    assert raised == PitchClass('C')


def test_add_negative_interval():
    p = PitchClass('G')
    i = Interval(-7)
    raised = p + i
    assert raised == PitchClass('C')


def test_substract_interval():
    p = PitchClass('C')
    i = Interval(7)
    lowered = p - i
    assert lowered == PitchClass('F')


def test_add_absolute_interval():
    p = PitchClass('C')
    i = AbsoluteInterval(-7)
    raised = p + i
    assert raised == PitchClass('G')


def test_substract_absolute_interval():
    p = PitchClass('C')
    i = AbsoluteInterval(-7)
    raised = p - i
    assert raised == PitchClass('F')


def test_add_interval_class():
    p = PitchClass('C')
    i = IntervalClass(16)
    raised = p + i
    assert raised == PitchClass('E')


def test_substract_interval_class():
    p = PitchClass('C')
    i = IntervalClass(16)
    raised = p - i
    assert raised == PitchClass('Ab')

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


def test_interval_from_other_interval():
    i = Interval(4)
    ai = AbsoluteInterval(-4)
    ic = IntervalClass(16)

    i2 = Interval(i)
    assert i2 == i

    i3 = Interval(ai)
    assert i3 == ai

    i4 = Interval(ic)
    assert i4 == ic


def test_compare_interval_to_integer():
    i = Interval(4)
    assert i == 4

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


def test_create_absolute_interval_from_interval():
    # creation from interval should work and make conversion
    i = Interval(-5)
    ai = AbsoluteInterval(i)
    assert ai == Interval(5)

# --------------------IntervalClass----------------------


def test_interval_class():
    """interval out of range should wrap
    """
    i = IntervalClass(14)
    assert(str(i) == '2')
    i = IntervalClass(-2)
    assert(str(i) == '10')


def test_create_interval_class_from_interval():
    # creation from interval should work and make conversion
    i = Interval(16)
    ic = IntervalClass(i)
    assert ic == Interval(4)

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
