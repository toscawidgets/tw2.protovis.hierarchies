"""
TODO
"""

import tw2.core as twc
import tw2.protovis.core as twp
from tw2.protovis.core import pv

class js(twc.JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)

class NodeLinkTree(twp.PVWidget):
    p_orient = twc.Param('orientation parameter', default="radial")
    p_breadth = twc.Param(default=10)
    p_depth = twc.Param(default=10)

    def prepare(self):
        self.init_js = js('var data = %s;' % self.p_data)

        self.setupRootPanel()

        tree = self.add(pv.Layout.Tree)\
            .nodes(js('pv.dom(data).root().nodes()'))\
            .depth(self.p_depth)\
            .breadth(self.p_breadth)\
            .orient(self.p_orient)

        tree.link.add(pv.Line)

        tree.node.add(pv.Dot)\
            .fillStyle(js('function(n) n.firstChild ? "#aec7e8" : "#ff7f0e"'))

        tree.label.add(pv.Label)

class CirclePackingWidget(twp.PVWidget):
    root_title = twc.Param("Root title", default="root title")


    def prepare(self):
        self.init_js = js(
            """
            var format = pv.Format.number();
            var data = %s;
            var title = "%s";
            """ % (self.p_data, self.root_title)
        )

        self.setupRootPanel()

        pack = self.add(pv.Layout.Pack)\
                .nodes(js('pv.dom(data).root(title).nodes()'))\
                .size(js('function(d) d.nodeValue'))

        pack.node.add(pv.Dot)\
                .fillStyle(js(
        'function(d) d.firstChild ? "rgba(31, 119, 180, .25)" : "#ff7f0e"'
                ))\
                .title(js(
        'function(d) d.nodeName + (d.firstChild ? "" : ": " + format(d.nodeValue))'
                ))\
                .lineWidth(1)
        pack.label.add(pv.Label)\
                .visible(js('function(d) !d.firstChild'))\
                .text(js(
        'function(d) d.nodeName.substring(0, Math.sqrt(d.nodeValue) / 20)'
                ))
