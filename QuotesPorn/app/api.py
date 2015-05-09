#QuotesPorn

import os
from flask import Flask, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class Subreddit(db.Model):
    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    createdUtc = db.Column(db.Integer, index = True)
    score = db.Column(db.Integer)
    title = db.Column(db.String(125), index=True)
    author = db.Column(db.String(125), index=True)
    ups = db.Column(db.Integer, index = True)
    downs = db.Column(db.Integer, index = True)
    num_comments = db.Column(db.Integer, index = True)
    permalink = db.Column(db.String(125), index=True)
    url = db.Column(db.String(125), index=True)
    

    def get_url(self):
        return url_for('get_quotes', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'createdUtc': self.createdUtc,
            'score': self.score,
            'title': self.title,
            'author': self.author,
            'ups': self.ups,
            'downs': self.downs,
            'num_comments': self.num_comments,
            'permalink': self.permalink
        }

    def import_data(self, data):
        try:
            self.get_url(),
            self.createdUtc = data['createdUtc']
            self.score = data['score']
            self.title = data['title']
            self.author = data['author']
            self.ups = data['ups']
            self.downs = data['downs']
            self.num_comments = data['num_comments']
            self.permalink = data['permalink']
        except KeyError as e:
            raise ValidationError('Invalid quote: missing ' + e.args[0])
        return self


@app.route('/QuotesPorn/', methods=['GET'])
def get_quotes():
    return jsonify({'quotes': [quotes.get_url() for quotes in
                                  Subreddit.query.all()]})

@app.route('/QuotesPorn/<int:id>', methods=['GET'])
def get_quote(id):
    return jsonify(Subreddit.query.get_or_404(id).export_data())

@app.route('/QuotesPorn/', methods=['POST'])
def new_quote():
    quotes = Subreddit()
    quotes.import_data(request.json)
    db.session.add(quotes)
    db.session.commit()
    return jsonify({}), 201, {'Location': quotes.get_url()}

@app.route('/QuotesPorn/<int:id>', methods=['PUT'])
def edit_quote(id):
    quotes = Subreddit.query.get_or_404(id)
    quotes.import_data(request.json)
    db.session.add(quotes)
    db.session.commit()
    return jsonify({})

@app.route('/')
def index():
    highlight = {'min': 1, 'max': 2}
    quotes = Subreddit.query.all()
    return render_template('index.html', quotes=quotes, highlight=highlight)
    
@app.route('/QuotesPorn/highestScore/')
def highestScore():
    highlight = {'min': 1, 'max': 2}
    quotes = Subreddit.query.order_by(Subreddit.score.desc())
    return render_template('index.html', quotes = quotes, highlight=highlight)
    
@app.route('/QuotesPorn/lowestScore/')
def lowestScore():
    highlight = {'min': 1, 'max': 2}
    quotes = Subreddit.query.order_by(Subreddit.score.asc())
    return render_template('index.html', quotes = quotes, highlight=highlight)    


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
