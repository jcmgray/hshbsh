from hshbsh import Taxi
from hshbsh import input

t = Taxi()
js1 = {}
js1[0]= input.Journey(2, 0, 3, 0, 0, 3, 0)

res1 = t.do_closest(js1)

assert res1 == False

t = Taxi()

js2 = {}
js2[0] = input.Journey(2, 0, 3, 0, 1, 4, 0)
res2 = t.do_closest(js2)

assert res2 == True
assert len(js2) == 0
print(t)
