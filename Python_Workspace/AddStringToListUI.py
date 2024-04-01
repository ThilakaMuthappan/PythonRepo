
import streamlit as st
import requests

# Define API endpoints
ADD_STRING_API_ENDPOINT = "http://localhost:5000/add_string"
GET_LIST_API_ENDPOINT = "http://localhost:5000/get_list"

def add_string_to_list(string):
    response = requests.post(ADD_STRING_API_ENDPOINT, json={"string": string})
    return response.status_code

def get_string_list():
    response = requests.get(GET_LIST_API_ENDPOINT)
    if response.status_code == 200:
        return response.json()["string_list"]
    else:
        return None

def main():
    st.title("Streamlit App with API Integration")

    # Input field to add a new string
    new_string = st.text_input("Enter a string:")
    
    # Button to add the string to the list
    if st.button("Add String"):
        if new_string:
            status_code = add_string_to_list(new_string)
            if status_code == 200:
                st.success("String added successfully!")
            else:
                st.error("Failed to add string to the list.")

    # Button to fetch and display the current list
    if st.button("Fetch String List"):
        string_list = get_string_list()
        if string_list:
            st.write("Current String List:")
            for string in string_list:
                st.write(string)
        else:
            st.error("Failed to fetch string list.")

if __name__ == "__main__":
    main()