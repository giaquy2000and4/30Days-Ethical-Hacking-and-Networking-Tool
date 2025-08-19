from flask import Flask, request, render_template_string, escape

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>XSS Test Page (Filtered)</title></head>
<body>
    <h2>XSS Test Form (Filtered)</h2>
    <form method="GET" action="/">
        <input type="text" name="q" placeholder="Type something">
        <input type="submit" value="Submit">
    </form>

    {% if query %}
    <h3>Server Response:</h3>
    <div>
        You entered (escaped): {{ query }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.values.get("q", "")
    # escape() để encode < > & " '
    return render_template_string(HTML_FORM, query=escape(query))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
