from flask import render_template, redirect, url_for, flash, request, Blueprint
from . import bp


@bp.route("/app_function")
def app_function():
    return render_template("home.html", title="App Function")