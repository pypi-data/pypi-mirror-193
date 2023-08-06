from graph import DirectedGraphNode, TransitionMixin, Connection

class StateContext:
    def __init__(self) -> None:
        self.current_state = None

class StateNode(DirectedGraphNode):
    def __init__(self, id: str, **kwargs) -> None:
        super().__init__(id, **kwargs)

class StateTransition(TransitionMixin, Connection):
    def __init__(self, id: str, func) -> None:
        super().__init__(id)
        self.func = func

    def transition(self):
        self.func()()
    
class UnknownState(StateNode):
    def __init__(self, id: str) -> None:
        super().__init__(id, None, None)