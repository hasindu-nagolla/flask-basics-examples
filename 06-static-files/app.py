from flask import Flask, send_from_directory, render_template, url_for
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    """Show available static files and links to view/download them."""
    static_dir = os.path.join(app.root_path, 'static')
    try:
        files = sorted(os.listdir(static_dir))
    except FileNotFoundError:
        files = []
    return render_template('index.html', files=files)


@app.route('/download/<path:filename>')
def download(filename):
    """Force download of a static file from the `static` folder."""
    return send_from_directory(os.path.join(app.root_path, 'static'), filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
