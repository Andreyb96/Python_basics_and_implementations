class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x>0:
            self = super(PositiveList, self).append(x) 
        else:
            raise NonPositiveError()