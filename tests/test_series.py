import pytest
from series_iter.series_iterative import fibonacci_iter, lucas_iter, sum_series_iter
def test_fibonacci_iter():
    int_fib=fibonacci_iter(10)
    assert int_fib==55,"test fail, fib() failed"

def test_lucas_iter():
    int_lucas=lucas_iter(10)
    assert int_lucas==123,"test fail, lucas() failed"

def test_sum_series_iter():
    int_fib=sum_series_iter(10,0,1)
    int_lucas=sum_series_iter(10,2,1)
    assert int_fib==55,'test fail, sum_series() didnt handle fibonacci variation'
    assert int_lucas==123, 'test fail, sum_series() didnt handle lucas variation'





