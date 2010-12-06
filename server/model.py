from google.appengine.ext import db
class Profile(db.Model):
    profile_id=db.StringProperty()
    profile_data=db.StringProperty()
    profile_date = db.DateTimeProperty(auto_now_add=True)

class User(db.Model):
    profile_id=db.StringProperty()
    profile_user=db.UserProperty()
