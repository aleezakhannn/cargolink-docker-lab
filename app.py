from flask import Flask, render_template_string
import csv

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>CargoLink IT Asset Lab</title></head>
<body>
    <h1>CargoLink IT Asset Inventory</h1>
    <table border="1" cellpadding="8">
        <tr>
            {% for header in headers %}<th>{{ header }}</th>{% endfor %}
        </tr>
        {% for row in rows %}
        <tr>
            {% for cell in row %}<td>{{ cell }}</td>{% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    with open("assets.csv") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    return render_template_string(TEMPLATE, headers=headers, rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)