class DataEntry:

    def __init__(self, attributes, classification=0) -> None:
        assert type(attributes) is list

        self.attributes = attributes
        self.classification = classification

    def __str__(self) -> str:
        return "{}: {}".format(self.classification, self.attributes)

    def __repr__(self) -> str:
        return self.__str__()
