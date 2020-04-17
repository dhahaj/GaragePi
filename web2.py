from flask import Flask, render_template, request

app = Flask(__name__)

open=0

@app.route('/', methods=['GET', 'POST'])
def index():
        print('Garage is Opening/Closing')
        #return app.send_static_file('Question.html')
        return app.send_static_file('Open.html')

@app.route('/Garage', methods=['GET', 'POST'])
def Garage():
        name = request.form['garagecode']
        if name == '12345678':  # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
              open=1
              print("garagecode")
              return app.send_static_file('Open.html')

        if name != '12345678':  # 12345678 is the Password that Opens Garage Door (Code if Password is Incorrect)
                if name == "":
                        name = "NULL"
                return app.send_static_file('Question.html')
               # else:
                print('Incorrect code')
               #        print ("Garage is Open")
                return app.send_static_file('Open.html')

@app.route('/stylesheet.css')
def stylesheet():
        return app.send_static_file('stylesheet.css')

@app.route('/Log')
def logfile():
        return app.send_static_file('log.txt')

@app.route('/images/<picture>')
def images(picture):
        return app.send_static_file('images/' + picture)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)


