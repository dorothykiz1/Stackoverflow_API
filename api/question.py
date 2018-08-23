from flask import Flask,jsonify,request
from api.models import Question
app = Flask(__name__)

@app.route('/api/v1/questions',methods=['POST', 'GET'])
def questions():
    if request.method == "POST":
            description = str(request.data.get('description', ''))
            topic= str(request.data.get('topic', ''))
            post_date = str(request.data.get('post_date', ''))

            if description:
                question = Question(id=id,topic=topic,description=description,post_date=post_date)
                question.save()
                response = jsonify({
                    'id': question.id,
                    'description': question.description,
                    'topic': question.topic,
                    'post_date':post_date
                    
                })
                response.status_code = 201
                return response
    else:
        # GET all questions
        questions= Question.get_all()
        results = []

        for question in questions:
            q = {
                'id': question.id,
                'description': question.description,
                'topic': question.topic,
                'post_date':post_date
                    }
            
            results.append(q)
            
        response = jsonify(results)
        response.status_code = 200
        return response

    return app

if  __name__  == "__main__":
     app.run(debug=True)