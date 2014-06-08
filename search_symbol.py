#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
    用于Android so分析寻找特定符号的导出和导入情况
    目前只处理U和T的情况，其他请自行补充
"""

import os
import subprocess

def nm(top_dirpath, symbol):
    stuff = {}
    for dirpath, dirnames, filenames in os.walk(top_dirpath):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            cmd = "nm -D %s | grep %s" % (
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

def main(top_dirpath, symbol):
    stuff = nm(top_dirpath, symbol)
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


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print "Usage: %s <top_dirpath> <symbol>" % sys.argv[0]
        sys.exit(-1)
    main(*sys.argv[1:3])
