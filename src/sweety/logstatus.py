#!/usr/bin/env python
'''
autostats.common.logstatus

@author: Yunzhi Zhou (Chris Chou) <yunzhi@yahoo-inc.com>
@description: 
'''

import cStringIO

_content = cStringIO.StringIO()

def get_log_content():
	_content.seek(0, 0)
	return _content.read()

