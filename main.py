import sys

def fibonacci(n:int)->int:
    """
    accepts n(integer) and returns nth index in Fibonacci Sequence ie[0,1,1,2,3,5,8...]
    accomplishes this through interation
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

# def rec_fib(n:int, memo: dict[int]={})->int:
#     """
#     accepts n(integer) and returns nth index in Fibonacci Sequence ie[0,1,1,2,3,5,8...]
#     accomplishes this through recursion
#     :param n:
#     :return:
#     """
#     if n<2:
#         return n
#     if n in memo:
#         return memo[n]
#     memo[n]=rec_fib(n-1,memo)+rec_fib(n-2,memo)
#     return memo[n]

def lucas(n:int)->int:
    """
    accepts n(integer) and returns nth index in Lucas Sequence ie[2,1,3,4,7,11,18,29...]
    accomplishes this through interation
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

# def rec_lucas(n:int, memo: dict[int]={2,1})->int:
#     """
#     accepts n(integer) and returns nth index in Lucas Sequence ie[2,1,3,4,7,11,18....]
#     accomplishes this through recursion
#     :param n:
#     :return:
#     """
#     if n in memo:
#         return memo[n]
#     memo[n]=rec_fib(n-1,memo)+rec_fib(n-2,memo)
#     return memo[n]


def sum_series(n:int, first=0, second=1) -> int:
    """
    requires index to return.
    optional first and second values for a series that will be summed up to index n
    ie...[first,second,first+second,second+third....]
    accomplishes this through iteration.
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
            print(sum_series(dict_sys[0],dict_sys[1],dict_sys[2]))
        else:
            print(sum_series(dict_sys[0]))
    else:
        print('No parameters provided. Please follow run script as follows "python main.py <number>". ')


