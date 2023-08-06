#!/usr/bin/env python
# -*- coding:utf-8 -*- 


__version__ = '0.0.2'

from uselesss.cli import cli
from uselesss.run import run
from uselesss.src import resource_info


__all__ = [
	'__version__', 
	'cli',
	'run', 
	'resource_info',
	'gpu_info'
]