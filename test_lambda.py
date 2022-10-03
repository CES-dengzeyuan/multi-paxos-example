from __future__ import print_function

from twisted.internet import reactor
from twisted.internet import task


def loop():
    task.LoopingCall(lambda: print("Hello World")).start(1)


reactor.callWhenRunning(loop)
reactor.run()
