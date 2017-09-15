#!/usr/bin/env python3

import os, sys
from glob import glob

template_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Trackula</title>
	<meta charset="utf-8">
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="shower/themes/ribbon/styles/screen-16x10.css">
</head>
<body class="shower full">
	<header class="caption">
            <h1>Trackula</h1>
            <p>Santiago Saavedra</p>
            <p>Sofia Prosper</p>
	</header>
        SECTIONS
	<!--
		To hide progress bar from entire presentation
		just remove “progress” element.
	<div class="progress"></div>
	-->
	<script src="shower/shower.min.js"></script>
	<!-- Copyright © 2016 Sofia Prosper Diaz-Morz. -->
	<!-- Copyright © 2016 Santiago Saavedra López. -->
</body>
</html>
"""

section = """
<section class="slide white">
    <img src="SOURCE" alt="" class="cover">
</section>
"""

def get_template(images):
    sections = list(map(get_section, images))
    return template_doc.replace('SECTIONS', "\n".join(sections))


def get_section(path):
    return section.replace("SOURCE", path)

import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def main():
    img_directory = 'images'
    images = natural_sort(glob('%s/*.*' % img_directory))
    print(get_template(images))

if __name__ == '__main__':
    main()




