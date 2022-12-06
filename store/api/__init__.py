from .routes import api_bp


def init_api(app):

    app.register_blueprint(api_bp, url_prefix='/api')
