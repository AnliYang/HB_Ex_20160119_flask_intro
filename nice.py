from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Home page.</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <a href="/hello">Hello!</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          <label>Select a compliment:</label>
          <br>
          <input type="radio" name="greeting" value="awesome">You are awesome!</input>
          <br> 
          <input type="radio" name="greeting" value="terrific">You are terrific!</input>
          <br>
          <input type="radio" name="greeting" value="fantastic">You are fantastic!</input>
          <br>
          <input type="radio" name="greeting" value="neato">You are neato!</input>
          <br>
          <input type="radio" name="greeting" value="fantabulous">You are fantabulous!</input>
          <br>
          <input type="radio" name="greeting" value="wowza">You are wowza!</input>
          <br>
          <input type="radio" name="greeting" value="oh-so-not-meh">You are oh-so-not-meh!</input>
          <br>
          <input type="radio" name="greeting" value="brilliant">You are brilliant!</input>
          <br>
          <input type="radio" name="greeting" value="ducky">You are ducky!</input>
          <br>
          <input type="radio" name="greeting" value="coolio">You are coolio!</input>
          <br>
          <input type="radio" name="greeting" value="incredible">You are incredible!</input>
          <br>
          <input type="radio" name="greeting" value="wonderful">You are wonderful!</input>
          <br>
          <input type="radio" name="greeting" value="smashing">You are smashing!</input>
          <br>
          <input type="radio" name="greeting" value="lovely">You are lovely!</input>
          <br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet', methods=['post'])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    compliment = request.form.get('greeting')

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False)
