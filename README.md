# Nextcloud App Password Manager & HTTP Bearer Token Generator

A comprehensive Streamlit-based toolkit providing two powerful web applications for authentication management.

## 🔑 Dual Authentication Tools

This project includes **two specialized applications** designed to streamline your authentication workflows:

### 1. **Nextcloud App Password Manager**
Your gateway to enhanced security and seamless application integration with your Nextcloud account.

### 2. **HTTP Bearer Basic Auth Token Generator**
A versatile tool for generating and testing HTTP Bearer Basic Authentication tokens for API integrations.

## 🚀 Why You Need These Tools

In today's connected world, secure authentication is crucial. Our elegant solutions provide:

✅ **Nextcloud Integration** - Create unique app passwords without compromising your main account
✅ **API Authentication** - Generate Bearer tokens for HTTP Basic Auth workflows
✅ **Instant Management** - Create, test, and revoke access with simple interfaces
✅ **Enhanced Security** - Application-specific credentials and token validation
✅ **Developer Friendly** - Code examples and testing capabilities built-in

## 🎯 Perfect For

- **Home users** managing personal cloud storage and API integrations
- **IT administrators** securing organizational Nextcloud instances
- **Developers** integrating applications with Nextcloud or other APIs
- **Security-conscious users** who want granular access control
- **API developers** needing quick Bearer token generation and testing

## ⚡ Get Started in Minutes

No complex installation or configuration required. Our PowerShell launchers automatically set up everything you need.

---

## 📋 Overview

This toolkit provides two specialized Streamlit applications:

1. **Nextcloud App Password Manager** - Register/unregister Nextcloud application passwords
2. **HTTP Bearer Token Generator** - Generate and test HTTP Basic Authentication Bearer tokens

## ✨ Features

### Nextcloud App Password Manager
- Register new application passwords for Nextcloud
- Unregister existing application passwords
- User-friendly web interface with detailed feedback
- Secure credential handling
- Comprehensive error reporting

### HTTP Bearer Token Generator
- Generate HTTP Bearer Basic Authentication tokens
- Test tokens against live API endpoints
- Multiple HTTP method support (GET, POST, PUT, DELETE)
- Code examples in multiple languages (Python, JavaScript, cURL)
- Real-time token validation and testing
- Detailed response analysis

### Common Features
- Cross-platform compatibility
- Automatic dependency management
- Virtual environment support
- Professional UI with Streamlit

## Installation

### Prerequisites

- Python 3.6 or higher
- PowerShell 7.1 or higher (for Windows users)
- Nextcloud server instance with API access

### Option 1: Using PowerShell Scripts (Recommended for Windows)

1. Clone or download this repository
2. Choose and run the appropriate PowerShell script:

**For Nextcloud App Password Management:**
```powershell
.\start_nx_app_pass.ps1
```

**For HTTP Bearer Token Generation:**
```powershell
.\start_http_bearer_app.ps1
```

Both scripts will:
- Check for PowerShell 7.1+ and use the correct version
- Find and activate a Python virtual environment if one exists
- Install dependencies from requirements.txt if available
- Install Streamlit if it's not already installed
- Launch the respective application

### Option 2: Manual Installation

1. Clone or download this repository
2. (Optional) Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install streamlit requests
```

4. Run the desired application:

**For Nextcloud App Password Management:**
```bash
streamlit run streamlit_nx_app_pass.py
```

**For HTTP Bearer Token Generation:**
```bash
streamlit run streamlit_http_bearer_gen.py
```

## 📖 Usage

### Nextcloud App Password Manager

1. Launch the application using [`start_nx_app_pass.ps1`](start_nx_app_pass.ps1) or manually with [`streamlit_nx_app_pass.py`](streamlit_nx_app_pass.py)
2. The application will open in your default web browser at http://localhost:8501
3. In the sidebar, enter the following information:
   - **Nextcloud URL** (e.g., https://nextcloud.example.com)
   - **Your Nextcloud username**
   - **Your Nextcloud password**
   - **Application name** (will be used as the User-Agent header)
4. Select the operation you want to perform:
   - **"Register a new app"** - to create a new application password
   - **"Unregister an existing app"** - to delete an existing application password
5. Click **"Submit Request"**
6. View the results in the main panel:
   - For successful registrations, an application password will be displayed
   - **Important**: Save this password securely as it won't be shown again

### HTTP Bearer Token Generator

1. Launch the application using [`start_http_bearer_app.ps1`](start_http_bearer_app.ps1) or manually with [`streamlit_http_bearer_gen.py`](streamlit_http_bearer_gen.py)
2. The application will open in your default web browser at http://localhost:8501
3. In the sidebar, enter your authentication credentials:
   - **Username** for the API/service
   - **Password** for the API/service
4. **Optional**: Enable token testing by checking "Test the generated token"
   - Enter the **API endpoint URL** to test against
   - Select the **HTTP method** (GET, POST, PUT, DELETE)
   - For POST/PUT requests, provide a **JSON request body**
5. Click **"Generate Token"**
6. View the results:
   - **Generated Bearer token** for use in HTTP headers
   - **Usage examples** in multiple programming languages
   - **Token details** and encoding information
   - **Test results** if testing was enabled

## Technical Details

### API Endpoints

The application interacts with the following Nextcloud API endpoints:

- **Register new app password**: `GET /ocs/v2.php/core/getapppassword`
- **Unregister app password**: `DELETE /ocs/v2.php/core/apppassword`

### Authentication

The application uses HTTP Basic Authentication with your Nextcloud username and password to authenticate API requests.

### Request Headers

- `User-Agent`: Set to the application name provided by the user
- `OCS-APIRequest`: Set to 'true'
- `Accept`: Set to 'application/json'

### Error Handling

The application handles various error scenarios:

- Connection errors (server unreachable)
- Authentication failures
- Timeout errors
- HTTP errors with specific messages for common status codes (401, 403, 404)
- General request exceptions
- JSON parsing errors

## Security Considerations

- Your Nextcloud credentials are used only for API authentication and are not stored
- The application uses HTTPS for secure communication with your Nextcloud server
- Generated app passwords are displayed only once and not stored by the application
- Consider running this application locally rather than on a public server

## Development

### Project Structure

- [`streamlit_nx_app_pass.py`](streamlit_nx_app_pass.py) - Nextcloud App Password Manager application
- [`streamlit_http_bearer_gen.py`](streamlit_http_bearer_gen.py) - HTTP Bearer Token Generator application
- [`start_nx_app_pass.ps1`](start_nx_app_pass.ps1) - PowerShell launcher for Nextcloud app
- [`start_http_bearer_app.ps1`](start_http_bearer_app.ps1) - PowerShell launcher for Bearer token app
- [`requirements.txt`](requirements.txt) - Python dependencies
- [`requirements-dev.txt`](requirements-dev.txt) - Development dependencies

### Dependencies

- **[Streamlit](https://streamlit.io/)** ≥1.22.0 - Web application framework
- **[Requests](https://docs.python-requests.org/)** ≥2.28.2 - HTTP library for API calls
- **[Certifi](https://pypi.org/project/certifi/)** ≥2022.12.7 - SSL certificate verification
- **[urllib3](https://urllib3.readthedocs.io/)** ≥1.26.15 - HTTP client library

See [`requirements.txt`](requirements.txt) for complete dependency list.

## License

MIT License - See the license information in the source code for details.

## Author

harokku999@gmail.com

---

Copyright 2025 harokku999@gmail.com | MIT License