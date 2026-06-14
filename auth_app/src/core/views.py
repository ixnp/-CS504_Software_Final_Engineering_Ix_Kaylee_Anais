from flask import Blueprint, render_template
from flask_login import login_required

core_bp = Blueprint("core", __name__)

#Renders home if user is logged in
@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")