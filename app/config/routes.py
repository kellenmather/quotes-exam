from system.core.router import routes

# these routes manage get routes for the user
routes['GET']['/main'] = 'Users#index'
routes['GET']['/'] = 'Users#sendhome'
routes['GET']['/user/logout'] = 'Users#logout'
routes['GET']['/user/<id>'] = 'Users#user'
# this route manages login and registration requests
routes['POST']['/user/action'] = 'Users#action'
# this route retrieves the list of quotes and user favorite quotes
routes['GET']['/quotes'] = 'Quotes#quotes'
# these routes govern users interaction with quotes they all petition the DB
routes['POST']['/quotes/new'] = 'Quotes#new'
routes['POST']['/quotes/fav'] = 'Quotes#fav'
routes['POST']['/quotes/remove'] = 'Quotes#remove'
