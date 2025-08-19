from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>XSS Test Page (Stripped)</title></head>
<body>
    <h2>XSS Test Form (Stripped)</h2>
    <form method="GET" action="/">
        <input type="text" name="q" placeholder="Type something">
        <input type="submit" value="Submit">
    </form>

    {% if query %}
    <h3>Server Response:</h3>
    <div>
        You entered (stripped): {{ query }}
    </div>
    {% endif %}
</body>
</html>
"""

def strip_xss(value):
    # Loại bỏ các thẻ script, img, svg, iframe
    return re.sub(r"(?i)<(script|img|svg|iframe).*?>.*?</\1>", "", value)

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.values.get("q", "")
    safe_q = strip_xss(query)
    return render_template_string(HTML_FORM, query=safe_q)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002, debug=True)
