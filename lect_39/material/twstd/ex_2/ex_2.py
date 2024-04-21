"""Простий приклад гарного виконання довільно довгих обчислень у Twisted.

Це також проста демонстрація twisted.protocols.basic.LineReceiver.
"""

from twisted.protocols import basic
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory

class LongMultiplicationProtocol(basic.LineReceiver):
    """Протокол для довгого множення.

    Він отримує список чисел (відокремлених пробілами) у рядку та
    записує відповідь. Відповідь обчислюється частинами, тому
    обчислення має блокуватися достатньо довго, щоб мати значення.
    """
    def connectionMade(self):
        self.workQueue = []

    def lineReceived(self, line):
        try:
            numbers = [int(num) for num in line.split()]
        except ValueError:
            self.sendLine(b'Error.')
            return

        if len(numbers) <= 1:
            self.sendLine(b'Error.')
            return

        self.workQueue.append(numbers)
        reactor.callLater(0, self.calcChunk)

    def calcChunk(self):
        # Переконайтеся, що залишилося трохи роботи; коли отримано кілька рядків
        # під час обробки кілька викликів reactor.callLater()
        # може статися між викликами calcChunk().
        if self.workQueue:
            # Отримайте першу частину роботи з черги
            work = self.workQueue[0]

            # Виконайте частину роботи: [a, b, c, ...] -> [a*b, c, ...]
            work[:2] = [work[0] * work[1]]

            # Якщо ця робота зараз має лише один елемент, надішліть його.
            if len(work) == 1:
                self.sendLine(str(work[0]).encode("ascii"))
                del self.workQueue[0]

            # Заплануйте цю функцію для виконання додаткової роботи, якщо ще є робота
            # має бути зроблено.
            if self.workQueue:
                reactor.callLater(0, self.calcChunk)


class LongMultiplicationFactory(ServerFactory):
    protocol = LongMultiplicationProtocol


if __name__ == '__main__':
    from twisted.python import log
    import sys
    log.startLogging(sys.stdout)
    reactor.listenTCP(1234, LongMultiplicationFactory())
    reactor.run()
