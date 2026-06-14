#Krishna, A. (2023, November 27). How to Implement Two-Factor Authentication with PyOTP and Google Authenticator in Your Flask App. freeCodeCamp.org. https://www.freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app/
#CLI access, will allow the addition of other commands if required 
from flask.cli import FlaskGroup

from src import app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()