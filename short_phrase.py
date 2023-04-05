class TestEx10:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        desired_length = 15
        assert len(phrase) < desired_length, f"length of the entered phrase is {len(phrase)}, which is more then {desired_length}"