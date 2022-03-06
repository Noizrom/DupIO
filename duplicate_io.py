'''
duplicates stdout or stderr to a file
'''


import sys

class DupIO():
    """duplicate an io to file"""
    _io = None
    def __init__(self ,name , mode:str = "a+" , header:str = None):
        self.file = open(name , mode , encoding='utf-8')
        self.header = header


    def write(self ,data):
        '''generally write into file'''
        self._io.write(data)
        if self.header:
            data = self.header + " : " + data
        self.file.write(data)


    def flush(self):
        '''i dunno. flush'''
        self.file.flush()


class Forkstdout(DupIO):
    """duplicate an stdout to file"""
    def __init__(self , name , mode:str = "a+" , header:str =None):
        self._io = sys.stdout
        super().__init__(name , mode , header)
        sys.stdout = self


    def __del__(self):
        sys.stdout = self._io
        self.file.close()


class Forkstderr(DupIO):
    """duplicate an stderr to file"""
    def __init__(self , name , mode:str = "a+" , header:str =None):
        self.io = sys.stderr
        super().__init__(name , mode , header)
        sys.stderr= self
        

    def __del__(self):
        sys.stderr= self.io
        self.file.close()


if __name__=="__main__":
    Forkstdout("rdout.txt" , "a+")
    print('Hello World')
    
    
