from flask import Flask, request, jsonify
from flask_swagger import swagger
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    login_user()
  elif request.method == 'GET':
    #serve login page
    serve_login_page()

@app.route('/user', methods=['GET','POST'])
def get_user():
  username = request.form['username']
  password = request.form['password']
  #login(arg,arg) is a function that tries to log in and returns true or false
  status = login(username, password)
  return status

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    Create a new user
    ---
    tags:
      - users
    definitions:
      - schema:
          id: Group
          properties:
            name:
              type: string
              description: the group's name
    parameters:
      - in: body
        name: body
        schema:
          id: User
          required:
            - email
            - name
          properties:
            email:
              type: string
              description: email for user
            name:
              type: string
              description: name for user
            address:
              description: address for user
              schema:
                id: Address
                properties:
                  street:
                    type: string
                  state:
                    type: string
                  country:
                    type: string
                  postalcode:
                    type: string
            groups:
              type: array
              description: list of groups
              items:
                $ref: "#/definitions/Group"
    responses:
      201:
        description: User created
    """
    if request.method == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('/var/www/uploads/profilephoto.png')


@app.route("/spec")
def spec():
    return jsonify(swagger(app))