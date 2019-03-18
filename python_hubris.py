from bottle import run, route, view, get, post, request
from itertools import count

class Comic:

    _ids = count (0)

    def __init__(self,comic_name, comic_num): 
        self.id = next(self._ids)
        self.comic_name = comic_name
        self.comic_num = comic_num


comics = [
    Comic("Super Dude", "3"),
    Comic("Water Woman", "9"),
    Comic("Lizard man", "13")
    ]

@route('/')
@view ('index')
def index():
    pass


@route('/card')
@view ('card')
def card():
    data = dict (book_info = comics)
    return data

@route('/buy_comic')
@view ('buy_comic')
def buy_comic():
    pass



run(host='0.0.0.0', port = 8080, reloader=True, debug=True)