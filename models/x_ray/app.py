from flask import Blueprint, render_template


xray_bp = Blueprint('xray', __name__, template_folder='.')


@xray_bp.route('/')
def xray_home():
    return render_template('blood.html')

