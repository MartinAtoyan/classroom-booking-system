import os
from quart import Quart, jsonify, request
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv



load_dotenv()
MONGO_URI = os.environ.get("MONGO_URI")

app = Quart(__name__)

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("students")

@app.route("/students", methods=["POST"])
async def add_student():
    data = await request.get_json()
    result = await db.students.insert_one(data)
    return jsonify({"message": "Student created", "id": str(result.inserted_id)}), 201

@app.route("/students", methods=["GET"])
async def get_students():
    students_cursor = db.students.find()
    students = [student async for student in students_cursor]

    for student in students:
        student["_id"] = str(student["_id"])

    return jsonify(students), 200

if __name__ == "__main__":
    app.run()
