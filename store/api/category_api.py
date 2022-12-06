import traceback
from flask_restful import Resource, reqparse, request
from flask import jsonify
import datetime
import json
import logging

# local imports
from store.utils import response_json, build_cors_preflight_response
from store.models import Category
from store.schemas import CategorySchema

LOGGER = logging.getLogger("store_app")


class CategoryApi(Resource):
    '''
    This class handles the get,post, delete api for Categories.
    '''
    def get(self, id=None):
        try:
            if id is None:
                catg = Category.query.filter().all()
                catg_schema = CategorySchema(many=True)
                return catg_schema.jsonify(catg)
            else:
                LOGGER.info('got no id for category sending them all')
                catg = Category.query.filter_by(id=id).first()
                catg_schema = CategorySchema(many=True)
                return catg_schema.jsonify(catg)
        except Exception as e:
            print(traceback.format_exc(), e)
            # jsonify({"error":"There was an error please contact the administrator"})
            LOGGER.exception('Exception in get api category')
            return {
                "error": "There was an error please try after sometime"}

    def post(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                catg_json = request.get_json()
                catg_query = Category.query.filter(
                    Category.name == catg_json['name']).one_or_none()
                print(catg_query, type(catg_query))
                # returns True or False
                if catg_query:
                    return response_json(
                        False, {}, f"{catg_json['name']} catagory already exist")
                catg_json['created_on'] = datetime.datetime.now()
                catg_json['updated_on'] = datetime.datetime.now()
                category_obj = Category(
                    name=catg_json['name'],
                    discription=catg_json['discription']
                )
                category_obj.save()
                return response_json(
                    True, {}, f"Successfully added {catg_json['name']}")
            except Exception as e:
                print(traceback.format_exc(), e)
                LOGGER.exception('Exception in post api category')
                return {
                    "error": "There was an error please try after sometime"}

    def delete(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                catg_json = request.get_json()
                existing_catg = Category.query.get(catg_json['id'])
                if existing_catg:
                    Category.delete_from_db(existing_catg)
                    # return make_response(f"{note_id} successfully deleted",
                    # 204)
                    return response_json(
                        True, {}, f"{catg_json['id']} successfully deleted")
                else:
                    response_json(True, {}, f"{catg_json['id']}ID not found")

            except Exception as e:
                print(traceback.format_exc(), e)
                LOGGER.exception(f'Exception in delete api category')
                return {
                    "error": "There was an error please try after sometime"}
