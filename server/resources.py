from flask_restful import Resource
from server.models import Bakery, BakedGood

class BakeryList(Resource):
    def get(self):
        # Fetch all bakeries from the database
        bakeries = Bakery.query.all()
        # Prepare the response data
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
        # Fetch a specific bakery by id
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
        # Fetch baked goods sorted by price in descending order
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
        # Fetch the most expensive baked good
        most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
        if most_expensive:
            return {
                'id': most_expensive.id,
                'name': most_expensive.name,
                'price': most_expensive.price,
                'bakery': {'id': most_expensive.bakery.id, 'name': most_expensive.bakery.name}
            }
        return {'message': 'No baked goods found'}, 404
