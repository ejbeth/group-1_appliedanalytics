from flask import Flask, render_template, redirect, url_for, session, flash, request
import os

app = Flask(__name__)
app.secret_key = 'amefa-portal-secret-key-2024'  # Change this for production

# Debug: Show template structure
print("=" * 50)
print("AMEFA ORDER PORTAL - Flask Application")
print("=" * 50)
print(f"Current directory: {os.getcwd()}")
print(f"Templates folder: {app.template_folder}")
print("=" * 50)

# Root route - redirects to login
@app.route('/')
def home():
    # Redirect to login page
    return redirect(url_for('login'))

# Login route (using your cust_login_reg.html template)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simple authentication (replace with real auth later)
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username and password:  # Basic validation
            session['user_id'] = 1  # Set a dummy user ID
            session['username'] = username
            flash('Login successful! Welcome to Amefa Order Portal.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Please enter both username and password', 'error')
    
    # Render the login page
    return render_template('pages/cust_login_reg.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login to access the dashboard.', 'error')
        return redirect(url_for('login'))
    return render_template('pages/dashboard.html', username=session.get('username'))

# Products route
@app.route('/products')
def products():
    if 'user_id' not in session:
        flash('Please login to view products.', 'error')
        return redirect(url_for('login'))
    return render_template('pages/products.html')

# Orders route
@app.route('/orders')
def orders():
    if 'user_id' not in session:
        flash('Please login to view orders.', 'error')
        return redirect(url_for('login'))
    return render_template('pages/order_view.html')

# Reports route
@app.route('/reports')
def reports():
    if 'user_id' not in session:
        flash('Please login to view reports.', 'error')
        return redirect(url_for('login'))
    return render_template('pages/report.html')

# Support route
@app.route('/support')
def support():
    if 'user_id' not in session:
        flash('Please login to access support.', 'error')
        return redirect(url_for('login'))
    return render_template('pages/support.html')

# Add a test route to verify CSS is working
@app.route('/test-css')
def test_css():
    """Test route to verify CSS is loading correctly"""
    return render_template('pages/dashboard.html', username='Test User')

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("🚀 AMEFA ORDER PORTAL STARTING...")
    print("=" * 50)
    print("Application is running!")
    print("Open your browser and go to: http://localhost:5000")
    print("=" * 50)
    print("TEST CREDENTIALS:")
    print("• Username: any username")
    print("• Password: any password")
    print("=" * 50)
    print("Navigation:")
    print("• /login - Login page")
    print("• /dashboard - Main dashboard (after login)")
    print("• /products - Products catalog")
    print("• /orders - Order management")
    print("• /reports - Reports & analytics")
    print("• /support - Support center")
    print("• /logout - Logout")
    print("=" * 50 + "\n")
    
    app.run(debug=True, port=5000)