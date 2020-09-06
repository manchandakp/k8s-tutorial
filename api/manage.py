from flask.cli import FlaskGroup
from project.main import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
