from flask import Flask, url_for
import random
from logic import *

app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/")
def index():
    # Menggunakan url_for('nama_fungsi')
    return f'''
    <h1>Hai! di halaman ini, kamu dapat mempelajari beberapa fakta menarik tentang ketergantungan teknologi!</h1>
    <a href="{url_for('facts')}">View a random fact!</a>
    <br><br>
    <a href="{url_for('password')}">Generate your password!</a>
    <br><br>
    <a href="{url_for('emoji')}">Generate your Emoji!</a>
    <br><br>
    <a href="{url_for('flip')}">Flip your Coin!</a>
    '''

@app.route("/random_fact")
def facts():
    # Menggunakan url_for('index') untuk kembali ke halaman utama
    return f'''
    <p>{random.choice(facts_list)}</p>
    <br>
    <a href="{url_for('index')}">← Back to Home</a>
    '''

@app.route("/generate_password")
def password():
    # Menggunakan url_for('index') untuk kembali ke halaman utama
    return f'''
    <p>Your new Password: <strong>{gen_pass(10)}</strong></p>
    <br>
    <a href="{url_for('index')}">← Back to Home</a>
    '''
    
@app.route("/generate_emoji")
def emoji():
    # Menggunakan url_for('index') untuk kembali ke halaman utama
    return f'''
    <p>Your Emoji: <strong>{gen_emodji()}</strong></p>
    <br>
    <a href="{url_for('index')}">← Back to Home</a>
    '''
    
@app.route("/flip_coin")
def flip():
    # Menggunakan url_for('index') untuk kembali ke halaman utama
    return f'''
    <p>Your coin is : <strong>{flip_coin()}</strong></p>
    <br>
    <a href="{url_for('index')}">← Back to Home</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)
