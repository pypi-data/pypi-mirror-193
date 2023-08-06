

from fermi_graph.graph import Connection, DirectedGraphNode, connect_nodes


def test_has_path():
    gn1 = DirectedGraphNode(id="1")
    gn2 = DirectedGraphNode(id="2")
    con = Connection(id="test_conn", src=None, dst=None)
    connect_nodes(gn1, gn2, con)
    assert(gn1.has_path(gn2.id))
    assert(not gn2.has_path(gn1.id))

def test_connect_to():
    gn1 = DirectedGraphNode(id="1")
    gn2 = DirectedGraphNode(id="2")
    gn1.connect_to(gn2)
    assert(gn1.has_path(gn2.id))
    assert(not gn2.has_path(gn1.id))

def test_print_adj_list():
    gn1 = DirectedGraphNode(id="1")
    gn2 = DirectedGraphNode(id="2")
    gn3 = DirectedGraphNode(id="3")
    gn4 = DirectedGraphNode(id="4")
    gn1.connect_to(gn2)
    gn1.connect_to(gn3)
    gn2.connect_to(gn4)
    gn3.connect_to(gn2)
    gn3.connect_to(gn4)
    gn1.print_adjacency_list()
    assert(gn1.count() == 4)

def test_print_edge_matrix():
    gn1 = DirectedGraphNode(id="1")
    gn2 = DirectedGraphNode(id="2")
    gn3 = DirectedGraphNode(id="3")
    gn4 = DirectedGraphNode(id="4")
    gn1.connect_to(gn2)
    gn1.connect_to(gn3)
    gn2.connect_to(gn4)
    gn3.connect_to(gn4)
    gn3.connect_to(gn2)
    gn1.print_adjacency_list()
    assert(gn1.count() == 4)