class ActionHandler:
    def __init__(self, tools):
        self.tools = tools

    def execute(self, action, params):
        if action in self.tools:
            return self.tools[action](**params)
        return f"Unknown action: {action}"