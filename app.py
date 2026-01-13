from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_data():
    """Loads data from the JSON file."""
    filename = os.path.join(app.root_path, 'data.json')
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Handle case where file is missing

@app.context_processor
def inject_global_vars():
    data = load_data()
    return dict(group_name=data.get('group_name', 'Research Group'), 
                school_name=data.get('school_name', 'University School'))

@app.route('/')
def home():
    data = load_data()
    return render_template('home.html', news=data.get('latest_news', []))

@app.route('/people')
def show_people():
    data = load_data()
    return render_template('people.html', people=data.get('people', []))

@app.route('/research')
def research():
    data = load_data()
    return render_template('research.html', themes=data.get('research_themes', []))

@app.route('/seminars')
def show_seminars():
    data = load_data()
    return render_template('seminars.html', seminars=data.get('seminars', []))

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)