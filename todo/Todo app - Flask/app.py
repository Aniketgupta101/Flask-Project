from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    srno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.title}"

@app.route('/')
def hello_world():
    todo = Todo(title = "first todo", description = "start investing in stocks")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)
   # return 'Hello, World!'
   
@app.route('/show')
def products():
    allTodos = Todo.query.all()
    print(allTodos)
    return 'This is products'


if __name__ == "__main__":
    app.run(debug=True)