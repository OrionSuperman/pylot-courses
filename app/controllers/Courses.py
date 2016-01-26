"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('Course')
    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses=courses)

    def create(self):
        if len(request.form['name']) > 15:
            course_info = request.form
            self.models['Course'].add_course(course_info)
        else:
            flash('Name must be at least 15 characters')
        return redirect('/')

    def doublecheck(self, id):
        course_info = self.models['Course'].get_course_info(id)
        course_info = course_info[0]
        return self.load_view('confirm.html', course_info=course_info)

    def destroy(self):
        print request.form['id']
        id = request.form['id']
        self.models['Course'].remove_course(id)
        return redirect('/')