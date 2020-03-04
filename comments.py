from flask import Flask, request
app = Flask(__name__)

@app.route('/comments', methods=['POST'])
def post_response():
    if request.form:
        return request.form
    return request.get_json()
