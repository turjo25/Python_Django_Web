const productList = document.getElementById("product-list");
const cartCount = document.getElementById("cart-count");
const cartItemsContainer = document.getElementById("cart-items");
const cartTotal = document.getElementById("cart-total");
const cartModal = document.getElementById("cart-modal");

function displayProducts() {
  productList.innerHTML = "";
  products.forEach(product => {
    const div = document.createElement("div");
    div.className = "bg-white p-4 rounded shadow";
    div.innerHTML = `
      <img src="${product.image}" alt="${product.name}" class="w-full h-40 object-cover rounded">
      <h3 class="text-lg font-bold mt-2">${product.name}</h3>
      <p class="text-sm text-gray-600">${product.description}</p>
      <p class="font-semibold mt-2">BDT ${product.price}</p>
      <button class="mt-2 bg-blue-500 text-white px-3 py-1 rounded" onclick="addToCart(${product.id})">
        Add to Cart
      </button>
    `;
    productList.appendChild(div);
  });
}

function updateCartUI() {
  cartCount.textContent = cart.reduce((sum, item) => sum + item.quantity, 0);
  cartItemsContainer.innerHTML = "";

  cart.forEach(item => {
    const div = document.createElement("div");
    div.className = "flex justify-between items-center border-b pb-2";
    div.innerHTML = `
      <div>
        <p>${item.name}</p>
        <p>BDT ${item.price}</p>
      </div>
      <input type="number" min="1" value="${item.quantity}" class="w-16 border rounded p-1"
        onchange="updateQuantity(${item.id}, this.value)">
    `;
    cartItemsContainer.appendChild(div);
  });

  cartTotal.textContent = getCartTotal();
}

document.getElementById("view-cart-btn").addEventListener("click", () => {
  cartModal.classList.remove("hidden");
  cartModal.classList.add("flex");
});

document.getElementById("close-cart").addEventListener("click", () => {
  cartModal.classList.add("hidden");
});

document.getElementById("clear-cart").addEventListener("click", clearCart);

document.getElementById("checkout").addEventListener("click", () => {
  alert("Checkout successful! Thank you for your purchase.");
  clearCart();
});

document.getElementById("apply-promo").addEventListener("click", () => {
  const code = document.getElementById("promo-code").value.trim();
  applyPromoCode(code);
});

displayProducts();
updateCartUI();
