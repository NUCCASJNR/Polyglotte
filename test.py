# #!/usr/bin/python3
# from models.engine.storage import Storage
# from models.user import User
# from models.blog_post import BlogPost
# from models.engine.storage import Storage
#
# # Create an instance of the Storage class
# storage = Storage()
#
# # Call the reload method to create the tables
# storage.reload()
#
# # Access the session to perform database operations
# session = storage.session
#
# post = BlogPost(
# # Example: Create a new user
# user = User(name="John Doe", email="johndoe@example.com")
# session.add(user)
# session.commit()
#
# # Example: Query all users
# users = session.query(User).all()
# for user in users:
#     print(user.name)
#
# # Example: Delete a user
# user = session.query(User).first()
# session.delete(user)
# session.commit()
#
# # Close the session
# session.close()
#
