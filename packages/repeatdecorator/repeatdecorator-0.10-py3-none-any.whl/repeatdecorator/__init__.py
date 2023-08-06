from functools import wraps
from typing import Any, Union

from kthread_sleep import sleep
import sys
from collections import deque
import threading

repeatdec_vars = sys.modules[__name__]
repeatdec_vars.active = lambda: threading.active_count()
repeatdec_vars.lock = threading.RLock()


def repeat_func(
    f_py: Any = None,
    repeat_time: Union[float, int] = 1.0,
    variablename: str = "threadresults",
    activate_lock: bool = False,
    ignore_exceptions: bool = False,
    exception_value: Any = None,
    max_len_allresults: Union[int, None] = None,
    print_results: bool = True,
    print_exceptions: bool = True,
    execution_limit: int = -1,
    max_concurrent_threads: int = -1,
    check_max_threads_every_n_seconds: Union[float, int] = 0.015,
) -> Any:
    """Summary of repeat_func.

    Args:
        f_py (Any)
            Description Don't use - reserved for the function
            Default     None
        repeat_time (Union[float,int])
            Description Execute each n seconds
            Default     1.0
        variablename (str)
            Description Creates a dict for the results in repeatdec_vars - Use repeatdecorator.repeatdec_vars.variablename to access it
            Default     "threadresults"
        activate_lock (bool)
            Description Threading Rlock
            Default     False
        ignore_exceptions (bool)
            Description Continue on Exceptions?
            Default     False
        exception_value (Any)
            Description Ignored if  ignore_exceptions is False
            Default     None
        max_len_allresults (Union[int,None])
            Description If None, results are stored in a list (no limit), if int, a deque is used to store
                        the results. Results can be found here: repeatdecorator.repeatdec_vars.variablename["results"]
                        Make sure to save the results before calling the function again.
            Default     None
        print_results (bool)
            Description Print the return value from each function?
            Default     True
        print_exceptions (bool)
            Description Print Exceptions
            Default     True
        execution_limit (int)
            Description Stop timer after n executions / -1 = No limit
            Default     -1
        max_concurrent_threads (int)
            Description Thread limit  / -1 = No limit
            Default     -1
        check_max_threads_every_n_seconds (Union[float,int])
            Description Sleep time before checking the current number of threads again.
            Default     0.015

    Returns:
        Any: Description of return value
    """

    assert callable(f_py) or f_py is None
    setattr(repeatdec_vars, variablename, {})

    if max_len_allresults:
        getattr(repeatdec_vars, variablename)["results"] = deque([], max_len_allresults)

    else:
        getattr(repeatdec_vars, variablename)["results"] = []
    getattr(repeatdec_vars, variablename)["enabled"] = True
    getattr(repeatdec_vars, variablename)["total_count"] = 0

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if getattr(repeatdec_vars, variablename)["enabled"]:
                if (
                    execution_limit == -1
                    or execution_limit
                    > getattr(repeatdec_vars, variablename)["total_count"]
                ):
                    while True:
                        if (
                            repeatdec_vars.active() < max_concurrent_threads
                            or max_concurrent_threads == -1
                        ):
                            t = threading.Timer(repeat_time, wrapper, args, kwargs)
                            t.start()
                            getattr(repeatdec_vars, variablename)["total_count"] += 1

                            break
                        else:
                            if not getattr(repeatdec_vars, variablename)["enabled"]:
                                return
                            sleep(check_max_threads_every_n_seconds)
            try:
                if activate_lock:
                    with repeatdec_vars.lock:

                        fures = func(*args, **kwargs)
                else:
                    fures = func(*args, **kwargs)

                getattr(repeatdec_vars, variablename)["results"].append(fures)
                if print_results:
                    print(fures)
            except Exception as fe:
                if print_exceptions:
                    print(fe)
                if ignore_exceptions:
                    getattr(repeatdec_vars, variablename)["results"].append(
                        exception_value
                    )
                else:
                    raise fe

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
