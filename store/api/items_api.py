import traceback
from flask_restful import Resource, reqparse, request
from flask import jsonify
import datetime
import json


# local imports
from store.utils import response_json, make_request, build_cors_preflight_response
from store.models import Item, Supplier
from store.schemas import ItemSchema






class ItemsApi(Resource):
    '''
    post api to update store info by admin only
    get api to the get the store info admin only access.
    '''

    def get(self):
        try:
            item_data = Item.query.filter().all()
            result ={}
            # item_schema = ItemSchema(many=True)

            for indx,item_obj in enumerate(item_data):
                obj = {}
                obj["name"] = item_obj.name
                obj["discription"] = item_obj.discription
                obj["mrp"]=item_obj.mrp
                obj["category_id"]=item_obj.category_id
                obj["store_id"]=item_obj.store_id
                obj["quantity"]=item_obj.quantity
                inner_obj = {}
                for indx,sup_obj in enumerate(item_obj.sup_id):
                    inner_obj[indx]=sup_obj.name
                obj["supplier_details"]=inner_obj
                result[indx]=obj
            return response_json(True, result, f'Succesfully fetched all the items')

        except Exception as e:
            print(traceback.format_exc(), e)
            return {
                "error": "There was an error please try after sometime"}

    def post(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                item_json = request.get_json()
                item_obj = Item()
                supplier_list = list()
                # item_query = Item.query.filter(
                #     Item.name == item_json['name'], Item.sup_id == item_json['supplier_id']).one_or_none()

                # if item_query:
                #     return response_json(False, {}, f"{item_json['name']} item already exists")
                for sup_id in item_json['supplier_id']:
                    supplier_obj = Supplier.query.filter(Supplier.id==sup_id).first()
                    print(supplier_obj, type(supplier_obj))
                    supplier_list.append(supplier_obj)

                item_obj = Item(
                    name=item_json['name'],
                    discription=item_json['discription'],
                    mrp=item_json['mrp'],
                    quantity=item_json['quantity'],
                    sup_id=supplier_list,
                    store_id=item_json['store_id'],
                    category_id=item_json['category_id'],
                    created_on=datetime.datetime.now(),
                    updated_on=datetime.datetime.now()
                )

                item_obj.save()
                return response_json(True, {}, f"Successfully added {item_json['name']}")
            except Exception as e:
                print(traceback.format_exc(), e)

                return {
                    "error": "There was an error please try after sometime"}

    def delete(self):
        if request.method == "OPTIONS":  # CORS preflight
            return build_cors_preflight_response()
        else:
            try:
                item_json = request.get_json()
                existing_store = Item.query.get(item_json['id'])
                if existing_store:
                    Item.delete_from_db(existing_store)
                    return response_json(True, {}, f"{item_json['id']} successfully deleted")
                else:
                    response_json(True, {}, f"Store ID {item_json['id']} not found")

            except Exception as e:
                print(traceback.format_exc(), e)
                return {
                    "error": "There was an error please try after sometime"}
