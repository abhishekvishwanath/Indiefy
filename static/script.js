document.addEventListener('DOMContentLoaded', () => {
  // Add click event to "Shop Now" buttons
  const shopNowButtons = document.querySelectorAll('.shop-now');

  shopNowButtons.forEach(button => {
      button.addEventListener('click', () => {
          alert('Added to cart!');
      });
  });
});
