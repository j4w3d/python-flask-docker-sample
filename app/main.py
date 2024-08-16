import os
import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Get container-related information
    hostname = socket.gethostname()
    environment = dict(os.environ)
    
    # Filtered environment variables to display
    env_vars = {key: environment.get(key) for key in ["FLASK_APP", "HOME", "PATH"]}
    
    # Render the index.html template with the context
    return render_template('index.html', hostname=hostname, env_vars=env_vars)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
