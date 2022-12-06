"""
Routing urls for the Api app
"""

# third-party imports
from flask import Blueprint
from flask_restful import Api

# local imports
from .store_api import StoreApi
from .category_api import CategoryApi
from .supplier_api import SupplierApi
from .items_api import ItemsApi
# pylint: disable=invalid-name
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Store routes
api.add_resource(StoreApi, '/managestore')
# api.add_resource(ItemsApi, '/manageitems')

# Category_API
api.add_resource(CategoryApi, '/managecategory')

# Supplier_API
api.add_resource(SupplierApi, '/managesupplier')

# items_API
api.add_resource(ItemsApi, '/manageitem')
