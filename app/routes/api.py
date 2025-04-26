from flask import Blueprint, request, jsonify
from app.models.user_model import get_user_by_username
from app.models.login_model import create_login_log
from app.models.user_model import create_user
from app import blacklist
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

api_bp = Blueprint('api', __name__)

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = get_user_by_username(username)
    
    if user and user['password'] == password:
        create_login_log(username, True)
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': refresh_token
        }), 200
    else:
        create_login_log(data.get('username'), False)
        return jsonify({'message': 'Login failed'}), 401
    



@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = get_user_by_username(data.get('username'))
    
    if user :
        create_login_log(data.get('username'), False)
        return jsonify({'message': 'Duplicate User'}), 401
    else:
        create_user(data)
        create_login_log(data.get('username'), True)
        return jsonify({'message': 'Create User'}), 200


@api_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({
        'message': f'Welcome {current_user}!'
    })


@api_bp.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def logout():
    jti = get_jwt()['jti']  # JWT ID
    blacklist.add(jti)
    return jsonify({"message": "Refresh token revoked"}), 200



@api_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)

    return jsonify({
        'access_token': new_access_token
    }), 200