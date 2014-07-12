#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
目前只产生Activity列表
"""

import xml.etree.ElementTree

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

def main(manifest_path):
	tree = xml.etree.ElementTree.parse(manifest_path)
	manifest = tree.getroot()
	package = manifest.get("package")
	name_tag = ''.join((ANDROID_NS, 'name'))
	application = manifest.find('application')
	acts = application.findall('activity')
	with open('activity_list.txt', 'w') as f:
		for act in acts:
			name = act.get(name_tag, None)
			if name is None:
				print '[Warning] find name error occur'
				continue
			f.write('/'.join((package, name)))
			f.write('\n')
	print 'finish'

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print 'Usage: %s <AndroidManifest.xml>' % sys.argv[0]
		sys.exit(-1)
	main(sys.argv[1])
