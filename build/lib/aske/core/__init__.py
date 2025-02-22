class Platform:
    """
    Main class for defining and managing platform architecture
    """
    def __init__(self, name):
        self.name = name
        self.components = {}

    def add_component(self, name, **properties):
        """Add a component to the platform"""
        self.components[name] = properties
        return self

    def get_component(self, name):
        """Get a component by name"""
        return self.components.get(name)

    def list_components(self):
        """List all components"""
        return list(self.components.keys())
