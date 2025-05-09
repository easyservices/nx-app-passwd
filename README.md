# Nextcloud App Password Manager

A Streamlit-based web application for managing Nextcloud application passwords.

## Secure Your Digital Life with Ease

**Nextcloud App Password Manager** is your gateway to enhanced security and seamless application integration with your Nextcloud account.

### Why You Need This Tool

In today's connected world, you're likely using multiple applications that connect to your Nextcloud storage. Using your main password everywhere creates unnecessary risk. Our elegant solution lets you:

✅ **Create unique passwords** for each application without compromising your main account  
✅ **Revoke access** instantly for any application without affecting others  
✅ **Maintain control** over which applications can access your data  
✅ **Enhance security** with application-specific credentials  

### Streamlined Experience

With our intuitive interface, managing application passwords has never been easier:

- **Simple setup** - Just enter your Nextcloud details and go
- **One-click generation** - Create new app passwords in seconds
- **Instant revocation** - Remove access with a single click
- **Clear feedback** - Always know exactly what's happening

### Perfect For

- Home users managing personal cloud storage
- IT administrators securing organizational Nextcloud instances
- Developers integrating applications with Nextcloud
- Security-conscious users who want granular access control

### Get Started in Minutes

No complex installation or configuration required. Our PowerShell launcher automatically sets up everything you need, so you can focus on what matters - keeping your digital life secure.

---

## Overview

This application provides a user-friendly interface to register new application passwords or unregister existing ones for your Nextcloud account. It interacts with the Nextcloud API to perform these operations securely.

## Features

- Register new application passwords for Nextcloud
- Unregister existing application passwords
- User-friendly web interface
- Secure handling of credentials
- Detailed error reporting
- Cross-platform compatibility

## Installation

### Prerequisites

- Python 3.6 or higher
- PowerShell 7.1 or higher (for Windows users)
- Nextcloud server instance with API access

### Option 1: Using the PowerShell Script (Recommended for Windows)

1. Clone or download this repository
2. Run the included PowerShell script:

```powershell
.\runMe.ps1
```

The script will:
- Check for PowerShell 7.1+ and use the correct version
- Find and activate a Python virtual environment if one exists
- Install Streamlit if it's not already installed
- Launch the application

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

4. Run the application:

```bash
streamlit run streamlit_app.py
```

## Usage

1. Launch the application using one of the installation methods above
2. The application will open in your default web browser at http://localhost:8501
3. In the sidebar, enter the following information:
   - Nextcloud URL (e.g., https://nextcloud.example.com)
   - Your Nextcloud username
   - Your Nextcloud password
   - Application name (will be used as the User-Agent header)
4. Select the operation you want to perform:
   - "Register a new app" - to create a new application password
   - "Unregister an existing app" - to delete an existing application password
5. Click "Submit Request"
6. View the results in the main panel:
   - For successful registrations, an application password will be displayed
   - **Important**: Save this password securely as it won't be shown again

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

- `streamlit_app.py` - Main Streamlit application
- `runMe.ps1` - PowerShell script for easy launching on Windows

### Dependencies

- [Streamlit](https://streamlit.io/) - Web application framework
- [Requests](https://docs.python-requests.org/) - HTTP library for API calls

## License

MIT License - See the license information in the source code for details.

## Author

harokku999@gmail.com

---

Copyright 2025 harokku999@gmail.com | MIT License