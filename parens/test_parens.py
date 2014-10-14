import pytest
import parens


def test_parens_check(text):
    testing1 = "I (hate) extra('s in my (strings."
    assert parens_check(testing1) == 1
    testing2 = "I said) I hate ) extra (parens) in my strings."
    assert parens_check(testing1) == -1
    testing3 = "I (mean) it."
    assert parens_check(testing1) == 0
    testing4 = "well )( what about that."
    assert parens_check(testing1) == -1
    testing5 = "Sometimes there aren't any."
    assert = parens_check(testing5) == 0
    testing6 = 5555
    #assert parens_check(testing6)
    #Attribute Error