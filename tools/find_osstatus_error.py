#!/usr/bin/env python2.7
# requires Python 2.7 for subprocess.check_output

import subprocess as sp
import os

def find_osstatus_err(err):
    SDKROOT = sp.check_output(["xcode-select", "--print-path"]).decode("utf-8").rstrip()
    SDKROOT += "/Platforms/iPhoneOS.platform/Developer/SDKs" 

    error = ""
    if err.isdigit():
        code = int(err)
        if code > 0:
            error = ""
            while(code > 0):
                c = code & 0xff
                error = "%c" % c + error
                code >>= 8
        error = "'" + error + "'"
    else:
        error = err
    results = []
    for (dirname, subdirs, files) in os.walk(SDKROOT):
        for f in files:
            if f.endswith(".h"):
                path = os.path.join(dirname, f)
                file = open(path)
                lino = 0
                for l in file:
                    lino += 1
                    if error in l:
                        results.append((path, f, lino, " ".join(l.split())))

    if len(results) > 0:
        return results
    return (("Not Found: " + err, ), )
        
import sys
def print_usage():
    name = sys.argv[0]
    print("Find mysterious OSStatus code")
    print("Usage: " + name + " code")
    print("eg:    " + name + " 1718449215")
    print("       " + name + " \"fmt?\"")

if '__main__' == __name__:
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)
    r = find_osstatus_err(sys.argv[1])
    for l in r:
        if len(l) > 1:
            print(str(l[1]) + "(" + str(l[2]) + ")" + ": " + str(l[3]))
        else:
            print(str(l[0]))


