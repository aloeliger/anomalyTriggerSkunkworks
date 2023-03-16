#!/usr/bin/env python3
import functools

def debug_function(func):
    @functools.wraps(func)
    def wrapper_debug_function(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        returnVal = func(*args, **kwargs)
        print(f'{func.__name__!r} returned: {returnVal!r}')
        return returnVal
    return wrapper_debug_function

def cache(func):
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            returnVal = func(*args,**kwargs)
            wrapper_cache.cache[cache_key] = returnVal
            return returnVal
        else:
            return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache