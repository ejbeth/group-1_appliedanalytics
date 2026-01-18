from flask import Flask, render_template

app = Flask(__name__)

# Root route - required to avoid 404 on homepage
@app.route('/')
def home():
    # Show login page as homepage
    return render_template('customer_login.html')

# Login route
@app.route('/login')
def customer_login():
    return render_template('customer_login.html')

# Products route
@app.route('/products')
def products():
    return render_template('products.html')

# Orders route
@app.route('/orders')
def order_view():
    return render_template('order_view.html')

# Reports route
@app.route('/reports')
def report_view():
    return render_template('report.html')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
