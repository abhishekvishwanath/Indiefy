function increaseQuantity() {
  const quantityInput = document.getElementById('quantity');
  const currentQuantity = parseInt(quantityInput.value, 10);
  quantityInput.value = currentQuantity + 1;
}

function decreaseQuantity() {
  const quantityInput = document.getElementById('quantity');
  const currentQuantity = parseInt(quantityInput.value, 10);
  if (currentQuantity > 1) {
    quantityInput.value = currentQuantity - 1;
  }
}
