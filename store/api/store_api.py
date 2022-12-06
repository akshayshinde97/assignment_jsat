import traceback
from flask_restful import Resource, reqparse, request
from flask import jsonify
import datetime
import json


# local imports
from store.utils import response_json, build_cors_preflight_response
from store.models import StoreMetadata
from store.schemas import StoreMetadataSchema


class StoreApi(Resource):
    '''
    post api to update store info by admin only
    get api to the get the store info admin only access.
    '''

    def get(self):
        try:
            store_db_data = StoreMetadata.query.filter().all()

            store_schema = StoreMetadataSchema(many=True)

            return store_schema.jsonify(store_db_data)

        except Exception as e:
            print(traceback.format_exc(), e)
            return {
                "error": "There was an error please try after sometime"}

    def post(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                store_json = request.get_json()
                store_query = StoreMetadata.query.filter(
                    StoreMetadata.name == store_json['name'],
                    StoreMetadata.address == store_json['address']).one_or_none()

                if store_query:
                    return response_json(
                        False, {}, f"{store_json['name']} Store already exist")

                storeMetadata_obj = StoreMetadata(
                    name=store_json['name'],
                    address=store_json['address'],
                    manager=store_json['manager'],
                    contact=store_json['contact'],
                    is_active=True,
                    created_on=datetime.datetime.now(),
                    updated_on=datetime.datetime.now()
                )

                storeMetadata_obj.save()
                return response_json(
                    True, {}, f"Successfully added {store_json['name']}")
            except Exception as e:
                print(traceback.format_exc(), e)

                return {
                    "error": "There was an error please try after sometime"}

    def delete(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                store_json = request.get_json()
                existing_store = StoreMetadata.query.get(store_json['id'])
                if existing_store:
                    StoreMetadata.delete_from_db(existing_store)
                    return response_json(
                        True, {}, f"{store_json['id']} successfully deleted")
                else:
                    response_json(
                        True, {}, f"Store ID {store_json['id']} not found")

            except Exception as e:
                print(traceback.format_exc(), e)
                return {
                    "error": "There was an error please try after sometime"}
