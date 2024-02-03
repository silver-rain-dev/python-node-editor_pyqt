from node_editor.pin import Pin


class DataPin(Pin):
    def __init__(self, parent, scene):
        super().__init__(parent, scene)
        self.set_execution(False)
        self._data = None

    @property
    def data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data