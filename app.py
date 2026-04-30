from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

cars = [
    {"name": "Swift", "price": 600000, "fuel": "Petrol"},
    {"name": "i20", "price": 800000, "fuel": "Petrol"},
    {"name": "Creta", "price": 1200000, "fuel": "Diesel"},
    {"name": "Nexon EV", "price": 1500000, "fuel": "Electric"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    budget = int(request.form.get('price', 1000000))
    fuel = request.form.get('fuel', 'Petrol')

    result = [c for c in cars if c['price'] <= budget and c['fuel'] == fuel]

    return render_template('results.html', cars=result)

if __name__ == '__main__':
    app.run(debug=True)