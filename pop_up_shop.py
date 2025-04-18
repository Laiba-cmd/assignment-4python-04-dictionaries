import streamlit as st

# Title of the app
st.title("Pop-Up Shop")

# Sample product list
products = {
    "T-shirt": 20.00,
    "Hat": 15.00,
    "Mug": 10.00,
    "Sticker": 5.00
}

# Initialize an empty shopping cart
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Display available products
st.write("### Available Products")
for product, price in products.items():
    st.write(f"{product}: ${price}")
    if st.button(f"Add {product} to cart"):
        if product in st.session_state.cart:
            st.session_state.cart[product] += 1
        else:
            st.session_state.cart[product] = 1
        st.success(f"{product} added to cart!")

# Display the shopping cart
if st.session_state.cart:
    st.write("### Shopping Cart")
    for product, quantity in st.session_state.cart.items():
        st.write(f"{product}: {quantity}")
else:
    st.write("Your cart is empty.")
