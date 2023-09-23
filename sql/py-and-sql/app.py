from flask import Flask, jsonify, abort, request, make_response
from flaskext.mysql import MySQL
from flask_cors import CORS

# Create an object named app
app = Flask(__name__)
CORS(app)

# Configure mysql database
app.config["MYSQL_DATABASE_HOST"] = "cpew.chzveui56egk.us-east-1.rds.amazonaws.com"
app.config["MYSQL_DATABASE_USER"] = "admin"
app.config["MYSQL_DATABASE_PASSWORD"] = "NvFGNEym64pBZqn"
app.config["MYSQL_DATABASE_DB"] = "cars"
app.config["MYSQL_DATABASE_PORT"] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()


# Write a function named `get_all_cars` which gets all cars from the cars table in the db,
# and return result as list of dictionary
def get_all_cars():
    query = """
    SELECT * FROM car;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cars = [
        {
            "car_id": row[0],
            "number_of_owners": row[1],
            "registration_number": row[2],
            "manufacture_year": row[3],
            "number_of_doors": row[4],
            "car_model_id": row[5],
            "mileage": row[6],
        }
        for row in result
    ]
    return cars


# Write a function named `get_cars` which returns all cars in JSON format for `GET`,
# and assign to the static route of ('/cars')
@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify({"cars": get_all_cars()})


# Write a function named `get_all_cars` which gets all cars from the cars table in the db,
# and return result as list of dictionary
def find_car(car_id):
    query = f"""
    SELECT * FROM car WHERE car_id={car_id};
    """
    cursor.execute(query)
    row = cursor.fetchone()
    car = None
    if row is not None:
        car = {
            "car_id": row[0],
            "number_of_owners": row[1],
            "registration_number": row[2],
            "manufacture_year": row[3],
            "number_of_doors": row[4],
            "car_model_id": row[5],
            "mileage": row[6],
        }
    return car


# function to remove a car from the database
def remove_car(car_id):
    delete = f"""
    DELETE FROM car WHERE car_id={car_id};
    """
    cursor.execute(delete)
    connection.commit()  # Make sure to commit the changes to the database
    return jsonify({"message": "Car removed successfully"})


# Write a function named `get_cars` which returns all cars in JSON format for `GET`,
# and assign to the static route of ('/cars')
@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car = find_car(car_id)
    if car == None:
        abort(404)
    return jsonify({"car found": car})


# routing to delete a car entry
@app.route("/cars/del/<int:car_id>", methods=["GET", "DELETE"])
def del_car(car_id):
    car = find_car(car_id)
    if car is None:
        abort(404)
    result = remove_car(car_id)
    if result:
        return jsonify({"message": "Car removed successfully"})
    else:
        return jsonify({"message": "Failed to remove car"}), 500


# Write a function named `home` which returns 'Welcome to the To-Do API Service',
# and assign to the static route of ('/')
@app.route("/")
def home():
    return "Welcome to car API Service"


# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=9876)
