
'''
Configuration
'''


import config_default

class Dict(dict):
    '''Simple dict but support access as x.y style.'''

    def __init__(self, names=(), values=(), **kw):
        '''
        New Dict initilized with names-values pair
        :param names:
        :param values:
        :param kw:
        '''
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):
    '''
    Merge two dicts into one dict.
    The value in the `defaults` would be overridden by the value for the same key in the `override` dict.
    :param defaults: default dict
    :param override: dict for override
    :return:
    '''
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    '''Tranform dict to Dict which has accessor for each key-value pair.'''
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D


# ====================================
#              读取配置
# ====================================

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)