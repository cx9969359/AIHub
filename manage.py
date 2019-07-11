from flask import render_template
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

from core import create_app
from core.model import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')

if __name__ == '__main__':
    manager.run()




