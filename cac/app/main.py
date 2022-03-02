import socket
from datetime import datetime
from flask import Flask, send_from_directory, url_for, render_template


#-Build The App Object from Flask Class---------------------------
app = Flask(__name__, static_url_path='', static_folder='html', template_folder='html' )
# app.secret_key = "changeitxyz"
app.debug = True


#-The APP Request Handler Area-------------------------------------
@app.route('/', methods=["GET"])
def html_home_get():

  nowTs = datetime.now()
  nowTsStr = nowTs.strftime("%Y-%m-%d %H:%M:%S")
  curHostName = socket.gethostname()

  return render_template('index.html', nowTsStr=nowTsStr, curHostName=curHostName)

#-App Runner-------------------------------------------------------
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

#------------------------------------------------------------------