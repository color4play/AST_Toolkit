#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    用于Android so分析寻找特定符号的导出和导入情况
    目前只处理U和T的情况，其他请自行补充
"""

import os
import subprocess

def execute(cmd_pattern, top_dirpath, symbol):
    stuff = {}
    for dirpath, dirnames, filenames in os.walk(top_dirpath):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            cmd = cmd_pattern % (
                    filepath,
                    symbol)
            p = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    shell=True)
            p.wait()
            if p.returncode == 0:
                stuff[filepath] = p.stdout.readline().strip()

    return stuff

def classify(stuff):
    result = {
        'import' : [],
        'export' : [],
    }

    for filepath, out in stuff.items():
        if out.strip().startswith('U'):
            result['import'].append(filepath)
        elif out.strip()[8:].strip().startswith('T'):
            result['export'].append(filepath)
        else:
            print 'Warning: nnnnnnnnnnn'

    return result

def main(op, top_dirpath, symbol):
    if op == 'nm':
        stuff = execute("nm -D %s | grep %s", top_dirpath, symbol)
        result = classify(stuff)

        print 'EXPORT LIB(s):'
        for filepath in result['export']:
            print '\t', filepath
        if len(result['export']) == 0:
            print '\t', 'there is no export found'
        print 'IMPORT LIB(s):'
        for filepath in result['import']:
            print '\t', filepath
        if len(result['import']) == 0:
            print '\t', 'there is no import found'
    elif op == 'strings':
        stuff = execute('strings -a %s | grep %s', top_dirpath, symbol)
        for filepath, result in stuff.items():
            print filepath, result
    else:
        print 'not support op'


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print "Usage: %s <nm|strings> <top_dirpath> <symbol>" % sys.argv[0]
        sys.exit(-1)
    main(*sys.argv[1:4])
