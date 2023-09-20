import sys

def fibonacci_rec(n:int, memo={0:0,1:1})->int:
    """
    Fibonacci Sequence ie[0,1,1,2,3,5,8...]
    input: integer n that references index n within Fibonacci Sequence.
    input: dictionary called memo that stores previous Fibonacci values to cut down on recursion
    output: values at index n
    :param n:
    :param memo:
    :return:
    """
    if n<2:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fibonacci_rec(n-1,memo)+fibonacci_rec(n-2,memo)
    return memo[n]

def lucas_rec(n:int, memo={0:2,1:1})->int:
    """
    Lucas Sequence ie[2,1,1,2,3,5,8...]
    input: integer n that references index n within Lucas Sequence.
    input: dictionary called memo that stores previous Lucas values to cut down on recursion
    output: values at index n
    :param n:
    :param memo:
    :return:
    """
    if n in memo:
        return memo[n]
    memo[n]=lucas_rec(n-1,memo)+lucas_rec(n-2,memo)
    return memo[n]

def sum_series_rec(n:int, memo={0:0,1:1})->int:
    """
    constructs sum-series as follows [first,second,first+second,second+third....]
    input: integer n that references index n within sum-series
    output: values at index n
    :param n:
    :param memo:
    :return:
    """
    if n in memo:
        return memo[n]
    memo[n]=sum_series_rec(n-1,memo)+sum_series_rec(n-2,memo)
    return memo[n]






if __name__=="__main__":
    dict_sys = {int(index):int(value) for index,value in enumerate(sys.argv[1:])}
    if 0 in dict_sys:
        if 1 in dict_sys and 2 in dict_sys:
            print(sum_series_rec(dict_sys[0],{0:dict_sys[1],1:dict_sys[2]}))
        else:
            print(sum_series_rec(dict_sys[0]))
    else:
        print('No parameters provided. Please follow run script as follows "python main.py <number>". ')


