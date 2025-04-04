#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, user_schema, users_schema


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Users(Resource):

    def get(self):

        users = User.query.all()
        response = users_schema.dump(users), 200
        return response
    
    def post(self):
        try:
            data = request.get_json()
            user = User(
                username = data['username'],
                email = data['email'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                profile_pic = data['profile_pic']
            )
            user.password_hash = data['password']
            db.session.add(user)
            db.session.commit()
            response = make_response(user_schema.dump(user), 201)
            return response
        except Exception as e:
            response_body = {'errors': [str(e)]}
            return response_body, 400
    
api.add_resource(Users,'/users')

class UsersByID(Resource):

    def get(self, id):
        user = User.query.filter_by(id=id).first()
        response = make_response(user_schema.dump(user), 200)
        return response

    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()
        if user:
            if 'password' in data:
                user.password_hash = data['password']
            for attr, value, in data.items():
                setattr(user, attr, value)
            db.session.add(user)
            db.session.commit()
            response = make_response(user_schema.dump(user), 202)
            return response
        else:
            response_body = {'error': 'User not found'}
            return response_body, 404
        
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response_body= ''
            return response_body, 204
        else: 
            response_body = {'error': 'User not found'}
            return response_body, 404



api.add_resource(UsersByID,'/users/<int:id>')

class SignUp(Resource):

    def post(self):
        try:
            data = request.get_json()
            user = User(
                username = data['username'],
                email = data['email'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                profile_pic = data['profile_pic']
            )
            user.password_hash = data['password']
            db.session.add(user)
            db.session.commit()
            response = make_response(
                user_schema.dump(user), 201)
            return response
        except:
            response_body = {'errors': ['validation errors']}
            return response_body, 400

api.add_resource(SignUp, '/signup')

class CheckSession(Resource):

    def get(self):
        print("CheckSession endpoint was hit")
        user_id = session.get('user_id')
        print(f"Session: {user_id}")
        if user_id:
               user = User.query.filter(User.id == user_id).first()
               response = make_response(user_schema.dump(user), 200)
               return response
        else:
            # Return a response that can be safely parsed as JSON
            response_body = {"message": "No active session", "session": None}
            response = make_response(response_body, 404)
            return response

api.add_resource(CheckSession, '/checksession')

class Login(Resource):

    def post(self):

        username = request.get_json().get('username')
        user = User.query.filter(User.username == username).first()

        password = request.get_json()['password']

        if user.authenticate(password):
            session['user_id'] = user.id
            response = make_response(
                user_schema.dump(user), 200)
            return response
        else:
            response_body = {'error': 'Invalid username and password'}
            return response_body, 401
        
api.add_resource(Login, '/login')

class Logout(Resource):

    def delete(self):

        session['user_id'] = None
        return {}, 204
    
api.add_resource(Logout, '/logout')


if __name__ == '__main__':
    # app.run(port=5555, debug=True)
    app.run(debug=True)


