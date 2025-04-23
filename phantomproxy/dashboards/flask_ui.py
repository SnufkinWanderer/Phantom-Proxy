from flask import Flask, render_template_string

app = Flask(__name__)
LOG_BUFFER = []

TEMPLATE = """
<html><head><title>Phantom Logs</title></head><body>
<h2>Live Logs</h2><pre>{{ logs }}</pre>
<script>setTimeout(()=>location.reload(), 3000);</script>
</body></html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, logs="\n".join(LOG_BUFFER[-50:]))

def start_dashboard():
    app.run(host="0.0.0.0", port=5000)