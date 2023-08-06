from __future__ import annotations
from typing import List
import abc
import queue

class DirectedGraphContext:
    def __init__(self) -> None:
        self.heads = []

"""
    Move this into a new hatchling project...
    Create a higher level interface using adj matrix or list
    one matrix for connected components, another matrix for transitions?
    set active state node -> on transition, can apply decorator to register function to call for transition(s)
    pathing can determine all transitions necessary to reach a certain state

"""
class DirectedGraphNode:
    def __init__(self, id: str, **kwargs) -> None:
        super().__init__()
        self._in_connections: List[Connection] = []
        self._out_connections: List[Connection] = []
        self._id = id
        self.kwargs=kwargs
            
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def out_degree(self):
        return len(self._out_connections)
    
    @property
    def in_degree(self):
        return len(self._in_connections)
    
    def stream_output_nodes(self):
        """Nodes which this node has an output connection to"""
        for output_connection in self._out_connections:
            yield output_connection.dst

    def stream_input_nodes(self):
        """Nodes which this node has an input connection to"""
        for input_connection in self._in_connections:
            yield input_connection.dst

    def count(self):
        """Return the count of nodes reachable by this node+1 (self)"""
        count = 0
        lo_queue: List[DirectedGraphNode] = []
        visited = []
        lo_queue.append(self)
        while lo_queue:
            node = lo_queue.pop(0) # behave like a FIFO queue
            count += 1
            visited.append(node)
            for n in node.stream_output_nodes():
                if n not in visited and n not in lo_queue:
                    lo_queue.append(n)
        return count


    def connect_to(self, dst: DirectedGraphNode):
        connection_id = self.id + '_' + dst.id
        connection = Connection(connection_id, self, dst)
        self._out_connections.append(connection)
        dst.accept_input_connection(connection)

    def accept_input_connection(self, connection: Connection):
        # match id
        for c in self._in_connections:
            if c.id == connection.id:
                raise KeyError("Connection with id[%s] already exist" % connection.id)
        # match obj
        if connection not in self._in_connections:
            self._in_connections.append(connection)

    def accept_output_connection(self, connection: Connection):
        # match id
        for c in self._out_connections:
            if c.id == connection.id:
                raise KeyError("Connection with id[%s] already exist" % connection.id)
        # match obj
        if connection not in self._out_connections:
            self._out_connections.append(connection)

    def get_all_paths(self, id: str) -> list[Path]:
        pass

    def has_path(self, id: str) -> bool:
        """
        Returns true if _at least one path exist_ from this node to another node with matching id
        """
        if id == self._id: return True # trivial path
        visited = [self]
        lo_queue = queue.Queue[DirectedGraphNode]()
        for node in self.stream_output_nodes():
            lo_queue.put(node)
        while not lo_queue.empty():
            current_node = lo_queue.get()
            if current_node.id == id:
                return True
            else:
                visited.append(current_node)
                for node in current_node.stream_output_nodes():
                    if node not in visited:
                        lo_queue.put(node)
        return False

    def print_adjacency_list(self) -> None:
        """This is just for development fun - remove me :)"""
        visited = []
        lo_queue: List[DirectedGraphNode] = []
        lo_queue.append(self)
        print("\n------- Adj List --------")
        while lo_queue:
            node = lo_queue.pop(0) # behave like a FIFO queue :)
            print(node.id, end=" ")
            visited.append(node)
            for n in node.stream_output_nodes():
                print("-> %s" % n.id, end=" ")
                if n not in visited and n not in lo_queue:
                    lo_queue.append(n)
            print("")
        print("-------------------------")

    def print_edge_array(self) -> None:
        """This is just for development fun - remove me :)"""
        
        visited = []
        lo_queue: List[DirectedGraphNode] = []
        lo_queue.append(self)
        print("\n------- Edge List --------")
        while lo_queue:
            node = lo_queue.pop(0) # behave like a FIFO queue :)
            print(node.id, end=" ")
            visited.append(node)
            for n in node.stream_output_nodes():
                print("-> %s" % n.id, end=" ")
                if n not in visited and n not in lo_queue:
                    lo_queue.append(n)
            print("")
        print("-------------------------")

class Path:
    def __init__(self) -> None:
        pass

class Connection:
    def __init__(self, id, src, dst) -> None:
        super().__init__()
        self._src = src
        self._dst = dst
        self._id = id
    
    @property
    def id(self) -> str:
        return self._id

    @property
    def dst(self) -> DirectedGraphNode:
        return self._dst

    @dst.setter
    def dst(self, dst: DirectedGraphNode) -> None:
        self._dst = dst

    @property
    def src(self) -> DirectedGraphNode:
        return self._src

    @src.setter
    def src(self, src: DirectedGraphNode):
        self._src = src

class TransitionMixin:
    def __init__(self, src: DirectedGraphNode, dst: DirectedGraphNode) -> None:
        self.src = src
        self.src = dst

    @abc.abstractmethod
    def transition(self, **kwargs):
        raise NotImplementedError

def connect_nodes(src: DirectedGraphNode, dst: DirectedGraphNode, conn: Connection):
    src.accept_output_connection(conn)
    dst.accept_input_connection(conn)
    conn.src = src
    conn.dst = dst