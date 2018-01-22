#coding:utf8

import functools
import time
import inspect
import datetime
'''
def m_cache(duration):
    def _cache(fn):
        local_cache = {}
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            ##清除过期缓存
            def expire_key(cache):
                expire_keys = []
                for k,(_,timestamp) in cache.items():
                    if datetime.datetime.now().timestamp() - timestamp > duration:
                       expire_keys.append(k)
                for k in expire_keys:
                    cache.pop(k)
            expire_key(local_cache)
            ##生成key
            def make_key():
                key_dict = {}
                sig = inspect.signature(fn)
                params = sig.parameters  #有序字典

                param_list = list(params.keys())
                #位置参数
                for i,v in enumerate(args):
                    k = param_list[i]
                    key_dict[k] = v

                #关键字参数
                #for k,v in kwargs.items():
                #    key_dict[k] = v
                key_dict.update(kwargs)

                #缺省值处理
                for k in params.keys():
                    if k not in key_dict.keys():
                        key_dict[k] = params[k].default

                return tuple(sorted(key_dict.items()))
            key = make_key()

            if key not in local_cache.keys():
                ret = fn(*args,**kwargs)
                local_cache[key] = (ret,datetime.datetime.now().timestamp())

            return key,local_cache[key]
        return wrapper
    return _cache

def logger(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('function run time is {}'.format(delta))
        return ret
    return wrapper


@logger
@m_cache(6)
def add(x,y=5):
    time.sleep(3)
    ret = x + y
add(4)
add(4,5)
add(x=4,y=5)

time.sleep(6)
add(4)
add(4,5)
add(x=4,y=5)
'''













