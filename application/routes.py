from application import app, db
from application.models import Income

from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.forms import UserInputForm


# dispay the content of db in index 
@app.route('/')
def index():
    entries = Income.query.order_by(Income.date.desc()).all()
    return render_template('index.html' ,title = 'index', entries = entries)


# get data from user and add it to db ..
@app.route('/add', methods=['GET','POST'])
def add_expenses():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = Income(type= form.type.data, amount= form.amount.data,
                       category= form.category.data)
        
        db.create_all()
        db.session.add(entry)
        db.session.commit()
        flash('Successful entry', 'success')
        return redirect(url_for('index'))

    return render_template('add.html',title = 'add', form = form )


# delete from 
@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    try:
        entry = Income.query.get_or_404(int(entry_id))
        db.session.delete(entry)
        db.session.commit()
        flash('Deleting was successful', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Deleting failed: {str(e)}', 'error')
    finally:
        db.session.close()
    
    return redirect(url_for('index'))
