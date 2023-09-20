import sys

def fibonacci_iter(n:int)->int:
    """
    Fibonacci Sequence ie[0,1,1,2,3,5,8...]
    input: integer n that references index n within Fibonacci Sequence.
    output: values at index n
    :param n:
    :return:
    """
    dict_fib={0:0,1:1}
    int_n=n

    if int_n<2:
        return dict_fib[int_n]

    for i in range(2,int_n+1):
        dict_fib[i]=dict_fib[i-2]+dict_fib[i-1]

    return dict_fib[int_n]


def lucas_iter(n:int)->int:
    """
    Lucas Sequence ie[2,1,3,4,7,11,18,29...]
    input: integer n that references index n within Lucas Sequence.
    output: values at index n
    :param n:
    :return:
    """
    dict_fib={0:2,1:1}
    int_n=n

    if int_n<2:
        return dict_fib[int_n]

    for i in range(2,int_n+1):
        dict_fib[i]=dict_fib[i-2]+dict_fib[i-1]

    return dict_fib[int_n]


def sum_series_iter(n:int, first=0, second=1) -> int:
    """
    constructs sum-series as follows [first,second,first+second,second+third....]
    input: integer n that references index n within sum-series
    output: values at index n
    :param n:int:
    :return int:
    """

    dict_series={0:first,1:second}
    int_n=n

    if int_n<2:
        return dict_series[int_n]

    for i in range(2,int_n+1):
        dict_series[i]=dict_series[i-2]+dict_series[i-1]

    return dict_series[int_n]



if __name__=="__main__":
    dict_sys = {int(index):int(value) for index,value in enumerate(sys.argv[1:])}
    if 0 in dict_sys:
        if 1 in dict_sys and 2 in dict_sys:
            print(sum_series_iter(dict_sys[0],dict_sys[1],dict_sys[2]))
        else:
            print(sum_series_iter(dict_sys[0]))
    else:
        print('No parameters provided. Please follow run script as follows "python main.py <number>". ')


