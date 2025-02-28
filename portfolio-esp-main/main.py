# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    button_instagram = request.form.get('button_instagram')
    button_twitter = request.form.get('button_twitter')
    button_facebook = request.form.get('button_facebook')

    return render_template('index.html', button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,
                           button_instagram=button_instagram,
                           button_twitter=button_twitter,
                           button_facebook=button_facebook
                           )
    

#Comentarios
@app.route('/Coment', methods=['POST'])
def coment_form():
    email = request.form['email']
    text = request.form['text']

    with open('grd.txt', 'a') as file:
        file.write(f'{email}, {text}\n')

    return render_template('coment.html',
                           email=email,
                           text=text)






if __name__ == "__main__":
    app.run(debug=True)
