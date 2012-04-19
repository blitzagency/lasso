class AttributeDict(dict):
    
    def __init__(self, arg=None):
        init = super(AttributeDict, self).__init__
        
        try:
            init(arg)
        except TypeError:
            init()

    def __setattr__(self, key, value):
        dict.__setitem__(self, key, value)
    
    def __getattr__(self, key):
        return dict.__getitem__(self, key)