from implementations.tips import total_with_tips

def test_100_20 () :
    assert total_with_tips(100,20) == 120

def test_100_notip () :
    assert total_with_tips(100,0) == 100

def test_cheap_bill () :
    assert total_with_tips(1,20) == 5

def test_expensive_bill () :
    assert total_with_tips(5000,15) == 5500

def test_cents () : 
    assert total_with_tips(10,33.3333) == 13.33