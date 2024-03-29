import os

from webapp import db, migrate, create_app, celery
from webapp.auth.models import User
from webapp.blog.models import Post, Tag

env = os.environ.get("WEBAPP_ENV", "dev")
app = create_app(f"config.{env.capitalize()}Config")


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Tag=Tag,
                migrate=migrate, celery=celery)
