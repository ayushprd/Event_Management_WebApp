from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(800), nullable=False)
    date = db.Column(db.String(15), nullable=False)


    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        event_name = request.form['name']
        event_desc = request.form['desc']
        event_date = request.form['date']
        new_event = Todo(name=event_name, desc=event_desc, date=event_date)

     
        
			

        
        try:
            db.session.add(new_event)
            db.session.commit()

            return redirect('/')

        except:
            return 'there was an error'

    else:
       events = Todo.query.all()
        #rows = Todo.query.count()
       names = []
       descs = []
       dates = []
       for event in events:
           names.append(event.name)
           descs.append(event.desc)
           dates.append(event.date)

       

       d = {'event': [{'names': a, 'descs': t, 'dates': ds} for a, t, ds in zip(names, descs, dates)]}


       car = 5
       peter = Todo.query.filter_by(name='Kaalrarv').first()
       return render_template('Current.html', names=names, descs=descs, dates=dates, peter=peter) # ,events=events, rows=rows)


@app.route('/delete/<int:id>')
def delete(id):
    event_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(event_to_delete)
        db.session.commit()
        return redirect('/admin')
    except:
        return "there was a problem deleting that event"



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    event = Todo.query.get_or_404(id)

    if request.method == 'POST':
        event.name = request.form['name']
        event.desc = request.form['desc']
        event.date = request.form['date']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue updating"

    else:
        return render_template('update.html', event=event)




@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        event_name = request.form['name']
        event_desc = request.form['desc']
        event_date = request.form['date']
        new_event = Todo(name=event_name, desc=event_desc, date=event_date)

     
          
        try:
            db.session.add(new_event)
            db.session.commit()

            return redirect('/')

        except:
            return 'there was an error'

    else:
       events = Todo.query.all()
        #rows = Todo.query.count()
       names = []
       descs = []
       dates = []
       for event in events:
           names.append(event.name)
           descs.append(event.desc)
           dates.append(event.date)

       #return render_template('Current.html', names=names, descs=descs, dates=dates, peter=peter) # ,events=events, rows=rows)
       return render_template('admin.html', events=events) 



@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            return redirect('/admin')
    return render_template('login_page.html', error=error)

@app.route('/search', methods=['GET', 'POST'])
def searching():
    if request.method == 'POST':
        squery = request.form['ing']
        sanswer = Todo.query.filter_by(name=squery).first()
        
        return render_template('result.html', sanswer=sanswer)
    else:
        return render_template('search.html')










if __name__ == "__main__":
    app.run(debug=True)



