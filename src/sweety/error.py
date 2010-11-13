#!/usr/bin/env python
'''
autostat.common.error

Defines the error classes.

@author: Yunzhi Zhou (Chris Chou) <yunzhi@yahoo-inc.com>
@description: 
'''

import exceptions

class AutoStatsError(exceptions.RuntimeError):
    pass

class AutoStatsOptionRequiredError(AutoStatsError):
    pass
