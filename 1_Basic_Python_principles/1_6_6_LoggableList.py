class LoggableList(Loggable, list):
    def append(self,x):
        super(LoggableList,self).append(x)
        self.log(x)