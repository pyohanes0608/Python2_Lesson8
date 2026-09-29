from flask import Flask
import random
from logic import *

app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/")
def index():
    # Menambahkan <br> agar link tidak menempel kesamping
    return f'''
    <h1>Hai! di halaman ini, kamu dapat mempelajari beberapa fakta menarik tentang ketergantungan teknologi!</h1>
    <a href="/random_fact">View a random fact!</a>
    <br><br>
    <a href="/generate_password">Generate your password!</a>
    <br><br>
    <a href="/generate_emoji">Generate your emoji!</a>
    <br><br>
    <a href="/flip_coin">Flip your coin!</a>
    '''

@app.route("/random_fact")
def facts():
    # Menambahkan tautan kembali ke "/"
    return f'''
    <p>{random.choice(facts_list)}</p>
    <br>
    <a href="/">← Back to Home</a>
    '''

@app.route("/generate_password")
def password():
    # Menambahkan tautan kembali ke "/"
    return f'''
    <p>Password baru kamu: <strong>{gen_pass(10)}</strong></p>
    <br>
    <a href="/">← Back to Home</a>
    '''
    
@app.route("/generate_emoji")
def emoji():
    # Menambahkan tautan kembali ke "/"
    return f'''
    <p>Emoji kamu: <strong>{gen_emodji()}</strong></p>
    <br>
    <a href="/">← Back to Home</a>
    '''
    
@app.route("/flip_coin")
def flip():
    # Menambahkan tautan kembali ke "/"
    return f'''
    <p>Koin kamu adalah : <strong>{flip_coin()}</strong></p>
    <br>
    <a href="/">← Back to Home</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)