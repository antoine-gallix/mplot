from mplot.primitives import PitchClass
from mplot.primitives import Interval

# for n in [13, 0, -5, 16, 20, 40]:
#     i = Interval(n)
#     print "{} : {} : {}".format(n, i.name(), i.name('long'))


for i in [-10, -7, -5, -3, 0, 1, 4, 5, 7, 13]:
    print "{} : {}".format(i, i % 5)
