from caluclator import add, div

# test addition function 
def test_add():
    assert add(5,6) == 11

def test_add1():
    assert add(5,6) == 10


# test divison function 
def test_div1():
    assert div(10,2) == 5.0


def test_div2():
    assert div(10,2) == 5.1


# run using pytest 
# assert is check if conditon is true 