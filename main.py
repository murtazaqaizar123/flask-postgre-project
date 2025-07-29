from app import app
from app.models import User, Post
from app import db


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
