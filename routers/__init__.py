from .route import shop_bp
def register_routes(app):
    app.register_blueprint(shop_bp)