#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval
from unittest import main, TestCase
from math import sqrt
from io import StringIO
from numpy import sqrt, square, mean, subtract

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase):

    # ----
    # eval
    # ----

    def test_eval_1(self):
        r = StringIO("10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10040:\n3.3\n3.5\n3.8\n0.94\n")

    def test_eval_2(self):
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "2043:\n3.7\n2.4\n3.8\n0.91\n")

    def test_eval_3(self):
        r = StringIO("10851:\n1050707\n1359601\n2477968\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10851:\n3.7\n4.0\n3.7\n0.82\n")

   
# ----
# main
# ----			
if __name__ == '__main__':
    main()

""" #pragma: no cover
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Netflix.py          27      0      4      0   100%
TestNetflix.py      13      0      0      0   100%
------------------------------------------------------------
TOTAL               40      0      4      0   100%

"""
