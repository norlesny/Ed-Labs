class TreeNode:
    def __init__(self, name) -> None:
        super().__init__()

        self.name = name
        self.connections = {}

    def add_node(self, operation, node):
        self.connections[operation] = node

    def custom_string(self, shift):
        tree = ""
        shift_str = '\t'
        for x in range(shift):
            shift_str += '\t'
        for c in self.connections:
            tree += shift_str + str(c) + ' -> ' + self.connections[c].custom_string(shift + 1) + '\n'

        return self.name + '\n' + tree

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.custom_string(0)
