// Function to handle Razorpay payment
document.getElementById('rzp-button').onclick = function(e) {
    var options = {
        "key": "rzp_test_XXXXXXXXXXXXXXXX", // Enter the Key ID generated from the Razorpay Dashboard
        "amount": "50000", // Amount is in paise (e.g. 50000 paise = INR 500)
        "currency": "INR",
        "name": "Your Store",
        "description": "Purchase Description",
        "image": "https://your-logo-url.com", // Optional: Your company logo
        "handler": function (response){
            // Here you can handle the successful payment event
            alert("Payment Successful! Payment ID: " + response.razorpay_payment_id);
        },
        "prefill": {
            "name": document.getElementById('name').value,
            "email": document.getElementById('email').value
        },
        "theme": {
            "color": "#3399cc"
        },
        "method": {
            "upi": true, // Enabling UPI as a payment method
            "card": true, // Enabling card payment method
            "netbanking": true, // Enabling netbanking method
            "wallet": true // Enabling wallet payment method
        }
    };
    var rzp1 = new Razorpay(options);
    rzp1.open();
    e.preventDefault();
}


