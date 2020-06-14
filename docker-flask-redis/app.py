from flask import Flask,render_template,jsonify,request
import redis
import sys
import random
import json
#This list stores all values of meanings when we enter on browser

app=Flask(__name__)

@app.route('/')
def index():
    return '''<html>
    <b>This is a Flask Api Framework retrieves data in memory from redis</b>
    <p><b>Try these in URL</b>: SAMPLE INPUT </p>
    <p>/add_word/word=foo </p>
    <p>/add_word/word=example </p>
    <p>/add_word/word=foobar </p>
    <p>/add_word/word=exam </p>
    <p></p>
    <p>Get all Words List Entered</p>
    <p>/wordslist</p>
    <p></p>
    <p>SAMPLE OUTPUT </p>
    <p>/autocomplete/query=fo</p>
    [
        "foo",
        "foobar"
    ]
    
    </html>'''


@app.route('/add_word/word=<string:word>',methods=['POST','GET'])
def add_word(word):
    redisdb = redis.StrictRedis(host='redis', port=6379, db=0)
    id=random.randint(0,1000)
    redisdb.set(word,id)
    return json.dumps(word)
    
    
@app.route('/autocomplete/query=<string:word>')
def autocomplete(word):
    redisdb = redis.StrictRedis(host='redis', port=6379, db=0)
    wordslist=[]
    for key in redisdb.keys(pattern=word+"*"):
        wordslist.append(key.decode())
    return json.dumps(wordslist)

@app.route('/wordslist')
def wordslist():
    redisdb = redis.StrictRedis(host='redis', port=6379, db=0)
    items=[]
    for i in redisdb.keys(pattern="*"):
        items.append(i.decode())
    return json.dumps(items)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)
