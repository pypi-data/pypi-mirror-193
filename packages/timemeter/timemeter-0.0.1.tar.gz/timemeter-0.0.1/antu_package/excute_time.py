import time


def exc_time(fun: callable) -> callable:
    """
    Measures the execution time of a function object.

    -----
    ### Parameters:
    -----
    fun: callable
        Wrapping function.

    -----
    ### Returns:
    -----
    function: callable
        The wrapper function.

    ----
    ### Examples
    ----
    ```
    from functools import reduce

    @exc_time
    def expo(*args):
        result = reduce(lambda acum, item: acum * item, args)
        return result

    print(expo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    # OUTPUT --> (0.002000093460083008, 3628800)
    ```
    """

    def wrapper(*args: tuple, **kwargs: dict) -> tuple:
        """
        This is a wrapper function

        -----
        ### Parameters:
        -----
        *args
            Arguments of function.
        **kwargs
            Keyword arguments of function.

        -----
        ### Returns:
        -----
        A tuple with the following format (time, result).
        * The "time" is the time it took for the function to execute.
        * The "result" is the result of function.W
        """

        start = time.time()
        fun(*args, **kwargs)
        end = time.time()

        return end - start, fun(*args, **kwargs)

    return wrapper
