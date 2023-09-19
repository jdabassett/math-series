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

    * PORT: NA

    * DATABASE_URL: NA

    * RUN: 'python main.py'

TESTS:

    * INSTRUCTIONS: For functionality, run these commands in the terminal...

```bash
python3 main.py 100     #the fibonacci number at index 100 will be returned
#354224848179261915075
python3 main.py 100 0 1 #return value from index 100, only 0 and 1 will be used to create the fibonacci sequence
#354224848179261915075
python3 main.py 100 2 1 #return value from index 100, only 2 and 1 will be used to create the lucas sequence
#792070839848372253127
```

PRODUCTION NOTES:

    * Testing: To test, run these tests with pytest installed

```bash
py.test 
================================================= test session starts =================================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: ../math-series
collected 3 items

test_main.py ...                                                                                                [100%]

================================================== 3 passed in 0.00s ==================================================

```