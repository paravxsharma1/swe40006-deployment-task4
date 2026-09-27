from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <h1>SWE40006 Task 4.3 - Distinction</h1>
    <p>Student: Parav Sharma (105321434)</p>
    <p>This is a custom web application deployed via Docker to a public cloud host.</p>
    <p>Server time: {datetime.now()}</p>
    <p><a href="/health">Health check endpoint</a></p>
    '''

@app.route('/health')
def health():
    return {"status": "ok", "task": "SWE40006 Task 4.3"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)