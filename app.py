from flask import Flask, render_template, request, redirect, url_for
from geocoder import geocode
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        adress = request.form['adress']
        geocode_result = geocode(adress)
        if geocode_result:
            information = json.dumps({
                'toponym_address': geocode_result[0],
                'toponym_coordinates': geocode_result[1],
                'country': geocode_result[2],
                'province': geocode_result[3],
                'area': geocode_result[4],
                'locality': geocode_result[5],
                'street': geocode_result[6],
                'house': geocode_result[7],
                'image': geocode_result[8]  # Путь к изображению
            })
            return redirect(url_for('result', adress=adress, information=information))
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    adress = request.args.get('adress')
    information = request.args.get('information')
    geocode_data = json.loads(information) if information else {}

    if request.method == "POST":
        return redirect(url_for('index'))

    return render_template('result.html', adress=adress, geocode_data=geocode_data)

if __name__ == '__main__':
    app.run(debug=True)