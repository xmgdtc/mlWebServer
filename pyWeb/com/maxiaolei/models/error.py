class Error(BaseException):
    def __int__(self,code,message):
        super(Error,BaseException(message))
        self.code=code