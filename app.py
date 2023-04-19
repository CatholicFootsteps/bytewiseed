from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        subscription = request.form['subscription']

        # Validate and process the form data
        # (e.g., store it in a database or send it to another service)
        # ...

        # Redirect to a success page or show a success message
        return redirect('/registration-success')

    return render_template_string(open('registration.html').read())

@app.route('/registration-success')
def registration_success():
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)
