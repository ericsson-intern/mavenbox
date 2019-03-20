#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from glob import glob
from inspect import getargspec
from subprocess import Popen, PIPE, STDOUT

# usefull to retain the proper version
# on system that have several python versions
python_exe = sys.executable


def answer(*arguments):
    proc = Popen(shell_quote(arguments), shell=True, stdout=PIPE)
    return proc.stdout.readlines()

def shell_quote(arguments):
    def quote(string):
        return "\\'".join("'" + p + "'" for p in string.split("'"))
    return " ".join(map(quote, arguments))

def system(*arguments):
    return os.system(shell_quote(arguments))

    proc = Popen(shell_quote(arguments), stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        return proc.stdout.read()
    else:
        raise RuntimeError('System command returned an error')


# ====================================================================================



def run(argument):
    proc = Popen(argument, shell=True, stdout=PIPE)
    return proc.stdout.readlines()

repo=''
url=''


command= 'git init' + repo + \
'cd' + repo + \
'git remote add origin'+ url + \
'git config core.sparsecheckout true ' \
'echo "finisht/*" >> .git/info/sparse-checkout ' \
'git pull --depth=1 origin master ' 


print(command)

# run(command)