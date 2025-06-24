from virtual_receiver import SaveableProtocol, SaveableMemento

class CompositeMemento:
    def __init__(self, properties: dict):
        self.prop_state = properties

    def get_state(self) -> dict:
        return self.prop_state
    
    def __str__(self):
        return self.prop_state
    

class CompositeOriginator:
    def __init__(self):
        self._originators = dict()

    # region CRUD
    def add_component(self, component: SaveableProtocol, name: str):
        self._originators[name] = component

    def get_component(self, name: str):
        return self._originators[name]
    
    def update_component(self, component: SaveableProtocol, name: str):
        if name in self._originators.keys():
            self._originators[name] = component

    def delete_component(self, name: str):
        self._originators.pop(name)
    # endregion

    def create_composite_memento(self):
        composite_state = dict()
        for name in self._originators.keys():
            composite_state[name] = self._originators[name].create_memento().get_state()
        return CompositeMemento(composite_state)

    def load_composite_memento(self, memento: CompositeMemento):
        composite_state = memento.get_state()
        for name in composite_state.keys():
            if name in self._originators.keys():
                state = composite_state[name]
                self._originators[name].load_memento(SaveableMemento(state))
