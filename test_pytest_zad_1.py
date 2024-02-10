from pytest_zad_1 import function
import  pytest

@pytest.fixture()
def Var():
    return 15

def test_pif_paf(Var):
    assert function(Var) == "Pif Paf"

def test_pif_or_paf():
    assert  function(5) == "Pif"
    assert  function(3) == "Paf"

def test_miss():
    assert  function(7) == ""