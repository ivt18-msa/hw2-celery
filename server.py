from os.path import join
from flask import Flask, render_template, request, redirect, url_for
from tasks import arhive_file

flask_app = Flask(__name__)


@flask_app.route("/")
def index_page():
    return render_template('index.html')


@flask_app.route('/result/<task_id>/')
def result_page(task_id):
    task = arhive_file.AsyncResult(task_id)
    return render_template('result.html', task=task)


@flask_app.route("/upload/", methods=['POST'])
def upload_page():
    if request.method == 'POST':
        file = request.files['file']
        filename = join('uploads', file.filename)
        file.save(filename)
        task = arhive_file.delay(filename)
        print(task.id)
    return redirect(url_for('index_page'))
