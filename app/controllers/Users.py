from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')

    def sendhome(self):
        return redirect('/main')

    def index(self):
        return self.load_view('index.html')

    def action(self):
        # action addresses both registrations and logins
        # the if checks to see if the action is a register
        if request.form['action'] == 'register':
            logged = self.models['User'].register(request.form.copy())
            if not logged['status']:
                for message in logged['errors']:
                    flash(message, 'regis_errors')
                return redirect('/main')
            session['user'] = logged['logged']
            return redirect('/quotes')
        # if the action was not register we know it was a login
        logged = self.models['User'].login(request.form.copy())
        if not logged['status']:
            for message in logged['errors']:
                flash(message, 'regis_errors')
            return redirect('/main')
        session['user'] = logged['logged']
        return redirect('/quotes')

    def logout(self):
        session.clear()
        return redirect('/main')

    def user(self, id):
        # user will populate number of quotes created by user and print each one out
        userquotes = self.models['User'].user(id)
        print userquotes
        count = len(userquotes)
        alias = userquotes[0]['alias']
        return self.load_view('user.html', quotes = userquotes, count = count, alias = alias)
