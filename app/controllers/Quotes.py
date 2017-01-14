from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)

        self.load_model('Quote')

    # populates two lists: quote list, favorite list
    def quotes(self):
        quotes = self.models['Quote'].quotelist(session['user']['id'])
        favorites = self.models['Quote'].favlist(session['user']['id'])
        return self.load_view('quotes.html', qlist = quotes, flist = favorites)

    # creates a new quote
    def new(self):
        quote = self.models['Quote'].addnew(request.form.copy())
        if not quote['status']:
            for message in quote['errors']:
                flash(message, 'regis_errors')
            return redirect('/quotes')
        return redirect('/quotes')

    # adds a quote to favorites
    def fav(self):
        fav = self.models['Quote'].fav(request.form.copy())
        return redirect('/quotes')

    # removes a quote from favorites
    def remove(self):
        remove = self.models['Quote'].remove(request.form.copy())
        return redirect('/quotes')
