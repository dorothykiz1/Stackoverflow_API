from flask import Flask, json, request,Response

app = Flask(__name__)


class JsonResponse(Response):

def __init__(self,json_dict,status=200):
    super().__init__(response=json.dumps(json_dict),status=status,content_type="application/json")

@app.route("/api/v1/questions", methods=["GET"])
def get_questions():
     json = request.json
     resp = JsonResponse(json_dict=questions,status=200)
     return resp

# questions = [
#     {
#         "id": 1,
#         "topic": "AI",
#         "question": "What does Machine Learning mean?",
#         "answer": " Machine learning is the science of getting computers to act without being explicitly programmed",
#     },
#     {
#         "id": 2,
#         "topic": "Health",
#         "question": "How can i get a flat tummy in 10 days?",
#         "answer": "My friend that's not possible",
#     },
# ]
# # Get all questions in a list
# @app.route("/api/v1/questions", methods=["GET"])
# def get_questions():
#     return jsonify(questions)


# # Get a particular question considering indices
# @app.route("/api/v1/questions/<int:id>", methods=["GET"])
# def get_question(id):
#     return jsonify(questions[id]), 200


# # Post a question and returns a new list of Questions
# @app.route("/api/v1/questions", methods=["POST"])
# def post_question():
#     item = request.get_json()
#     questions.append(item)
#     return jsonify(questions), 201


# # Post an answer to a question identified by indices
# @app.route("/api/v1/questions/<int:id>/answers", methods=["POST"])
# def answer_question(id):
#     if len(questions) > 0:
#         for question in questions[id]:
#             answer = request.get_json()
#             (questions[id])['answer2'] = answer
#             return jsonify(questions), 201
#         return jsonify("Answered question"), 200
#     else:
#         return jsonify("Question index is out of range"), 504


# @app.route("/api/v1/questions/<int:id>", methods=["DELETE"])
# def delete_questions(id):
#     del questions[id]
#     return jsonify(questions), 200


# if __name__ == "__main__":
#     app.run(debug=True)
