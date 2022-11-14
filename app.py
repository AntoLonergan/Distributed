from flask import Flask, Response, render_template
from flask_socketio import SocketIO
from camera import Video

app=Flask(__name__)
socketioApp = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')
        
@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

def run():
    socketioApp.run(app)

if __name__ == '__main__':
    socketioApp.run(app)