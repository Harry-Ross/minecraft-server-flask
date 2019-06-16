import subprocess
import os

from app import app

lines = []

running = False

def runServer():
    global running
    if not running:
        running = True
        process = subprocess.Popen(['java', '-Xmx1024M', '-Xms1024M', '-jar', 'server.jar'], stdout=subprocess.PIPE)
        global lines
        while True:
            output = process.stdout.readline()
            lines.append(process.stdout.readline())
            if output == '' and output.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
        return rc
    else:
        return "already running"

def getLines():
    global lines
    return lines

def server_command(cmd):
    process.stdin.write(cmd+"\n")

process = None