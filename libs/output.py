import sys
import ctypes
import platform

def windows_out(color, msg):
    STD_OUTPUT_HANDLE = -11
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)
    print msg
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 0x0c|0x0a|0x09)

def good(msg):
    if "windows" not in platform.platform():
        print "[+]\033[01;32m"+msg+"\033[0m"
    else:
        windows_out(0x0a, "[+] %s" % msg)