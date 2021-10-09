

from rx import operators as op
from rx.subject import Subject
from rx.scheduler import ThreadPoolScheduler

t_pool = ThreadPoolScheduler(2)

def debounceDec(seconds):
    def _debounceFunc(function):
        obs = Subject()
        def wrapper(arg):
            function(*arg[0],**arg[1])
            t_pool.executor.shutdown()
        obs.pipe(op.debounce(seconds, t_pool)).subscribe(wrapper,scheduler=t_pool)
        def _debounceFunctionParams(*arg,**kwargs):
            obs.on_next((arg,kwargs))
        return _debounceFunctionParams
    return _debounceFunc
