#!/usr/bin/env python
'''
ssma.common.loader

This module contains the functions for loading modules.

@author: Yunzhi Zhou (Chris Chou) <yunzhi@yahoo-inc.com>
@description: 
'''

import os
import sys
import traceback

#from smartcube.util.log import get_logger
from autostats.common.log import get_logger

def load_file(filename):
    '''
    load_file(filename) -> module
    
    Loads python module with specified filename.
    '''
    dirname = os.path.dirname(filename)
    dirname = os.path.abspath(dirname)
    modulename = os.path.basename(filename)

    modulename = modulename.rsplit('.', 1)[0]

    if dirname:
        sys.path.insert(0, dirname)

    mod = None
    try:
        #print sys.path
        mod = __import__(modulename, {}, {}, [''])
        reload(mod)
    except:
        errinfo = traceback.format_exc()

        _log = get_logger('smartcube.util.load_file')
        _log.error(errinfo)

    if dirname:
        del sys.path[0]

    return mod

def load_module(modulename):
    mod = None
    try:
        mod = __import__(modulename, {}, {}, [''])
        reload(mod)
    except:
        errinfo = traceback.format_exc()

        _log = get_logger('smartcube.util.load_module')
        _log.error(errinfo)

    return mod

