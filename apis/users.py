from flask import Blueprint, Response, request
from utils.users import user_signup
users_api = Blueprint("users",__name__)


@users_api.route("/user/signup", methods=['POST'])
def signup():
    data = request.get_json()
    user_id = user_signup(data)
    if user_id:
        response = {
            "message":'Data found',
            "data":{'user_id':user_id},
            "status_code":200
        }
    else:
        response = {
            "message":'Data not found',
            "status_code":500
        }
    return response