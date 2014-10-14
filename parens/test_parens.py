import pytest
import parens


def test_parens_check():
    testing1 = "I (hate) extra('s in my (strings."
    assert parens.parens_check(testing1) == 1
    testing2 = "I said) I hate ) extra (parens) in my strings."
    assert parens.parens_check(testing2) == -1
    testing3 = "I (mean) it."
    assert parens.parens_check(testing3) == 0
    testing4 = "well )( what about that."
    assert parens.parens_check(testing4) == -1
    testing5 = "Sometimes there aren't any."
    assert parens.parens_check(testing5) == 0
    testing6 = "Sometimes it's (weird)(."
    assert parens.parens_check(testing6) == 1
    testing6 = 5555
    
def test_parens_error():
    with pytest.raises(AttributeError):
        parens.parens_check(555)
    