from Core.base.abstract.Models import Node


class Movie(Node):

    def __init__(self, **kwargs):
        super(Movie, self).__init__(**kwargs)
        self.year = kwargs.get('year')

    def get_data(self):
        return {
            'title': self.name,
            'year': self.year,
        }
