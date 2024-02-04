from node_editor.node import Node


class Add_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Add"
        self.type_text = "Logic Nodes"
        self.set_color(title_color=(0, 128, 0))

        self.add_pin(name="Ex In", is_output=False, execution=True)
        self.add_pin(name="Ex Out", is_output=True, execution=True)

        self.input_pin1 = self.add_pin(name="input A", is_output=False)
        self.input_pin2 = self.add_pin(name="input B", is_output=False)
        self.add_pin(name="output", is_output=True)
        self.build()

        self.sum = 0

    def execute_inputs(self):
        if self.input_pin1:
            self.input_pin1.set_data(self.input_pin1.connected_pin.data)
        if self.input_pin2:
            self.input_pin2.set_data(self.input_pin2.connected_pin.data)
        
    def compute(self):
        num1 = self.input_pin1.data if self.input_pin1.data else 0
        num2 = self.input_pin2.data if self.input_pin2.data else 0
        self.sum = num1 + num2
        return self.sum

    def execute_outputs(self):
        if output_pin := self.get_pin("output"):
            output_pin.set_data(self.sum)
        
