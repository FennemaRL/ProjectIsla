import threading, queue
import datetime


count = []

def debounceDec(seconds):
    def _debounceFunc(function):
        q = queue.Queue(maxsize=3)
        def _debounceFunctionParams(*arg,**kwargs):
            if q.qsize() != 0:
                count.append(1)
                q.get().cancel()
            def anonimus(): 
                 function(*arg,**kwargs)
                 print("function executed after {}",len(count))
            threadCalled=threading.Timer(seconds, anonimus)
            threadCalled.start()
            q.put(threadCalled)
        return _debounceFunctionParams
    return _debounceFunc