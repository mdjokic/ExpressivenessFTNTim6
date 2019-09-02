from Core.base.abstract.Models import Node


class Person(Node):

    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)
        self.birthDate = kwargs.get('birthDate')
        self.birthPlace = kwargs.get('birthPlace')

    def get_data(self):
        return {
            'name': self.name,
            'birthDate': self.birthDate,
            'birthPlace': self.birthPlace
        }
