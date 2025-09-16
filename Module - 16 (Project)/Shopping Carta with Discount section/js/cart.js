let cart = [];
let appliedPromo = null; 

function addToCart(productId) {
  const product = products.find(p => p.id === productId);
  if (!product) return;

  const cartItem = cart.find(item => item.id === productId);
  if (cartItem) {
    cartItem.quantity++;
  } else {
    cart.push({ ...product, quantity: 1 });
  }
  updateCartUI();
}

function updateQuantity(productId, quantity) {
  quantity = parseInt(quantity);
  if (quantity <= 0) return;

  const cartItem = cart.find(item => item.id === productId);
  if (cartItem) {
    cartItem.quantity = quantity;
    updateCartUI();
  }
}

function clearCart() {
  cart = [];
  appliedPromo = null;
  updateCartUI();
}

function getCartTotal() {
  let total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  if (appliedPromo === "ostad10") total *= 0.9;
  if (appliedPromo === "ostad50") total *= 0.5;

  return total.toFixed(2);
}

function applyPromoCode(code) {
  const promoMessage = document.getElementById("promo-message");

  if (appliedPromo) {
    promoMessage.textContent = "Promo code already applied.";
    promoMessage.classList.add("text-red-500");
    return;
  }

  if (code === "ostad10" || code === "ostad50") {
    appliedPromo = code;
    promoMessage.textContent = `Promo code "${code}" applied successfully!`;
    promoMessage.classList.remove("text-red-500");
    promoMessage.classList.add("text-green-600");
  } else {
    promoMessage.textContent = "Invalid Promo Code";
    promoMessage.classList.remove("text-green-600");
    promoMessage.classList.add("text-red-500");
  }

  updateCartUI();
}
