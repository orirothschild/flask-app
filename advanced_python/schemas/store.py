from schemas.item import ItemSchema
from ma import ma
# our marshmello can accsess the information from the app
#using sqlachamy and marshmello
from models.store import StoreModel
#pass list of item modules
class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many = True)
    class Meta:
        #here' we are giving marshmellow thoe model it needs to create
        #only by explaining that we can delete the usermodel init method

        # A Building block of sorts
        model = StoreModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
