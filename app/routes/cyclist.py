from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.cyclist import Cyclist
# from .routes_helper import get_one_obj_or_abort

cyclist_bp = Blueprint("cyclist_bp", __name__, url_prefix="/cyclist")

@cyclist_bp.route("", methods=["POST"])
def add_cyclist():
    request_body = request.get_json()

    new_cyclist = Cyclist.from_dict(request_body)

    db.session.add(new_cyclist)
    db.session.commit() # DO NOT FORGET THIS METHOD! Think git add followed by git commit

    return {"id": new_cyclist.id}, 201

@cyclist_bp.route("", methods=["GET"]) # the reason for the empty string because I just want all of the bikes, periodt. What http methods do we want?
def get_all_cyclist():

    name_param = request.args.get("name")

    if name_param is None:
        cyclists = Cyclist.query.all()
    else:
        bikes = Cyclist.query.filter_by(name=name_param)
        
    response = [cyclist_bp.to_dict() for cyclist in cyclists] # list comprehension, instead of creating an empty response list
    #                                             set response to what you want in it.

    return jsonify(response), 200 

@cyclist_bp.route("/<cyclist_id>/bike", methods=["GET"])
def get_all_bikes_belonging_to_a_cyslist(cyclist_id):
    cyclist = get_one_or_abort(Cyclist, cyclist_id)