LAB:

    * Class02

PROJECT: 
    
    * Math Series

AUTHOR: 

    * Jacob Bassett

LINKS:

    * NA

SETUP:

    * REQUIREMENTS: 
        iniconfig==2.0.0
        packaging==23.1
        pluggy==1.3.0
        pytest==7.4.2

    * PORT: NA

    * DATABASE_URL: NA

    * RUN: Can run the following terminal commands to utilize these functions.

```bash
python3 series_iter/series_iterative.py 100     #the fibonacci number at index 100 will be returned
#354224848179261915075
python3 series_rec/series_iterative.py 100 0 1 #return value from index 100, only 0 and 1 will be used to create the fibonacci sequence
#354224848179261915075
python3 series_iter/series_iterative.py 100 2 1 #return value from index 100, only 2 and 1 will be used to create the lucas sequence
#792070839848372253127

# can also run these same commands to the series_rec/series_recursive.py module and get the same answers
```

TESTS:

    * INSTRUCTIONS: Can run the following commands...

```bash
# to run all tests
py.test 
================================================================ test session starts =================================================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: ../math-series
collected 6 items

tests/test_series.py ......                                                                                                                    [100%]

================================================================= 6 passed in 0.01s ==================================================================
# to test just the recursive functions
pytest -k rec
================================================================ test session starts =================================================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: ../math-series
collected 6 items / 3 deselected / 3 selected

tests/test_series.py ...                                                                                                                       [100%]

========================================================== 3 passed, 3 deselected in 0.01s ===========================================================

# to test just the iterative functions
pytest -k iter
================================================================ test session starts =================================================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: ../math-series
collected 6 items / 3 deselected / 3 selected

tests/test_series.py ...                                                                                                                       [100%]

========================================================== 3 passed, 3 deselected in 0.01s ===========================================================
```


PRODUCTION NOTES:

    * NA
