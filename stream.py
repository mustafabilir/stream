import streamlink 
from flask import Flask
app = Flask(__name__)

@app.route("/<path:link>")
def generateLink(link):
	streams = streamlink.streams(link)
	return streams['best'].url
