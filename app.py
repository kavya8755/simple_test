from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<title>Add Two Numbers</title>
<h2>Add Two Numbers</h2>
<form method="POST" action="/">
  Number 1: <input type="number" name="num1" required><br><br>
  Number 2: <input type="number" name="num2" required><br><br>
  <input type="submit" value="Add">
</form>
{% if result is not none %}
  <h3>Result: {{ result }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def add():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
