""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):

        return self.db.query_db("SELECT * FROM courses")

    def get_course_info(self, id):
        query = "SELECT * FROM courses WHERE id=%s"
        info = [id]
        return self.db.query_db(query, info)

    def remove_course(self, id):
        query = "DELETE FROM courses WHERE id=%s"
        info = [id]
        self.db.query_db(query, info)

    def add_course(self, course_info):
        query = "INSERT INTO courses (name, description, created_at, updated_at) VALUES(%s, %s, NOW(), NOW())"
        info = [course_info['name'], course_info['description']]
        self.db.query_db(query, info)



    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """
