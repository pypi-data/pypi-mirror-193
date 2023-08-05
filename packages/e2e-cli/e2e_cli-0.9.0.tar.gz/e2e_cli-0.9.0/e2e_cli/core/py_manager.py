import sys

class Py_version_manager:
    def __init__(self):
        pass

    @classmethod
    def py_input(self, msg):
        if(int(sys.version[0:1])<3):
                return raw_input(msg)
        else:
                return input(msg)
        
