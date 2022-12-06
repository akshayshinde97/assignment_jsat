import traceback
from flask_restful import Resource, reqparse, request
import datetime
import json

# local imports
from store.utils import response_json, build_cors_preflight_response
from store.models import Supplier
from store.schemas import SupplierSchema
import logging

LOGGER = logging.getLogger("store_app")


class SupplierApi(Resource):
    '''
    post api to update supplier info
    get api to the get the supplier info.
    '''

    def get(self):
        try:
            # if id is None:
            supplier_db_data = Supplier.query.filter().all()

            supplier_schema = SupplierSchema(many=True)

            return supplier_schema.jsonify(supplier_db_data)
        except Exception as e:
            print(traceback.format_exc(), e)
            LOGGER.exception('Exception in supplier get api', exc_info=True)
            return {
                "error": "There was an error please try after sometime"}

    def post(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                supplier_json = request.get_json()
                supplier_query = Supplier.query.filter(
                    Supplier.name == supplier_json['name'],
                    Supplier.address == supplier_json['address'],
                    Supplier.contact == supplier_json['contact']).one_or_none()

                if supplier_query:
                    return response_json(
                        False, {}, f"{supplier_json['name']} already exists")

                supplier_obj = Supplier(
                    name=supplier_json['name'],
                    address=supplier_json['address'],
                    contact=supplier_json['contact'],
                    is_active=True,
                    created_on=datetime.datetime.now(),
                    updated_on=datetime.datetime.now()
                )

                supplier_obj.save()
                return response_json(
                    True, {}, f"Successfully added {supplier_json['name']}")
            except Exception as e:
                print(traceback.format_exc(), e)
                LOGGER.exception('Exception in supplier post api', exc_info=True)
                return {
                    "error": "There was an error please try after sometime"}

    def delete(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                supplier_json = request.get_json()
                existing_store = Supplier.query.get(supplier_json['id'])
                if existing_store:
                    Supplier.delete_from_db(existing_store)
                    return response_json(
                        True, {}, f"{supplier_json['id']} successfully deleted")
                else:
                    return response_json(
                        True, {}, f" supplier id {supplier_json['id']} not found")

            except Exception as e:
                print(traceback.format_exc(), e)
                LOGGER.exception('Exception in supplier delete api', exc_info=True)
                return {
                    "error": "There was an error please try after sometime"}
