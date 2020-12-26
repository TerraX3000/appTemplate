from flask import render_template, redirect, url_for, flash, request, Blueprint
from . import bp

# main_bp = Blueprint("main_bp", __name__)


@bp.route("/")
def homePage():
    return render_template("home.html", title="Home")


@bp.route("/about")
def aboutPage():
    return render_template("about.html", title="About")
