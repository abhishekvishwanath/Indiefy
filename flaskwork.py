from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from twilio.rest import Client
from dotenv import load_dotenv
import MySQLdb.cursors
import random
import os
import secrets
from flask import Flask, request, jsonify  
import razorpay
from flask import Flask, render_template, url_for

# Initialize Flask app
app = Flask(__name__)

# Generate a unique secret key
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

# Load environment variables from .env file
load_dotenv()

# Twilio configuration
'''TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)'''

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'madhan'
app.config['MYSQL_DB'] = 'indiefy'

# Initialize MySQL
mysql = MySQL(app)

# Routes
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('FirstName')
        last_name = request.form.get('LastName')
        email = request.form.get('Email')
        phone_number = request.form.get('PhoneNumber')
        message = request.form.get('Message')

        try:
            # Insert data into the contacts table
            cursor = mysql.connection.cursor()
            insert_query = """
                INSERT INTO contacts  (first_name, last_name, email, phone, message)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (first_name, last_name, email, phone_number, message))
            mysql.connection.commit()
            cursor.close()

            # Redirect to a success page or show a success message
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for('contact'))
        except Exception as e:
            print(f"Error: {e}")
            flash("An error occurred. Please try again later.", "error")
            return redirect(url_for('contact'))

    return render_template('contact.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the form data is valid
        if not username or not email or not password:
            flash("Please fill out all fields!", "error")
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            # Insert data into the users table
            cursor = mysql.connection.cursor()
            insert_query = """
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (username, email, hashed_password))
            mysql.connection.commit()
            cursor.close()

            # Success message and redirect
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            # Handle and log errors
            print(f"Error: {e}")
            flash("An error occurred. Please try again later.", "error")
            return redirect(url_for('register'))
        


    return render_template('register.html')

@app.route('/verify')
def verify():
    return render_template('verifyotp.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/state')
def state():
    return render_template('state.html')

@app.route('/banarasisaree')
def banarasisaree():
    return render_template('banarasisaree.html')

@app.route('/homeanddecor')
def homeanddecor():
    return render_template('homeanddecor.html')

@app.route('/karnataka')
def karnataka():
    return render_template('karnataka.html')
@app.route('/rajasthan')
def rajasthan():
    return render_template('rajasthan.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            flash("Please fill out all fields!", "error")
            return redirect(url_for('login'))

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password!", "error")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        
        flash(f"Welcome {session['username']} to Indiefy!")
        return redirect(url_for('homepage'))  
    return redirect(url_for('login'))

# OTP logic
'''def generate_otp():
    return str(random.randint(100000, 999999))

def send_sms(phone_number, otp):
    try:
        message = client.messages.create(
            body=f"Your OTP is {otp}. It is valid for 10 minutes.",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

@app.route('/send_otp', methods=['POST'])
def send_otp():
    try:
        username = request.form['username']
        phone_number = request.form['phone']
        password = request.form['password']

        otp = generate_otp()
        session['otp'] = otp
        session['user_details'] = {'username': username, 'phone': phone_number, 'password': password}

        if send_sms(phone_number, otp):
            flash('An OTP has been sent to your phone. Please check your SMS.', 'info')
            return redirect(url_for('otp_verification'))
        else:
            flash('Failed to send OTP via SMS. Please try again.', 'error')
            return redirect(url_for('register'))

    except Exception as e:
        print(f"Error processing OTP request: {e}")
        flash('There was an error processing your request. Please try again.', 'error')
        return redirect(url_for('register'))

@app.route('/otp_verification', methods=['GET'])
def otp_verification():
    return render_template('verifyotp.html')

@app.route('/verifyotp', methods=['POST'])
def verifyotp():
    user_otp = request.form['otp']
    actual_otp = session.get('otp')

    if user_otp == actual_otp:
        user_details = session.get('user_details')
        hashed_password = generate_password_hash(user_details['password'])

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO users (username, phone, password) VALUES (%s, %s, %s)',
                       (user_details['username'], user_details['phone'], hashed_password))
        mysql.connection.commit()
        flash('Your account has been created successfully!', 'success')

        session.pop('otp', None)
        session.pop('user_details', None)
        return redirect(url_for('login'))
    else:
        flash('Invalid OTP, please try again.', 'danger')
        return redirect(url_for('otp_verification'))'''





 #Razorpay logic

 # Initialize Razorpay client with API key and secret
'''razorpay_client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_SECRET"))


@app.route('/create-order', methods=['POST'])
def create_order():
    try:
        # Assuming 'product_id' is passed in the request body
        product_id = request.form.get('product_id')

        # Step 1: Fetch product details using Flask-MySQL
        cursor = mysql.connection.cursor()
        query = "SELECT price FROM products WHERE product_id = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()

        if not product:
            return jsonify(error="Product not found"), 404

        amount = int(product[0] * 100)  # Convert to paise
        currency = "INR"
        receipt = f"receipt_order_{product_id}"

        # Step 2: Create Razorpay order
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, receipt=receipt))

        # Close the cursor
        cursor.close()

        return jsonify(order_id=razorpay_order['id'], amount=amount, currency=currency)

    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/verify-payment', methods=['POST'])
def verify_payment():
    try:
        payment_id = request.form.get('razorpay_payment_id')
        order_id = request.form.get('razorpay_order_id')
        signature = request.form.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        # Step 3: Verify the payment signature
        razorpay_client.utility.verify_payment_signature(params_dict)

        return jsonify(status="Payment verified successfully!")

    except razorpay.errors.SignatureVerificationError:
        return jsonify(status="Payment verification failed!"), 400'''

#insert images into databse
'''def insert_product(product_name, product_image_path, qr_code_path, price):

    # MySQL connection is now handled by Flask-MySQL
    cur = mysql.connection.cursor()

    # Insert the file paths into the database
    cur.execute(
        "INSERT INTO products (product_name, product_image_path, qr_code_image_path, price) VALUES (%s, %s, %s, %s)",
        (product_name, product_image_path, qr_code_path, price)
    )

    # Commit the transaction
    mysql.connection.commit()

    # Close the cursor
    cur.close()

# Route to display the payment page
@app.route('/product/<int:product_id>')
def product_details(product_id):
    cur = mysql.connection.cursor()

    # Fetch product details including image and QR code paths
    cur.execute("SELECT id, product_name, product_image_path, qr_code_image_path, price FROM products WHERE id = %s", (product_id,))
    product = cur.fetchone()

    if product:
        product_data = {
            'id': product[0],
            'name': product[1],
            'image_path': product[2],  # File path for product image
            'qr_code_path': product[3],  # File path for QR code
            'price': product[4]
        }
        return render_template('payment.html', product=product_data)
    else:
        return "Product not found!", 404'''





@app.route('/index')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT product_id, name, price, image FROM products")
    products = cur.fetchall()
    cur.close()
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""
        SELECT cart.product_id, products.name, products.price, cart.quantity 
        FROM cart 
        INNER JOIN products ON cart.product_id = products.product_id
    """)
    cart_items = cur.fetchall()
    
    # Calculate total price
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    
    cur.close()
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = request.form.get('quantity', 1)
    cur = mysql.connection.cursor()
    
    # Check if product is already in the cart
    cur.execute("SELECT * FROM cart WHERE product_id=%s", (product_id,))
    existing_product = cur.fetchone()

    if existing_product:
        # Update quantity if the product is already in the cart
        cur.execute("UPDATE cart SET quantity = quantity + %s WHERE product_id = %s", (quantity, product_id))
    else:
        # Insert the product into the cart
        cur.execute("INSERT INTO cart (product_id, quantity) VALUES (%s, %s)", (product_id, quantity))

    # Commit changes and close cursor
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('cart'))
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cur = mysql.connection.cursor()
    
    # Remove the item from the cart
    cur.execute("DELETE FROM cart WHERE product_id=%s", (product_id,))
    
    # Commit changes and close cursor
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('cart'))



if __name__ == '__main__':
    app.run(debug=True)
