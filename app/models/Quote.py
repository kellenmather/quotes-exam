from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def addnew(self, info):
        errors = []
        if not info['qb']:
            errors.append('Quoted by must be entered')
        elif len(info['qb']) < 3:
            errors.append('Quoted by must be at least three characters')

        if not info['quote']:
            errors.append('A Quote must be entered')
        elif len(info['quote']) < 10:
            errors.append('Your Quote must be at least ten characters')
        if errors:
            return { 'status' : False, 'errors' : errors }
        query = "INSERT INTO quote (qb, quote, user_id) VALUES (:qb, :quote, :user_id)"
        data = { 'qb' : info['qb'], 'quote' : info['quote'], 'user_id' : info['uid'] }
        self.db.query_db(query, data)
        return { 'status' : True }

    def quotelist(self, id):
        query = "SELECT q.id qid, q.quote, q.qb author, u.id poster, u.alias alias FROM quote q JOIN user u ON u.id = q.user_id WHERE q.id NOT IN (SELECT q.id qid FROM quote q JOIN fav f ON f.quote_id = q.id WHERE f.user_id = :id)"
        data = { 'id' : id }
        return self.db.query_db(query, data)

    def favlist(self, id):
        query = "SELECT quote.id as qid, quote.qb as qb, quote.quote as quote, quote.user_id as quid, fav.id as fid, fav.user_id as fuid, fav.quote_id as fqid, user.alias as alias, user.id as origin FROM quote LEFT JOIN fav on fav.quote_id = quote.id LEFT JOIN user on user.id = quote.user_id WHERE fav.user_id LIKE :id"
        data = { 'id' : id }
        return self.db.query_db(query, data)

    def fav(self, info):
        query = "INSERT INTO fav (user_id, quote_id) VALUES (:user_id, :quote_id)"
        data = { 'user_id' : info['uid'], 'quote_id' : info['qid'] }
        return self.db.query_db(query, data)

    def remove(self, info):
        print 'got here'
        print info
        query = "DELETE FROM fav WHERE id = :id"
        data = { 'id' : info['fid'] }
        return self.db.query_db(query, data)
