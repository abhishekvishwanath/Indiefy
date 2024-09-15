// script.js

document.querySelector('.browse-btn').addEventListener('click', () => {
    confirm('Browse Products button clicked!');
    // Here, you can implement actual navigation or other interactions
    window.location.href = 'shop.html'; // Redirects to the shop page, replace with actual link
});
// Utility function to add click event listeners
function addClickListener(selector, callback) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
        element.addEventListener('click', callback);
    });
}

// Handle Subscribe Button Click
addClickListener('.subscribe-btn', () => {
    alert('Thank you for subscribing to our community!');
    // Additional functionality for subscription can go here
});

// Handle Shop Now Button Clicks
addClickListener('.shop-now-btn', () => {
    alert('Redirecting to the shop page.');
    window.location.href = 'shop.html'; // Replace with the actual shop page URL
});