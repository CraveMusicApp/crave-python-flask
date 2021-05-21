import flask
from flask import request 
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/user', methods=['POST'])
def postUser():
    print(request.is_json)
    content = request.get_json(force=True)
    app.logger.info(content)
    full_name = content['user_name'];
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    app.logger.info(first_name)
    app.logger.info(last_name)

    connection = sqlite3.connect(currentdirectory +'\cravedb.db')
    cursor = connection.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS craveUser(first_name TEXT,last_name TEXT)")
    connection.commit()
    cursor.execute("INSERT INTO craveUser VALUES('%(first_name)s','%(last_name)s')")
    connection.commit()
    cursor.close()
    return 'JSON posted'


@app.route('/songData', methods=['POST'])
def updateLikeStatus():
    #print(request.is_json)
    content = request.get_json(force=True)
    app.logger.info(content)
    print(content)
    likeJson = content['likeStatus']
    likeStatus = ''
    if likeJson == True:
        likeStatus = 'True'
    else:
        likeStatus ='False'
    songName = content['songName']
    songGenre = content['songGenre']
    connection = sqlite3.connect(currentdirectory +'\cravedb.db')
    cursor = connection.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS SongsCraves(song_name TEXT,song_genre TEXT,song_like TEXT)")
    connection.commit()
    cursor.execute("INSERT INTO SongsCraves VALUES('%(songName)s','%(songGenre)s','%(likeStatus)s')",(songName,songGenre,likeStatus))
    connection.commit()
    cursor.close()
    return 'JSON posted'


@app.route('/retrieveData',methods=['Get'])
def getSongData():
    connection = sqlite3.connect(currentdirectory +'\cravedb.db')
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM SongsCrave")
    return data
app.run()

