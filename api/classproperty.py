class classproperty:
    '''
    Class property, read only

    If Python was NodeJS, I would publish this on PyPI
    '''
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)
