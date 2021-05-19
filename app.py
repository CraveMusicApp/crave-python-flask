import flask
from flask import request 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test', methods=['POST'])
def home():

    print(request.is_json)
    content = request.get_json(force=True)
    app.logger.info('hey')
    app.logger.info(content)
    return 'JSON posted'

app.run()