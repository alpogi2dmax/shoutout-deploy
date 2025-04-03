from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt, ma

# Models go here!
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    profile_pic = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    username = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    profile_pic = ma.auto_field()
    # comments = ma.Nested( lambda: CommentSchema, many=True, only=('id', 'comment', 'created_date', 'commenter', 'replies', 'likes'))
    # comments = ma.Method("get_comments")
    # replies = ma.Nested(lambda: ReplySchema, many=True, only=('id', 'reply', 'created_date', 'replier', 'comment'))
    # replies = ma.Method("get_replies")
    # followers = ma.Nested(lambda: UserSchema, many=True, only=('id', 'first_name', 'last_name', 'profile_pic', 'username'))
    # followed = ma.Nested(lambda: UserSchema, many=True, only=('id', 'first_name', 'last_name', 'profile_pic', 'username'))
    # search_string = ma.Method('get_search_string')

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "usersbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

    # def get_comments(self, user):
    #     comments = user.comments
    #     comments_schema = CommentSchema(many=True)
    #     # Use sorted with reverse=True to sort in descending order
    #     sorted_comments = sorted(comments, key=lambda x: x.created_date, reverse=True)
    #     comment_data = comments_schema.dump(sorted_comments)
    #     return comment_data

    # def get_replies(self, user):
    #     replies = user.replies
    #     replies_schema = ReplySchema(many=True)
    #     # Use sorted with reverse=True to sort in descending order
    #     sorted_replies = sorted(replies, key=lambda x: x.created_date, reverse=True)
    #     reply_data = replies_schema.dump(sorted_replies)
    #     return reply_data
    
    # def get_search_string(self, user):
    #     # Concatenate the fields into a single search string
    #     return f"{user.username} {user.email} {user.first_name} {user.last_name}".lower()


user_schema = UserSchema()
users_schema = UserSchema(many=True)