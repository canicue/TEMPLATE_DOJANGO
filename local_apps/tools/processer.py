import functools
import threading
import multiprocessing
import time
from numpy import arange,sqrt, random, linalg
from multiprocessing import Pool

def threaded (func):
    def thread_call (*args, **kwargs):
        t = threading.Thread (target=func, args=args, kwargs=kwargs)
        t.setDaemon (True)
        t.id = id(func)
        t.start ()

    functools.update_wrapper (thread_call, func)
    return thread_call
def processed(func):
    def proc_call(*args,**kwargs):
        p=multiprocessing.Process(target=func,args=args,kwargs=kwargs)
        p.daemon=True
        p.start()
        
    functools.update_wrapper (proc_call, func)
    return proc_call
@processed
def prueba(lista):
    for i in range(1,100):
        print i
        lista.append(i)
    return lista

global counter
counter = 0
def cb(r):
    global counter
    print counter, r
    counter +=1
    
def det(M):
    return linalg.det(M)


if __name__=='__main__':
    lista=[]
    prueba(lista)
    print lista
    time.sleep(1)
    print lista
    time.sleep(10)
    print lista
    po = Pool()
    for i in xrange(1,300):
        j = random.normal(1,1,(100,100))
        po.apply_async(det,(j,),callback=cb)
        po.close()
        po.join()
        print counter
    