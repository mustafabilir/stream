import os
import streamlink 
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/<path:link>")
def generateLink(link):
	streams = streamlink.streams(link)
	return streams['best'].url

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.environ['PORT'])
