import webapp2

from rdflib import Graph
from dbstore import NDBStore

class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/sparql-results+json; charset=utf-8'

        graph = Graph(store = NDBStore(identifier = 'test-graph'))
        result = graph.query(self.request.get('query')).serialize(format='json')

        self.response.write(result)

    def post(self):
        graph = Graph(store = NDBStore(identifier = 'test-graph'))
        graph.update(self.request.body)

        self.response.set_status(204)

app = webapp2.WSGIApplication([('/s/main', MainHandler)], debug=True)
