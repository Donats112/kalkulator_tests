from ..main import sas, atn, rei, dal, kap

def test_sas():
    assert sas(4, 5) == 9
    assert sas(-4, 5) == 1
    assert sas(-4, -5) == -9
    assert sas(4, 5.4) == 9.4
    assert sas(-4.5, 5) == 0.5
    assert sas(0, 0) == 0.0

def test_atn():
    assert atn(4, 5) == -1
    assert atn(4, -5) == 9
    assert atn(-4, 5) == -9
    assert atn(4.5, 5.5) == -1
    assert atn(0, 0) == 0

def test_rei():
    assert rei(4, 5) == 20
    assert rei(-4, 5) == -20
    assert rei(-4, -5) == 20
    assert rei(4.2, 5) == 21
    assert rei(0, 5) == 0

def test_dal():
    assert dal(4, 5) == 0.8
    assert dal(20, 5) == 4
    assert dal(0, 5) == 0
    assert dal(0, 0) == "idiots"
    assert dal(2,3) == 0.66667

def test_kap():
    assert kap(2, 3) == 8
    assert kap(2, 0) == 1
    assert kap(2, 2) == 4
    assert kap(2, -3) == 0.125



test_sas()
test_atn()
test_rei()
test_dal()