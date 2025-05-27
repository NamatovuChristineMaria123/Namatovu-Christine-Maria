#Two parent classes define a method named send()
#Python uses Method Resolution Order (MRO) to determine which method to run.
class Logger:
    def send(self):
        print("Sending log data...") # Will be called because it's the first in the inheritance list.

class Notifier:
    def send(self):
        print("Sending user notification...")

class SmartSecuritySystem(Logger, Notifier):
    pass


system = SmartSecuritySystem()
system.send()



