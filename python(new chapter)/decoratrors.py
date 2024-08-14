import functools,time
def my_deco(func):
    @functools.wraps(func) 
    def waraper_my_deco(*args,**kwargs):
        '''doc string must be writen if you want to be shown in help;'''
        print('before')
        return func(*args,**kwargs)
    return waraper_my_deco

def slowly(func):
    '''this is a decorator to slow the prosses down'''
    @functools.wraps(func)
    def wrapper_slowly(*args,**kwargs):
        time.sleep(2)
        func(*args,**kwargs)
    return wrapper_slowly

def slow_down(func):
    '''this is a decorator to slow the prosses down'''
    @functools.wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        for i in range(5,0,-1):
            print(f'{i} seccod remaining')
            time.sleep(1)
        func(*args,**kwargs)
    return wrapper_slow_down

def debug(func):
    '''this is a decorator to debug the code'''
    @functools.wraps(func)
    def wrapper_debug(*args,**kwargs):
        arg=[repr(a) for a in args]
        dic=[f'{b!r}={c!r}' for b,c in kwargs.items()]
        end=arg+dic
        print(f"calling {func.__name__!r}({' , '.join(end)})")
        p=func(*args,**kwargs)
        print (f"{func.__name__!r} returned {p}")
        return p
    return wrapper_debug

def timer(func):
    '''calculating wate of the time'''
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        o=(time.perf_counter())
        u=func(*args,**kwargs)
        o1=(time.perf_counter())
        o1-=o
        print(f'finished in : {o1 : 0.5f}')
        return u
    return wrapper_timer