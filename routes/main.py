from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.user import User

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', user=current_user)

@bp.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return render_template('errors/403.html', title='Forbidden'), 403
    users = User.query.all()
    return render_template('admin/dashboard.html', title='Admin Dashboard', users=users) 