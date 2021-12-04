# -*- coding: utf-8 -*-

# Converts from the source markup format to HTML for the web version.

from shutil import copy

with open("source/index.md", 'r') as ff:
	with open("docs/index.md", 'w') as ft:
		ft.write(ff.read())
