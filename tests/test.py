from mypackage import myModule

def test_top_n():
    assert myModule.top_n([8,3,2,7,4],3) == [8,7,6], 'incorrect'
    assert myModule.top_n([1,2,3,4,5],3) == [5,4,3], 'incorrect'
    assert myModule.top_n([5,4,3,2,1],3) == [5,4,3], 'incorrect'
    