
from flask import Flask, render_template, redirect, url_for, current_app, send_file
from flask_simplelogin import SimpleLogin
from flask_simplelogin import login_required
from werkzeug.urls import url_quote
from flask_bootstrap import Bootstrap
from flask_apscheduler import APScheduler
import time, os, subprocess

def run_backup(hostname, username, password, database, working_dir):
    try:
        timestamp = str(int(time.time()))
        p = subprocess.Popen("mysqldump -h" + hostname + " -u" + username + " -p'" + password + "' " + database + " > dump_" + hostname + "_" + database + "_" + timestamp + ".sql", shell=True, cwd=working_dir)
        output, err = p.communicate()
        if(p.returncode != 0):
            raise Exception("return code: {}, output: {}, error: {}".format(p.returncode, output if output else '', err if err else ''))
        print("{} backup done ".format(database))
    except Exception as e:
        print("{} backup failed. exception:\r\n{}".format(database, e))

def run_restore(hostname, username, password, database, working_dir, backup_file):
    try:
        timestamp = str(int(time.time()))
        p = subprocess.Popen("mysql -h" + hostname + " -u" + username + " -p'" + password + "' " + database + " < " + backup_file, shell=True, cwd=working_dir)
        output, err = p.communicate()
        if(p.returncode != 0):
            raise Exception("return code: {}, output: {}, error: {}".format(p.returncode, output if output else '', err if err else ''))
        print("{} restore done ".format(database))
    except Exception as e:
        print("{} restore failed. exception:\r\n{}".format(database, e))

def delete_file(backup_root, backup_file):
    try:
        os.remove(os.path.join(backup_root, backup_file))
        print("{} delete done ".format(backup_file))
    except OSError as e:
        print("{} delete failed. exception:\r\n{}".format(backup_file, e))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something-secret'
    HOSTNAME = os.environ.get('HOST') or 'mysql'
    USERNAME = os.environ.get('USERNAME') or 'root'
    PASSWORD = os.environ.get('PASSWORD') or 'abc123'
    SIMPLELOGIN_USERNAME = os.environ.get('USERNAME') or 'root'
    SIMPLELOGIN_PASSWORD = os.environ.get('PASSWORD') or 'abc123'
    DATABASE = os.environ.get('DATABASE') or 'mydb'
    BACKUP_DIR = os.environ.get('BACKUP_DIR') or './backup'
    HOUR = os.environ.get('HOUR') or '00'
    MINUTE = os.environ.get('MINUTE') or '00'
    JOBS = [
        {
            'id': 'runbackup',
            'func': run_backup,
            'args': (HOSTNAME, USERNAME, PASSWORD, DATABASE, BACKUP_DIR),
            'trigger': 'cron',
            'hour': HOUR,
            'minute': MINUTE
        }
    ]
    
    SCHEDULER_API_ENABLED = True

if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    backup_root = app.config['BACKUP_DIR']
    os.makedirs(backup_root, exist_ok=True)
    Bootstrap(app)
    
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    SimpleLogin(app)

    @app.route('/')
    @login_required
    def index():
        backup_files = []
        for f in os.listdir(backup_root): 
            if f.endswith('sql'):
                size = os.path.getsize(os.path.join(backup_root, f))
                t = os.path.getmtime(os.path.join(backup_root, f))
                bk_file = {'file_name': f,
                           'file_size': size,
                           'create_time': t}
                backup_files.append(bk_file)
        return render_template('index.html', backup_files=backup_files)

    @app.route('/delete/<backup_file>')
    @login_required
    def delete(backup_file):
        delete_file(app.config['BACKUP_DIR'], backup_file)
        return redirect(url_for('index'))
    
    @app.route('/backup')
    @login_required
    def backup():
        run_backup(app.config['HOSTNAME'], app.config['USERNAME'], app.config['PASSWORD'], app.config['DATABASE'], app.config['BACKUP_DIR'])
        return redirect(url_for('index'))

    @app.route('/restore/<backup_file>')
    @login_required
    def restore(backup_file):
        run_restore(app.config['HOSTNAME'], app.config['USERNAME'], app.config['PASSWORD'], app.config['DATABASE'], app.config['BACKUP_DIR'], backup_file)
        return redirect(url_for('index'))

    @app.route('/download/<backup_file>')
    @login_required
    def download(backup_file):
        action = send_file(os.path.join(app.config['BACKUP_DIR'], backup_file), attachment_filename=backup_file, as_attachment=True)
        action = current_app.make_response(action)
        action.headers["Content-Disposition"] = \
            "attachment;" \
            "filename*=UTF-8''{utf_filename}".format(
                utf_filename=url_quote(backup_file.encode('utf-8'))
            )
        response = current_app.make_response(action)
        return response

    app.run(host='0.0.0.0')
