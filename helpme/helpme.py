class Greetings(object):
    def hello(self):
        print self.greeting
        return
    def __init__(self, greeting):
        self.greeting = greeting

    def is_greeting(self):
        if len(self.greeting) > 1:
		return True
	else:
		return False
