#!/usr/bin/env python3
"""
Copyright 2025 harokku999@gmail.com
MIT Licence
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import streamlit as st
import base64
import json
import requests
from urllib.parse import urlparse

# Set page config
st.set_page_config(
    page_title="HTTP Bearer Basic Auth Token Generator",
    page_icon="🔐",
    layout="centered"
)

# App title and description
st.title("HTTP Bearer Basic Auth Token Generator")
st.markdown("""
This application generates Bearer Basic Authentication tokens for HTTP header requests.
Enter your username and password to generate the encoded token for API authentication.
""")

# Create a sidebar for inputs
with st.sidebar:
    st.header("Authentication Details")
    
    # User inputs
    username = st.text_input("Username", help="Your username for authentication")
    password = st.text_input("Password", type="password", help="Your password for authentication")
    
    st.markdown("---")
    st.header("Optional: Test the Token")
    test_enabled = st.checkbox("Test the generated token", help="Enable to test the token against an API endpoint")
    
    if test_enabled:
        test_url = st.text_input("API Endpoint URL", help="URL to test the authentication token against")
        test_method = st.selectbox("HTTP Method", ["GET", "POST", "PUT", "DELETE"], index=0)
        
        if test_method in ["POST", "PUT"]:
            test_body = st.text_area("Request Body (JSON)", help="JSON body for POST/PUT requests", placeholder='{"key": "value"}')
    
    # Generate button
    generate_button = st.button("Generate Token", type="primary")

# Main content area for displaying results
if generate_button:
    if not username or not password:
        st.error("Both username and password are required.")
    else:
        # Generate the Basic Auth token
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        bearer_token = f"Basic {encoded_credentials}"
        
        # Display the generated token
        st.success("Bearer Basic Authentication token generated successfully!")
        
        # Token display section
        st.subheader("Generated Token")
        
        st.code(bearer_token, language="text")
        
        # Show different usage examples
        with st.expander("Usage Examples", expanded=True):
            st.markdown("### HTTP Header")
            header_example = f"Authorization: {bearer_token}"
            st.code(header_example, language="text")
            
            st.markdown("### cURL Example")
            curl_example = f'curl -H "Authorization: {bearer_token}" https://api.example.com/endpoint'
            st.code(curl_example, language="bash")
            
            st.markdown("### Python Requests Example")
            python_code = f'''import requests

headers = {{
    "Authorization": "{bearer_token}",
    "Content-Type": "application/json"
}}

response = requests.get("https://api.example.com/endpoint", headers=headers)
print(response.json())'''
            st.code(python_code, language="python")
            
            st.markdown("### JavaScript Fetch Example")
            js_code = f'''fetch('https://api.example.com/endpoint', {{
    method: 'GET',
    headers: {{
        'Authorization': '{bearer_token}',
        'Content-Type': 'application/json'
    }}
}})
.then(response => response.json())
.then(data => console.log(data));'''
            st.code(js_code, language="javascript")
        
        # Token details section
        with st.expander("Token Details"):
            st.info(f"**Username:** {username}")
            st.info(f"**Encoded Credentials:** {encoded_credentials}")
            st.info(f"**Full Authorization Header:** Authorization: {bearer_token}")
            
            # Show the raw credentials being encoded (for verification)
            st.markdown("**Raw Credentials String:**")
            st.code(credentials, language="text")
        
        # Test the token if enabled
        if test_enabled and test_url:
            st.markdown("---")
            st.subheader("Token Test Results")
            
            # Validate URL
            try:
                parsed_url = urlparse(test_url)
                if not parsed_url.scheme or not parsed_url.netloc:
                    st.error("Please enter a valid URL (including http:// or https://)")
                else:
                    with st.spinner("Testing the authentication token..."):
                        try:
                            headers = {
                                "Authorization": bearer_token,
                                "Content-Type": "application/json",
                                "User-Agent": "HTTP-Bearer-Token-Generator/1.0"
                            }
                            
                            # Prepare request based on method
                            if test_method == "GET":
                                response = requests.get(test_url, headers=headers, timeout=30)
                            elif test_method == "POST":
                                data = json.loads(test_body) if test_body else {}
                                response = requests.post(test_url, headers=headers, json=data, timeout=30)
                            elif test_method == "PUT":
                                data = json.loads(test_body) if test_body else {}
                                response = requests.put(test_url, headers=headers, json=data, timeout=30)
                            elif test_method == "DELETE":
                                response = requests.delete(test_url, headers=headers, timeout=30)
                            
                            # Display results
                            if response.status_code == 200:
                                st.success(f"✅ Authentication successful! Status Code: {response.status_code}")
                            elif response.status_code == 401:
                                st.error(f"❌ Authentication failed! Status Code: {response.status_code}")
                            else:
                                st.warning(f"⚠️ Request completed with Status Code: {response.status_code}")
                            
                            # Show response details
                            with st.expander("Response Details", expanded=True):
                                st.info(f"**Status Code:** {response.status_code}")
                                st.info(f"**Response Headers:**")
                                st.json(dict(response.headers))
                                
                                # Try to display response as JSON, fallback to text
                                try:
                                    response_json = response.json()
                                    st.markdown("**Response Body (JSON):**")
                                    st.json(response_json)
                                except:
                                    st.markdown("**Response Body (Text):**")
                                    st.code(response.text)
                        
                        except requests.exceptions.Timeout:
                            st.error("⏱️ The request timed out after 30 seconds.")
                        
                        except requests.exceptions.ConnectionError as e:
                            st.error(f"🔌 Could not connect to the server. Check the URL and network connection.\nDetails: {e}")
                        
                        except requests.exceptions.HTTPError as e:
                            st.error(f"🚫 HTTP Error: {e.response.status_code} - {e.response.reason}")
                        
                        except json.JSONDecodeError:
                            st.error("❌ Invalid JSON in request body. Please check the format.")
                        
                        except Exception as e:
                            st.error(f"❌ An unexpected error occurred: {e}")
            
            except Exception as e:
                st.error(f"❌ URL validation error: {e}")

# Add instructions at the bottom
st.markdown("---")
st.markdown("""
### How to use this app:
1. **Enter your credentials:** Provide your username and password in the sidebar
2. **Generate token:** Click "Generate Token" to create your Bearer Basic Auth token
3. **Copy and use:** Copy the generated token and use it in your HTTP requests
4. **Optional testing:** Enable token testing to verify it works with your API endpoint
5. **Security note:** This tool runs locally - your credentials are not stored or transmitted anywhere

### About Basic Authentication:
Basic Authentication encodes your username and password in Base64 format. The format is:
- Combine username and password with a colon: `username:password`
- Encode in Base64: `base64(username:password)`
- Add "Basic " prefix: `Basic base64(username:password)`
""")

# Add a footer
st.markdown("---")
st.caption("HTTP Bearer Basic Auth Token Generator | Copyright 2025 harokku999@gmail.com | MIT Licence | Created with Streamlit")