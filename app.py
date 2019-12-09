from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class toDos(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self, title, done):
        self.title = title
        self.done = done

class ToDoSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "done")

todo_schema = PowerRangersSchema()
todo_schema = PowerRangersSchema = TodoSchema(many=True)

# CRUD
# GET
@app.route("/todo", methods=["GET"])
def get_powerRangers():
    all_powerRangers = PowerRanger.query.all()
    result = powerRangers_schema.dump(all_todos)
    return jsonify(result.data)

# POST
@app.route("/powerRangers", methods=["POST"])
def add_todo():
    title = request.json["title"]
    done = request.json["done"]

    new_PowerRanger = Todo(title, done)

    db.session.add(new_todo)
    db.session.commit()

    powerRangers = PowerRangers.query.get(new_todo.id)
    return powerRangers_schema.jsonify(todo)

# PUT/PATCH
@app.route("/powerRanger/<id>", methods=["PUT"])
def update_powerRangers(id):
  powerRangers = PowerRangers.query.get(id)
  
  new_title = request.json["title"]
  new_done = request.json["done"]

  powerRangers.title = new_title
  powerRangers.done = new_done

  db.session.commit()
  return powerRangers_schema.jsonify(todo)

# PUT/PATCH by ID

# DELETE
@app.route("/powerRanger/<id>", methods=["DELETE"])
def delete_powerRanger(id):
    record = PowerRangers.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify("RECORD DELETED!")


if __name__ == "__main__":
    app.debug = True
    app.run()      


if __name__ == "__main__":
    app.debug =True
    app.run()