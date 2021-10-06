import os

from flask import Flask, flash, redirect, render_template, session#, request
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

import urllib.parse

try:
    from helpers import apology
except ImportError:
    from .helpers import apology

try:

    # Configure application
    app = Flask(__name__)

    # Ensure templates are auto-reloaded
    app.config["TEMPLATES_AUTO_RELOAD"] = True


    @app.route("/")
    def home_page():
        return render_template("home_page.html")


    @app.route("/games")
    def games():
      return render_template("games.html")


    @app.route("/study_zone")
    def study_zone():
      return render_template("study.html")
    

    @app.route("/panic")
    def panic():
      return render_template("panic.html")


    def errorhandler(e):
      # Handle error 
      if not isinstance(e, HTTPException):
          e = InternalServerError()
      return apology(e.name, e.code)


    # Listen for errors
    for code in default_exceptions:
        app.errorhandler(code)(errorhandler)


except:
  session.rollback()