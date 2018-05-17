#import importlib

from ctypes import *
from zdebug_defs import *

kernel32 = windll.kernel32

class Debugger():
    def __init__(self):
        pass
    def load(self, path_to_exe):

        # dwCreation determines how to create the process
        creation_flags = DEBUG_PROCESS

        # Initiate the Process
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x01
        startupinfo.wShowWindow = 0x00

        startupinfo.cb = sizeof(startupinfo)


        # Call CreateProcessW instead of CreateProcessA due to Unicode stuff in Python3
        if kernel32.CreateProcessW(path_to_exe,
                                    None,
                                    None,
                                    None,
                                    None,
                                    creation_flags,
                                    None,
                                    None,
                                    byref(startupinfo),
                                    byref(process_information)):
            print("[*] Process launched successfully!!!!!")
            print("[*] PID: %d" %(process_information.dwProcessId))
        else:
            print("[-] Error: 0x%08x." % (kernel32.GetLastError()))
