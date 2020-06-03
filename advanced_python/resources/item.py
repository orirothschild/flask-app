from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from marshmallow import ValidationError
from models.item import ItemModel
from schemas.item import ItemSchema
from libs.strings import gettext #runs only once as this is importent at many diffrent modules

item_schema = ItemSchema()

#pass list of item modules
item_list_schema = ItemSchema(many=True)


class Item(Resource):
    @classmethod
    def get(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200

        return {"message": gettext("item_not_found")}, 404

    @classmethod
    @fresh_jwt_required
    def post(cls, name: str): # item name only exists in the resource and not the post data
        if ItemModel.find_by_name(name):
            return {"message": gettext("item_name_exists").format(name)}, 400

        item_json = request.get_json()
        item_json["name"] = name
        item = item_schema.load(item_json)

        try:
            item.save_to_db()
        except:
            return {"message": gettext("item_error_inserting")}, 500

        return item_schema.dump(item), 201

    @classmethod
    @jwt_required
    def delete(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": gettext("item_deleted")}, 200

        return {"message": gettext("item_not_found")}, 404

    @classmethod
    def put(cls, name: str):
        item_json = request.get_json()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = item_json["price"]
        else:
            item_json["name"] = name
            item = item_schema.load(item_json)

        item.save_to_db()

        return item_schema.dump(item), 200


class ItemList(Resource):
    @classmethod
    def get(cls):
        #dumps a list of each item
        return {"items": item_list_schema.dump(ItemModel.find_all())}, 200
