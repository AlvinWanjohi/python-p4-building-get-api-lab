from flask import Flask
from flask_restful import Api
from server.models import db
from server.resources import BakeryList, BakeryById, BakedGoodsByPrice, MostExpensiveBakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

# Register routes
api.add_resource(BakeryList, '/bakeries')
api.add_resource(BakeryById, '/bakeries/<int:id>')
api.add_resource(BakedGoodsByPrice, '/baked_goods/by_price')
api.add_resource(MostExpensiveBakedGood, '/baked_goods/most_expensive')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port if needed
