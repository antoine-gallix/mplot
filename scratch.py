from mplot.primitives import IntervalSet, Interval, IntervalClassSet

ins = IntervalClassSet()
ins.add(Interval(4))
ins.add(Interval(-1))
ins2 = IntervalClassSet()
ins2.add(4)
ins2.add(Interval(11))
print "ins",
print ins
print "ins==ins2",
print ins == ins2
