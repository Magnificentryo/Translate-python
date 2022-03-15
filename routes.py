
# -*- coding: utf-8 -*-

import secrets
from App import app
from flask import redirect, render_template, request , url_for, session
import os
import cv2 
from App import utils
import pytesseract
from App.forms import MyForm
import numpy as np

@app.route("/")
def index():
    return render_template("index.html", title = "Home Page")
    



@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST": 
        sentence = "  "
        f = request.files.get("file")
        filename, extension = f.filename.split(".")
        generated_filename = secrets.token_hex(20) +f".{extension}"
        
        file_location = os.path.join(app.config["UPLOADED_PATH"], generated_filename)
       
        f.save(file_location)
        pytesseract.pytesseract.tesseract_cmd = r'/Users/joeth/AppData/Local/tesseract.exe'
        img = cv2.imread(file_location)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
       
        boxes = pytesseract.image_to_data(img) 
        for i, box in enumerate(boxes.splitlines()):
           if i ==0: 
              continue
           box = box.split()
        
           if len(box) ==12: 
            sentence += box[11] + "  "

       # print(sentence)
        session["sentence" ] =sentence

        os.remove(file_location)
        






        return redirect("/decoded/")



    
    
    else: 
     return render_template("upload.html", title="Upload")


@app.route("/decoded", methods=["POST","GET"])
def decoded():

  sentence = session.get("sentence")
  
  form = MyForm()
 
  if request.method == "POST": 
            text_data = form.text_field.data
            translate_to = form.language_field.data
            #print("Translate to: ", translate_to)

            translated_text = utils.tranlate_text(text_data,translate_to)
            #print(translated_text)
            form.text_field.data = translated_text
            return render_template("decoded.html", form = form )
  else:
      form.text_field.data = sentence
      session["sentence"] =""
    
    
  
      return render_template("decoded.html", form = form )