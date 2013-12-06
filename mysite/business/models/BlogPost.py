from mysite import db


# blog post data model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    writer = db.Column(db.String(10), default='Cal')
    post = db.Column(db.String(10000))

    def __init__(self, writer, text):
        self.writer = writer
        self.post = text
