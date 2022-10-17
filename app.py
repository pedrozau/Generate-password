from flask import Flask, render_template
from random import sample 

app  = Flask(__name__) 

def generate_password():
    letter_lower = "abcdefghijklmnopqrstuvwxyz"
    letter_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = r"*$#!/=?"
    number = "0123456789"
    letter_join = letter_lower + letter_upper + symbols + number 
    password_length = 8 
    return "".join(sample(letter_join,password_length))
 
@app.route("/") 
def generate(): 
    password = generate_password()
    return render_template("index.html",password=password)   

    



    







