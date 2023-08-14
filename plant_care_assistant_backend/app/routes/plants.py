from flask import jsonify, request
from app.models import Plant
from app.schemas import PlantSchema
from app import db
from app.routes import plants_bp

plant_schema = PlantSchema()
plant_schema = PlantSchema(many=True)

# @plants_bp.route('/plants', methods=['GET'])
# def get_plants():
#     # Retrieve and return list of plants
#     plants = Plant.query.all()
#     serialized_plants = plant_schema.dump(plants)
#     return jsonify(serialized_plants)

# Quick Prototype
@plants_bp.route("/plants", methods=["GET"])
def get_plants():
    placeholder_plants = [
        {"id": 1, "name": "Placeholder Plant 1"},
        {"id": 2, "name": "Placeholder Plant 2"},
        {"id": 3, "name": "Placeholder Plant 3"},
    ]
    serialized_plants = plant_schema.dump(placeholder_plants)
    return jsonify({"plants": serialized_plants}), 200


@plants_bp.route("/plants/<int:plant_id>", methods=["GET"])
def get_plant(plant_id):
    # Retrieve and return details of a specific plant
    plant = Plant.query.get_or_404(plant_id)
    serialized_plant = plant_schema.dump(plant)
    return jsonify(serialized_plant)


# @plants_bp.route("/plants", methods=["POST"])
# def create_plant():
#     try:
#         data = request.get_json()
#         new_plant = Plant(name=data["name"], species=data["species"])
#         db.session.add(new_plant)
#         db.session.commit()
#         serialized_plant = plant_schema.dump(new_plant)
#         return jsonify(serialized_plant), 201
#     except Exception as e:
#         return jsonify(message="An error occurred"), 500
