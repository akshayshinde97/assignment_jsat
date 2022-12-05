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

# api.add_resource(ApiResource, '/last', methods=['GET'], endpoint='last')
# api.add_resource(
#     ApiResource, '/grab_and_save',
#     methods=['POST'],
#     endpoint='grab_and_save'
# )

#Store routes
api.add_resource(StoreApi, '/managestore')
# api.add_resource(ItemsApi, '/manageitems')

#Category_API
api.add_resource(CategoryApi, '/managecategory')

#Supplier_API
api.add_resource(SupplierApi, '/managesupplier')

#items_API
api.add_resource(ItemsApi, '/manageitem')
# api.add_resource(SuppliersApi, '/manageSupplier')
# user routes
# api.add_resource(UserRegistration, '/registration')
# api.add_resource(UserLogin, '/login')
# api.add_resource(UserLogoutAccess, '/logout/access')
# api.add_resource(UserLogoutRefresh, '/logout/refresh')
# api.add_resource(TokenRefresh, '/token/refresh')
# api.add_resource(AllUsers, '/users')
# api.add_resource(SecretResource, '/secret')

# # dashboard routes
# api.add_resource(DashboardApi, '/getdocs/<userid>/<docid>')
# api.add_resource(DeleteDocument, '/deletedoc/<userid>')
# api.add_resource(EditApi, '/edit/<userid>/<userdocid>')

# #result routes
# api.add_resource(DocumentResultApi, '/docresult/<userid>/<userdocid>')
# api.add_resource(PDFApi, '/pdf/<path:path>')
# api.add_resource(HomeApi, '/docs/<userid>')
# api.add_resource(MasterTable, '/mtinsights')
# api.add_resource(UpdateMastertable, '/updatemt')
