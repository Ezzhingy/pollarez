import os

from functools import wraps
from flask import g, request, redirect, url_for, render_template, session


def apology(message, code=400):
    return render_template("apology.html", message=message, code=code), code