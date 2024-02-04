from PyQt5 import QtWidgets

from node_editor.node import Node

class Begin_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Begin"
        self.type_text = "Begin Node"
        self.set_color(title_color=(128, 0, 0))
        self.add_pin(name="Ex Out", is_output=True, execution=True)

        self.build()

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()

    def compute(self):
        pass
