from bottle import run, route, view, get, post, request
from itertools import count

def __init__(comic_name, comic_num): 
    #not passing ID as we want it to create it.
    self.id = next(self._ids)
    self.comic_name = comic_name
    self.comic_num = comic_num


comics = [
    comic("Super Dude", "Quantity = 'comic_num'", False),
    comic("Water Woman", "Quantity = 'comic_num'", False),
	comic("Lizard man", "Quantity = 'comic_num'", False),
    ]

@route('/')
@view ('index')
def index():
    #need this function to attach the decorators above.
    pass

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)