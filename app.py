import flask
from flask import request 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/user', methods=['POST'])
def postUser():

    print(request.is_json)
    content = request.get_json(force=True)
    app.logger.info('hey')
    app.logger.info(content)
    return 'JSON posted'

@app.route('/songData', methods=['POST'])
def updateLikeStatus():

    print(request.is_json)
    content = request.get_json(force=True)
    app.logger.info('hey')
    app.logger.info(content)
    return 'JSON posted'

app.run()