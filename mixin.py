class NumberQueue(object):
    def __init__(self):
        self.q = list()

    def put(self, value):
        print "----"
        self.q.append(value)

    def printSelf(self):
        print repr(self.q)


class DoublingMixin(object):

    def put(self, value):
        print "===="
        super(DoublingMixin, self).put(value * 2)


class IncrementingMixin(object):

    def put(self, value):
        print "++++"
        super(IncrementingMixin, self).put(value + 1)


# In Python, calls to 'super' go left-to-right through peer super classes

class Doubler(DoublingMixin, NumberQueue):
    pass


class DoublerIncrementer(DoublingMixin, IncrementingMixin, NumberQueue):
    pass


class IncrementerDoubler(IncrementingMixin, DoublingMixin, NumberQueue):
    pass


def show(kind, q):
    q.put(2)
    q.put(3)
    q.put(4)
    print kind,
    q.printSelf()


show('Original:          ', NumberQueue())
show('Doubler:           ', Doubler())
show('DoublerIncrementer:', DoublerIncrementer())
show('IncrementerDoubler:', IncrementerDoubler())
