from flask import Flask, request, render_template_string

app = Flask(__name__)

# Trang web có form input, phản chiếu trực tiếp dữ liệu => dễ dính XSS
HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>XSS Test Page</title></head>
<body>
    <h2>XSS Test Form</h2>
    <form method="GET" action="/">
        <input type="text" name="q" placeholder="Type something">
        <input type="submit" value="Submit">
    </form>

    {% if query %}
    <h3>Server Response:</h3>
    <div>
        You entered: {{ query|safe }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.values.get("q", "")
    return render_template_string(HTML_FORM, query=query)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
