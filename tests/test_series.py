import pytest
from series_iter.series_iterative import fibonacci_iter, lucas_iter, sum_series_iter
from series_rec.series_recursive import fibonacci_rec, lucas_rec, sum_series_rec

# @pytest.mark.skip
def test_fibonacci_iter():
    int_fib=fibonacci_iter(10)
    assert int_fib==55,"test fail, fibonacci_iter() failed"

# @pytest.mark.skip
def test_lucas_iter():
    int_lucas=lucas_iter(10)
    assert int_lucas==123,"test fail, luca_iter() failed"

# @pytest.mark.skip
def test_sum_series_iter():
    int_fib=sum_series_iter(10,0,1)
    int_lucas=sum_series_iter(10,2,1)
    assert int_fib==55,'test fail, sum_series_iter() didnt handle fibonacci variation'
    assert int_lucas==123, 'test fail, sum_series_iter() didnt handle lucas variation'

# @pytest.mark.skip
def test_fibonacci_rec():
    int_fib=fibonacci_rec(100)
    assert int_fib==354224848179261915075,"test fail, fibonacci_rec() failed"

# @pytest.mark.skip
def test_lucas_rec():
    int_lucas=lucas_rec(100)
    assert int_lucas==792070839848372253127,"test fail, lucas_rec() failed"

# @pytest.mark.skip
def test_sum_series_rec():
    int_fib=sum_series_rec(100,{0:0,1:1})
    int_lucas=sum_series_rec(100,{0:2,1:1})
    assert int_fib==354224848179261915075,'test fail, sum_series_rec() didnt handle fibonacci variation'
    assert int_lucas==792070839848372253127, 'test fail, sum_series_rec() didnt handle lucas variation'





