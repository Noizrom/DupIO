import sys

class DupIO(object):
    """duplicate an io to file"""
    def __init__(self ,name , mode:str = "a+" , header:str = None):
        self.file = open(name , mode)
        self.header = header
    def write(self ,data):
        self.io.write(data)
        if self.header:
            data = self.header + " : " + data
        self.file.write(data)

    def flush(self):
        self.file.flush()

class DupStdout(DupIO):
    """duplicate an stdout to file"""
    def __init__(self , name , mode:str = "a+" , header:str =None):
        self.io = sys.stdout    
        super().__init__(name , mode , header)
        sys.stdout = self
    def __del__(self):
        sys.stdout = self.io
        self.file.close()

class DupStderr(DupIO):
    """duplicate an stderr to file"""
    def __init__(self , name , mode:str = "a+" , header:str =None):
        self.io = sys.stderr   
        super().__init__(name , mode , header)
        sys.stderr= self
    def __del__(self):
        sys.stderr= self.io
        self.file.close()

if __name__=="__main__":
    # test Duplicated output
    import time
    DupStdout("rdout.txt" , "a+")
    print('Hello World')