
# creating our basic user schema by using marshmellow
from ma import ma
from models.item import ItemModel
# our marshmello can accsess the information from the app
#using sqlachamy and marshmello
from models.store import StoreModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #here' we are giving marshmellow thoe model it needs to create
        #only by explaining that we can delete the usermodel init method
        model = ItemModel
        load_only = ("store",)
        dump_only = ("id",)
        include_fk = True