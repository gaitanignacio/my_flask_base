from flask import Flask, render_template, request, jsonify
from flask_swagger import swagger
import socket

app = Flask(__name__)

@app.route("/")
def index():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return render_template('index.html', hostname=host_name, ip=host_ip)

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

@app.route("/bbox")
def summary():
    d = {'bbox': [0.1, 0.1, 1, 1.5], 'class': 'cat'}
    response = jsonify(d)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)