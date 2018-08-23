class Question:
    questions=[]

    def __init__(self, id, description,topic,post_date):
        """initialize with id,description,topic,post_date"""
        self.id = id
        self.topic = topic
        self.description = description
        self.post_date = post_date

    def post(self):
        pass

    def save(self):
        pass
    @staticmethod
    def get_all():
        return Question.questions



class User(Question):
    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password

    def post(self):
        pass

    def answer(self):
        pass

    def upvote(self):
        pass

    def downvote(self):
        pass

    def like(self):
        pass


class Answer(Question):
    def __init__(self, id, topic, question, post_date):
        self.id = id
        self.topic = topic
        self.question = question
        self.post_date = post_date

    def post(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

