#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
计算内存地址
"""

def main(ava, aoff, ooff):
	base = ava-aoff
	print 'result', '%#010x' % (base+ooff)
	
if __name__ == '__main__':

	va = raw_input('VA: ')
	off = raw_input('OFF: ')
	calc_off = raw_input('CALC_OFF: ')
	
	main(*map(lambda x: int(x, 16), [va, off, calc_off]))
