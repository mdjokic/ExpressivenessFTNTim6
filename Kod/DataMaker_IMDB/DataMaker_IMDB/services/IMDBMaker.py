from Core.services.DataMaker import DataMaker
from Core.base.Graph import Graph
from DataMaker_IMDB.extended.Movie import Movie
from DataMaker_IMDB.extended.Person import Person
from DataMaker_IMDB.extended.Acting import Acting
from DataMaker_IMDB.extended.Directing import Directing
from django.apps.registry import apps
from imdb import IMDb


class IMDBMaker(DataMaker):

    def __init__(self):
        super(IMDBMaker, self).__init__('IMDB Data maker', 'imdb')
        self.data = set()
        self.yearMax = 3000
        self.yearMin = 0
        self.movies = dict()

    def create_data(self):
        imdb = IMDb(adultSearch=False)
        graph = Graph()
        # Looks up info for one person at the time
        for search_term in self.data:
            person = imdb.search_person(search_term, results=1)[0]
            imdb.update(person, ['filmography', 'biography'])
            personNode = self.createPersonNode(person)
            graph.add_node(personNode)
            # Looks up movies worked on based on the job done
            for jobs in person['filmography']:
                self.addMovies('actor', jobs, personNode, Acting, graph)
                self.addMovies('actress', jobs, personNode, Acting, graph)
                self.addMovies('director', jobs, personNode, Directing, graph)
        # Sets the core graph value
        apps.get_app_config('Core').graph = graph

    def save_data(self):
        pass

    def load_data(self):
        pass

    def send_data(self, payload):
        self.data = payload['persons']
        try:
            yearMin = int(payload['yearMin'])
            self.yearMin = yearMin
        except ValueError:
            pass     
        try:
            yearMax = int(payload['yearMax'])
            self.yearMax = yearMax
        except ValueError:
            pass
    
    def createPersonNode(self, person):
        return Person(nodeName=person.get('name'),
                      birthDate=person.get('birth date'),
                      birthPlace=person.get('birth notes'))
    
    def createMovieNode(self, movie):
        if movie.get('year') is not None and (int(movie.get('year')) > self.yearMin and int(movie.get('year')) < self.yearMax):
            return Movie(nodeName=movie.get('title'),
                        year=movie.get('year'))

    def addMovies(self, jobkeyword, jobs, personNode, edgeType, graph):
        if jobkeyword in jobs.keys():
            for movie in jobs[jobkeyword]:
                if movie.get('title') in self.movies:
                    edge = edgeType(node1=personNode, node2=self.movies[movie.get('title')])
                    graph.add_edge(edge)
                else:
                    movieNode = self.createMovieNode(movie)
                    if (movieNode is not None):
                        edge = edgeType(node1=personNode, node2=movieNode)
                        self.movies[movie.get('title')] = movieNode
                        graph.add_node(movieNode)
                        graph.add_edge(edge)