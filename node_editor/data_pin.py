from node_editor.pin import Pin


class DataPin(Pin):
    def __init__(self, parent, scene):
        super().__init__(parent, scene)
        self.set_execution(False)