# pip install flask
"""
Python for web development

We have many web frameworks in python

- bottle framework
- flask framework # POPULAR
- django framework # POPULAR
- fastapi framework # Was getting popularity
Many More
"""

"""
We will discuss
flask framework
"""

"""
1) Using flask framework we can develop websites
2) Using flask framework we can develop RESTAPI & Micro services
"""

"""
In our training,
We will discuss, 
How to flask framework for developing REST-API
"""

"""
To run any web application, we need
1) web server: flask has builtin web server that we can use it for DEVELOPMENT
2) database: SQLite
3) web browser
"""

"""
Suppose, we want to provide access to our database with others/public
then how to provide?
One way is, we can share complete credentials like username/password/host-ip etc

This will not work, we can't provide all credentials
"""

"""
We got 2 solutions to provide access
1) SOAP: Simple Object Access Protocol
2) REST: REpresentational State Transfer

both will tell how to provide access
both we can call styles/designs/architecture

both tells provide some INTERFACE between your application with others
both also tells how to write/develop such INTERFACE

our-app/our-db  <-- INTERFACE -->  others/public

This INTERFACE is also called APPLICATION PROGRAMMING INTERFACE (API)
SOAP-API
REST-API
"""

"""
REST came after SOAP
REST is easy to implement
REST is popular

Since flask is already implemented REST-ARCHITECTURE, 
we need to worry about implmenting REST architecture,
we just need to know how to create REST-API using flask
"""

# ----------
# Create App
############
import flask
# my_rest_api_app = flask.Flask("AnyName")
my_rest_api_app = flask.Flask(__name__) # __name__ = '__main__' : Builtin variable
##############################


# ----------
# REST API END POINT: Internally this URL http://127.0.0.1:5000/getlogdata mapped to route("/")
############
@my_rest_api_app.route("/getlogdata", methods=["GET"])
def my_log_db_api():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result) # Convert to json and return
##############################


# HTTP METHODS
# GET -> If end user is asking data (Reading)
# POST -> If end user is asking to create new record
# PUT -> If end user is asking to update record
# PATCH -> If end user is asking to update only phone number & all details
# DELETE -> If end user is asking to delete record

# ----------
# Run builtin server
############
my_rest_api_app.run()
##############################

# Access this API using http://127.0.0.1:5000/getlogdata