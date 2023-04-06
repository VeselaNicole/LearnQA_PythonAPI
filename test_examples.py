class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert (a, b) == (b, a)


    def test_check_math2(self):
        a = 5
        b = 9
        assert a+b == 14