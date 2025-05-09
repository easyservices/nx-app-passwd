# Nextcloud App Password Manager - Technical Documentation

This document provides detailed technical information about the Nextcloud App Password Manager application, intended for developers who want to understand or modify the codebase.

## Architecture Overview

The application follows a simple client-server architecture:

1. **Client**: Streamlit web interface running in the user's browser
2. **Application Server**: Python-based Streamlit server handling the UI and business logic
3. **Nextcloud Server**: External system that the application communicates with via REST API

```
+----------------+       +------------------+       +------------------+
|                |       |                  |       |                  |
|  Web Browser   | <---> |  Streamlit App   | <---> |  Nextcloud API   |
|                |       |                  |       |                  |
+----------------+       +------------------+       +------------------+
```

## Code Structure

### streamlit_app.py

The main application file contains the following components:

1. **Imports and Constants**:
   - Streamlit and requests libraries
   - API endpoint constants

2. **UI Components**:
   - Page configuration
   - Title and description
   - Sidebar with input fields
   - Main content area for results
   - Instructions and footer

3. **Request Handling**:
   - Input validation
   - API request preparation
   - Response processing
   - Error handling

4. **Response Display**:
   - Success messages
   - JSON/text response formatting
   - App password highlighting
   - Error messages with details

### runMe.ps1

The PowerShell script handles the application setup and execution:

1. **Version Checking**:
   - Verifies PowerShell version (7.1+)
   - Re-launches with correct version if needed

2. **Virtual Environment Management**:
   - Searches for virtual environments in common locations
   - Activates the environment if found

3. **Dependency Checking**:
   - Verifies Python installation
   - Checks for Streamlit and installs if missing

4. **Application Launch**:
   - Executes the Streamlit application

## API Integration

### Nextcloud API Endpoints

1. **Register App Password**:
   - Endpoint: `/ocs/v2.php/core/getapppassword`
   - Method: GET
   - Authentication: Basic Auth (username/password)
   - Response: JSON containing the new app password

2. **Unregister App Password**:
   - Endpoint: `/ocs/v2.php/core/apppassword`
   - Method: DELETE
   - Authentication: Basic Auth (username/password)
   - Response: Success/failure status

### Request Flow

1. User submits form with credentials and operation type
2. Application constructs the appropriate API request:
   ```python
   headers = {
       'User-Agent': app_name,
       'OCS-APIRequest': 'true',
       'Accept': 'application/json'
   }
   auth = (username, password)
   ```
3. Request is sent to Nextcloud server using the requests library
4. Response is processed and displayed to the user

## Error Handling

The application implements comprehensive error handling:

1. **Input Validation**:
   - Checks for empty required fields
   - Provides clear error messages

2. **Network Errors**:
   - Timeout handling (30-second timeout)
   - Connection error handling

3. **HTTP Errors**:
   - Status code-specific error messages
   - Response content display for debugging

4. **General Exceptions**:
   - Catch-all for unexpected errors
   - User-friendly error messages

## Security Implementation

1. **Credential Handling**:
   - Passwords are masked in the UI
   - Credentials are only used for API requests and not stored
   - HTTPS is used for secure communication

2. **Response Handling**:
   - Generated app passwords are displayed once and not stored
   - Clear warnings to save passwords securely

## Streamlit UI Components

1. **Layout**:
   - Centered layout with sidebar for inputs
   - Main area for results and instructions

2. **Input Components**:
   - Text inputs for URL, username, and application name
   - Password input with masking
   - Radio buttons for operation selection

3. **Output Components**:
   - Expandable sections for request details
   - JSON/code blocks for responses
   - Success/error messages with appropriate styling
   - Warning messages for important information

## Performance Considerations

1. **Request Timeout**:
   - 30-second timeout for API requests to prevent hanging

2. **Error Recovery**:
   - Detailed error messages to help users troubleshoot issues

3. **UI Responsiveness**:
   - Spinner during API requests to indicate processing

## Extension Points

Areas where the application could be extended:

1. **Additional Operations**:
   - Listing existing app passwords
   - Modifying app password properties

2. **Enhanced Security**:
   - Two-factor authentication support
   - OAuth integration

3. **UI Improvements**:
   - Dark mode support
   - Localization
   - Mobile-friendly responsive design

4. **Persistence**:
   - Saving Nextcloud URL for future sessions
   - History of generated app passwords (with proper security)

## Development Environment Setup

1. **Required Tools**:
   - Python 3.6+
   - PowerShell 7.1+ (for Windows)
   - Code editor (VS Code recommended)

2. **Development Workflow**:
   - Clone repository
   - Create virtual environment
   - Install dependencies
   - Run with `streamlit run streamlit_app.py`
   - Streamlit will automatically reload on code changes

3. **Testing**:
   - Manual testing against a Nextcloud instance
   - Consider adding automated tests with pytest

## Troubleshooting Common Issues

1. **Connection Errors**:
   - Verify Nextcloud URL is correct and includes protocol (https://)
   - Check network connectivity
   - Ensure Nextcloud server is online

2. **Authentication Failures**:
   - Verify username and password
   - Check for special characters in password
   - Ensure account is not locked

3. **API Errors**:
   - Check Nextcloud version compatibility
   - Verify API endpoints are enabled
   - Review Nextcloud server logs

---

Copyright 2025 harokku999@gmail.com | MIT License