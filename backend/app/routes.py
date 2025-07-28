from flask import Blueprint, jsonify, request
from .models import Product
from . import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/admin')
def home():
    return "Админ-панель API"
