class myclass(object):
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def login(self):
        #authentication
        print "authenticating"
        return self._password
    def _validate(self):
        pass

o = myclass('python', 'class')
print o.username
print o._password
print o._validate
