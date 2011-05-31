""" Samples of how to use tw2.protovis.hierarchies

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import NodeLinkTree, CirclePackingWidget

from widgets import js
from tw2.core import JSSymbol

import math
import random
import os

tw2core_location = "/".join(
    __import__('tw2.core', fromlist=['core']).__file__.split('/')[:-1])

def build_tree(root=tw2core_location, depth=0):
    result = {}
    if depth > 3:
        return result
    tups = os.walk(root)
    d, dirs, files = [e for e in tups][0]
    for dir in dirs:
        result[dir] = build_tree("%s/%s" % (d, dir), depth=depth+1)
    for file in files:
        if file.endswith('.pyc') or file.endswith('.pyo'):
            continue
        result[file] = int(os.path.getsize("%s/%s" % (d, file))) + 1
    return result

class DemoNodeLinkTree(NodeLinkTree):
    p_height = 500
    p_width = 500
    p_orient = 'radial'
    p_breadth = 29 
    p_depth = 100
    def prepare(self):
        self.p_data = build_tree() # of tw2.core
        super(DemoNodeLinkTree, self).prepare()

class DemoCirclePackingWidget(CirclePackingWidget):
    p_height = 500
    p_width = 500
    root_title = "filesizes in tw2.core"
    p_data = build_tree() # Builds a tree of the filesizes of tw2.core

