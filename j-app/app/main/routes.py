from datetime import datetime
from flask import render_template, request, current_app, redirect, url_for, flash, g
from app.main import bp
import tempfile
import os


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')


@bp.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html')


def write_script_to_tempfile(script):
    """
    return filename for tempfile
    """
    with tempfile.NamedTemporaryFile(dir='/tmp', delete=False) as tmpfile:
        filename = tmpfile.name

    with open(filename, 'w') as f:
        f.write("from subprocess import Popen, PIPE\n")
        f.write("p = Popen(\"jconsole\", stdin=PIPE)\n")
        code = f'p.communicate("'
        for line in script.splitlines():
            code += f"{line}\\n"
        code += f'".encode())\n'
        f.write(code)
    return filename


@bp.route('/run_script', methods=['GET', 'POST'])
def run_script():
    data = request.json
    script = data["script"]

    filename = write_script_to_tempfile(script)
    out_filename = f"{filename}_out"
    os.system(f"python {filename} > {out_filename}")

    with open(out_filename) as f:
        data = f.read()
        return data

    return "No output"
