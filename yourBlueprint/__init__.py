from flask import Blueprint
yourBlueprint_bp = Blueprint('yourBlueprint', __name__)
from yourBlueprint.info import *
from yourBlueprint.op import *