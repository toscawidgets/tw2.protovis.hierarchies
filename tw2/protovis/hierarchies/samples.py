""" Samples of how to use tw2.protovis.hierarchies

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import NodeLinkTree

from widgets import js
from tw2.core import JSSymbol

import math
import random
import os
def build_tree(root, depth=0):
    result = {}
    if depth > 3 or 'development-deps' in root:
        return result
    tups = os.walk(root)
    d, dirs, files = [e for e in tups][0]
    for dir in dirs:
        result[dir] = build_tree("%s/%s" % (d, dir), depth=depth+1)
    for file in files:
        result[file] = int(os.path.getsize("%s/%s" % (d, file))) + 1
    return result

class DemoNodeLinkTree(NodeLinkTree):
    p_height = 500
    p_width = 500
    p_orient = 'radial'
    p_breadth = 25
    p_depth = 60
    def prepare(self):
        self.p_data = build_tree('.')
        super(DemoNodeLinkTree, self).prepare()

