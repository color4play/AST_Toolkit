#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
一般activity_list由gen_component_list.py产生
"""

import os

def main(args_file):
	with open(args_file, 'r') as f:
		for arg in f:
			os.system('adb shell su -c "am start -n %s"' % arg)
			os.system("pause")
			
	
if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print 'Usage: %s <activity_list>' % sys.argv[0]
		sys.exit(-1)
	main(sys.argv[1])
