import pytest
from main import fibonacci, lucas, sum_series
def test_main_fibonacci():
    int_fib=fibonacci(10)
    assert int_fib==55,"test fail, fib() failed"

def test_main_lucas():
    int_lucas=lucas(10)
    assert int_lucas==123,"test fail, lucas() failed"

def test_main_sum_series():
    int_fib=sum_series(10,0,1)
    int_lucas=sum_series(10,2,1)
    assert int_fib==55,'test fail, sum_series() didnt handle fibonacci variation'
    assert int_lucas==123, 'test fail, sum_series() didnt handle lucas variation'





