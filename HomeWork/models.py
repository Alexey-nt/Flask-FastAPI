from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Authors(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    book = db.relationship('Books', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'Author({self.name}, {self.lastname})'


class Books(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name_book = db.Column(db.String(80), nullable=False)
    year_of_publication = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id_'), nullable=False)

    def __repr__(self):
        return f'Books({self.name_book})'
