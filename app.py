from flask import Flask, render_template

app = Flask(__name__)

# Mock Data
group_name = "Theoretical Computer Science"
school_name = "School of Computing & Communications"

latest_news = [
    {"date": "2026-01-10", "title": "New Paper Accepted", "content": "Our work on Quantum distributed algorithms was accepted at STOC 2026."},
    {"date": "2025-12-20", "title": "Winter Workshop", "content": "Join us for our upcoming workshop on Categorical Semantics."},
]

research_themes = [
    {
        "name": "Logic, Semantics and Computation",
        "description": "Investigating models and calculi for fundamental computation.",
        "points": [
            "Model theory for non-classical logics such as spatial, temporal or description logics",
            "Calculi for formal deduction and automated reasoning",
            "Categorical semantics for algebraic composition",
            "Models of high-level computation",
            "Knowledge representation",
            "Mechanisation of proofs and logical operations"
        ],
        "members": ["Dr Marco Caminati", "Dr Fabio Papacchini"]
    },
    {
        "name": "Formal Methods",
        "description": "Establishing rigorous foundations for system verification.",
        "points": [
            "Automated theorem proving",
            "Synthesis and correctness-by-construction",
            "Verification of hybrid and autonomous systems",
            "Languages and frameworks for the formal specification of software systems",
            "Proof assistants and constraint solvers for certified solutions in safety-critical domains"
        ],
        "members": ["Dr Damian Arellanes", "Dr Andrew Sogokon"]
    },
    {
        "name": "Design and Analysis of Algorithms",
        "description": "Developing efficient algorithms for complex challenges.",
        "points": [
            "Graph algorithms",
            "Approximation algorithms",
            "Quantum distributed algorithms"
        ],
        "members": ["Dr Fabien Dufoulon", "Dr Pascal Welke"]
    }
]

people = [
    {"name": "Dr Damian Arellanes", "email": "damian.arellanes@lancaster.ac.uk", "theme": "Formal Methods", "image": "Damian.jpg"},
    {"name": "Dr Marco Caminati", "email": "m.caminati@lancaster.ac.uk", "theme": "Logic, Semantics and Computation", "image": "Marco.jpg"},
    {"name": "Dr Fabien Dufoulon", "email": "f.dufoulon@lancaster.ac.uk", "theme": "Design and Analysis of Algorithms", "image": "Fabien.jpg"},
    {"name": "Dr Fabio Papacchini", "email": "f.papacchini@lancaster.ac.uk", "theme": "Logic, Semantics and Computation", "image": "Fabio.jpg"},
    {"name": "Dr Andrew Sogokon", "email": "a.sogokon@lancaster.ac.uk", "theme": "Formal Methods", "image": "Andrew.jpg"},
    {"name": "Dr Pascal Welke", "email": "p.welke@lancaster.ac.uk", "theme": "Design and Analysis of Algorithms", "image": "Pascal.jpg"},
]

seminars = [
    {
        "type": "Upcoming",
        "time": "14:00",
        "date": "2026-02-14",
        "speaker": "Dr. Grace Hopper",
        "location": "Room 101",
        "title": "The Future of Compilers",
        "abstract": "A deep dive into optimization techniques."
    },
    {
        "type": "Previous",
        "time": "10:00",
        "date": "2025-11-05",
        "speaker": "Prof. Alan Turing",
        "location": "Auditorium A",
        "title": "Computing Machinery",
        "abstract": "Can machines think? We discuss the imitation game."
    }
]

@app.context_processor
def inject_global_vars():
    return dict(group_name=group_name, school_name=school_name)

@app.route('/')
def home():
    return render_template('home.html', news=latest_news)

@app.route('/people')
def show_people():
    return render_template('people.html', people=people)

@app.route('/research')
def research():
    return render_template('research.html', themes=research_themes)

@app.route('/seminars')
def show_seminars():
    return render_template('seminars.html', seminars=seminars)

@app.route('/opportunities')
def opportunities():
    return render_template('opportunities.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
