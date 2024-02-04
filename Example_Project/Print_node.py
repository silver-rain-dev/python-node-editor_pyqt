from node_editor.node import Node


class Print_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Print"
        self.type_text = "Debug Nodes"
        self.set_color(title_color=(160, 32, 240))

        self.add_pin(name="Ex In", is_output=False, execution=True)

        self.input_pin = self.add_pin(name="input", is_output=False)
        self.build()

    def execute_inputs(self):
        self.input_pin.set_data(self.input_pin.connected_pin.data)

    def compute(self):
        print(self.input_pin.data)