from store.db import ma


class StoreMetadataSchema(ma.Schema):
    '''
    StoreMetadata Schema
    '''
    class Meta:
        fields = (
            'id',
            'name',
            'address',
            'manager',
            'contact',
            'created_on',
            'updated_on'
        )


class ItemSchema(ma.Schema):
    '''
    Item Schema
    '''
    class Meta:
        fields = (
            'id',
            'name',
            'discription',
            'mrp',
            'sup_id',
            'category_id',
            'store_id',
            'created_on',
            'updated_on'
        )



class CategorySchema(ma.Schema):
    '''
    Category Schema
    '''
    class Meta:
        fields = (
            'id',
            'name',
            'discription',
            'created_on',
            'updated_on',
        )



class SupplierSchema(ma.Schema):
    '''
    Supplier Schema
    '''
    class Meta:
        fields = (
            'id',
            'name',
            'address',
            'is_active',
            'contact',
            'created_on',
            'updated_on'
        )
