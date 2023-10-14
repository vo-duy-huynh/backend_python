from flask import Flask, request, jsonify
import face_recognition
import cv2, sys, os
import werkzeug
uploaded_filename = ""
app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_filename
    if request.method == 'POST':
        file = request.files['image']
        filename = werkzeug.utils.secure_filename(file.filename)
        file.save("./upload/"+filename)
        main_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        uploaded_filename = main_script_dir + "/upload/" + filename

        return jsonify({"message": "Upload successfully"})
@app.route('/number_faces', methods=['GET'])
def number_faces():
    if request.method == 'GET':
        path_image = request.args.get('filename')
        print(path_image)
        image = face_recognition.load_image_file(uploaded_filename)
        face_locations = face_recognition.face_locations(image)
        image = cv2.imread(uploaded_filename)
        for loc in face_locations:
            top, right, bottom, left = loc
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow("Detected Faces", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return jsonify({"number": str(len(face_locations))})
        

if __name__ == '__main__':
    app.run(debug=True, port=5000)
