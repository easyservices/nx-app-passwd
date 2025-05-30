#!/usr/bin/env python3
"""
Copyright 2025 harokku999@gmail.com
MIT Licence
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import streamlit as st
import requests

# Constants
NEXTCLOUD_APP_PASSWD_REGISTER_URL = "/ocs/v2.php/core/getapppassword"
NEXTCLOUD_APP_PASSWD_UNREGISTER_URL = "/ocs/v2.php/core/apppassword"

# Set page config
st.set_page_config(
    page_title="Nextcloud App Password Manager",
    page_icon="🔑",
    layout="centered"
)

# App title and description
st.title("Nextcloud App Password Manager")
st.markdown("""
This application allows you to register new application passwords or unregister existing ones
for your Nextcloud account.
""")

# Create a sidebar for inputs
with st.sidebar:
    st.header("User Information")
    
    # Request type selection
    req_type = st.radio(
        "Select operation:",
        ["Register a new app", "Unregister an existing app"],
        index=0
    )
    
    # User inputs
    nextcloud_base_url = st.text_input("Nextcloud URL", help="Your Nextcloud base URL with port if any (like https://nextcloud.example.com)")
    username = st.text_input("Username", help="Your Nextcloud username")
    password = st.text_input("Password", type="password", help="Your Nextcloud password")
    app_name = st.text_input("Application Name", help="Name for the application (User-Agent header)")
    
    # Submit button
    submit_button = st.button("Submit Request", type="primary")

# Main content area for displaying results
if submit_button:
    if not username or not password or not app_name or not nextcloud_base_url:
        st.error("All fields are required.")
    else:
        # Prepare the request
        headers = {
            'User-Agent': app_name,
            'OCS-APIRequest': 'true',
            'Accept': 'application/json'
        }
        auth = (username, password)

        full_url = f"{nextcloud_base_url}{NEXTCLOUD_APP_PASSWD_REGISTER_URL if req_type == 'Register a new app' else NEXTCLOUD_APP_PASSWD_UNREGISTER_URL}"
        
        # Display request information
        with st.expander("Request Details", expanded=True):
            st.info(f"URL: {full_url}")
            st.info(f"User-Agent: {app_name}")
            st.info(f"Authenticating as user: {username}")
            st.info(f"Operation: {'Registration' if req_type == 'Register a new app' else 'Unregistration'}")
        
        # Create a spinner while making the request
        with st.spinner("Processing request..."):
            try:
                if req_type == "Register a new app":
                    # Register a new app
                    response = requests.get(
                        full_url,
                        headers=headers,
                        auth=auth,
                        timeout=30
                    )
                else:
                    # Unregister an existing app
                    response = requests.delete(
                        full_url,
                        headers=headers,
                        auth=auth,
                        timeout=30
                    )
                
                # Raise an exception for bad status codes
                response.raise_for_status()
                
                # Process successful response
                st.success(f"Request Successful! Status Code: {response.status_code}")
                
                # Display response in a nice format
                st.subheader("Response")
                
                # Try to parse as JSON for better display
                try:
                    response_json = response.json()
                    st.json(response_json)
                except:
                    # If not JSON, show as text
                    st.code(response.text)
                
                # If it's a registration, highlight the app password
                if req_type == "Register a new app" and "apppassword" in response.text.lower():
                    st.subheader("Your App Password")
                    json_res = response.json()
                    if json_res["ocs"]["data"]["apppassword"]:
                        app_password = json_res["ocs"]["data"]["apppassword"]
                        # Highlight the password
                        st.code(app_password, language="text")
                        st.warning("⚠️ Save this password securely! It won't be shown again.")
            
            except requests.exceptions.Timeout:
                st.error("The request timed out after 30 seconds.")
            
            except requests.exceptions.ConnectionError as e:
                st.error(f"Could not connect to the server. Check the URL and network connection.\nDetails: {e}")
            
            except requests.exceptions.HTTPError as e:
                error_message = f"HTTP Error: {e.response.status_code} - {e.response.reason}"
                
                if e.response.status_code == 401:
                    error_message += "\nAuthentication failed. Please check your username and password."
                elif e.response.status_code == 403:
                    error_message += "\nAccess forbidden. You may not have permission to access this resource."
                elif e.response.status_code == 404:
                    error_message += "\nResource not found. Please check the URL."
                
                st.error(error_message)
                
                # Show error response for debugging
                with st.expander("Error Response Details"):
                    st.code(e.response.text)
            
            except requests.exceptions.RequestException as e:
                st.error(f"An unexpected error occurred during the request.\nDetails: {e}")
            
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

# Add instructions at the bottom
st.markdown("---")
st.markdown("""
### How to use this app:
1. Enter your Nextcloud base URL (with port if any), username and password
2. Provide a name for the application
3. Select whether you want to register a new app or unregister an existing one
4. Click "Submit Request"
5. For new registrations, be sure to save the generated app password
""")

# Add a footer
st.markdown("---")
st.caption("Nextcloud App Password Manager | Copyright 2025 harokku999@gmail.com | MIT Licence | Created with Streamlit")