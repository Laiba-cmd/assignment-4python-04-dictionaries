import streamlit as st

# Title of the app
st.title("Phonebook")

# Initialize an empty list to store contacts
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

# Input fields for adding a contact
name = st.text_input("Enter contact name:")
phone = st.text_input("Enter contact phone number:")

# Button to add the contact
if st.button("Add Contact"):
    if name and phone:
        st.session_state.contacts.append({"name": name, "phone": phone})
        st.success(f"Contact {name} added!")
    else:
        st.error("Please enter both name and phone number.")

# Display the list of contacts
if st.session_state.contacts:
    st.write("### Contacts List")
    for contact in st.session_state.contacts:
        st.write(f"{contact['name']}: {contact['phone']}")
else:
    st.write("No contacts added yet.")
