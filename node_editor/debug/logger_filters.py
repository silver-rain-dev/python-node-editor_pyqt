import logging

class NodeEditorFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith('NodeEditor')
    

class NodeGraphFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith('NodeGraph')