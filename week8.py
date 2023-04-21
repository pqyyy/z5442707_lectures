# You should not import any other module
import datetime as dt


def time_it(func, parms):
    """ Returns the number of microseconds it took to execute a function.

    Parameters
    ----------
    func : any function

    parms : dict
        A dictionary with the parameters that will be passed to the function.
        For instance, if `parms` is {'parm1': 1}, then the function call will be
        `func(parm1=1)`

    Returns
    -------
    int
        The number of microseconds it took to execute `func` with the parameters `parms`.

    Example
    -------

    Suppose there is a function called `my_func` that takes a single parameter called `parm1`.

        >> res = time_it(my_func, {'parm1': 3})
        >> print(res)
        >> 8010000

    In the example above, we are assuming it took 8010000 microseconds to execute
    the function `my_func(parm1=3)`.

    Note
    ----
    - You should not use the `time` module inside this function
      (meaning, do not use `import time` inside this function)

    """
    # <COMPLETE THIS PART>


    start = dt.datetime.now()
    func(**parms)
    end = dt.datetime.now()
    elapsed = end - start
    secs = elapsed.total_seconds()
    microsecs = int(secs*1000000)
    return microsecs

def _test_time_it():
    """ This function uses the time.sleep to test the function time_it.
    The output of this function should be:

        It took about 5000000 microseconds to execute this function.

    NOTE
    ----
    - The number of microsecs in the output will almost certainly be different
      when you run this function due to server latency.

    """
    import time

    def _my_func(secs):
        time.sleep(secs)

    res = time_it(_my_func, {'secs': 5})
    print(f"It took about {res} microseconds to execute this function.")


if __name__ == "__main__":
    pass
    _test_time_it()
