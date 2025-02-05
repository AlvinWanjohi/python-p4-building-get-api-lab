from flask import Flask
from flask_restful import Api, Resource
from server.models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bakery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db.init_app(app)

api = Api(app)

class BakeryList(Resource):
    def get(self):
        bakeries = Bakery.query.all()
        return [
            {
                'id': bakery.id,
                'name': bakery.name,
                'baked_goods': [{'id': good.id, 'name': good.name, 'price': good.price} for good in bakery.baked_goods]
            }
            for bakery in bakeries
        ]

class BakeryById(Resource):
    def get(self, id):
        bakery = Bakery.query.get(id)
        if bakery:
            return {
                'id': bakery.id,
                'name': bakery.name,
                'baked_goods': [{'id': good.id, 'name': good.name, 'price': good.price} for good in bakery.baked_goods]
            }
        return {'message': 'Bakery not found'}, 404

class BakedGoodsByPrice(Resource):
    def get(self):
        baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
        return [
            {
                'id': good.id,
                'name': good.name,
                'price': good.price,
                'bakery': {'id': good.bakery.id, 'name': good.bakery.name}
            }
            for good in baked_goods
        ]

class MostExpensiveBakedGood(Resource):
    def get(self):
        most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
        if most_expensive:
            return {
                'id': most_expensive.id,
                'name': most_expensive.name,
                'price': most_expensive.price,
                'bakery': {'id': most_expensive.bakery.id, 'name': most_expensive.bakery.name}
            }
        return {'message': 'No baked goods found'}, 404

api.add_resource(BakeryList, '/bakeries')
api.add_resource(BakeryById, '/bakeries/<int:id>')
api.add_resource(BakedGoodsByPrice, '/baked_goods/by_price')
api.add_resource(MostExpensiveBakedGood, '/baked_goods/most_expensive')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
