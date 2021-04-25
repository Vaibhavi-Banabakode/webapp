import flask
import flask_restful as fr
from imgtotext import ocr_core
from flask import Flask, render_template, make_response,request
from werkzeug import secure_filename
app=flask.Flask(__name__)
api=fr.Api(app)
class OCR(fr.Resource):
    def get(self):
        headers={'Content-Type':'text/html'}
        return make_response(render_template('ocr.html'),200,headers)
    def post(self):
        headers={'Content-Type':'text/html'}
        file=request.files['photo']
        file.save(secure_filename('test.jpg'))
        print(file)
        lang=request.form.get('languages')
        print(lang)
        ret=ocr_core("test.jpg",lang)
        print(ret)
        return make_response(render_template('ocr.html',prediction=ret),200,headers)
api.add_resource(OCR,"/ocrtrans")
if __name__ == "__main__":
    app.run(debug=True)