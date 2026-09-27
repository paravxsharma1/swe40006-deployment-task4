from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>SWE40006 Task 4.2 - Flask in Docker</h1>
    <p>Student: Parav Sharma (105321434)</p>
    <p>This page is being served from inside a Docker container.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)