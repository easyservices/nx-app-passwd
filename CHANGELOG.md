# Changelog

All notable changes to the Nextcloud App Password Manager & HTTP Bearer Token Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-05-30

### Added
- **New Application**: HTTP Bearer Basic Auth Token Generator (`streamlit_http_bearer_gen.py`)
  - Generate Bearer tokens from username/password combinations
  - Real-time token testing against API endpoints
  - Support for multiple HTTP methods (GET, POST, PUT, DELETE)
  - Code examples in Python, JavaScript, and cURL
  - Detailed response analysis and debugging
  - Token validation and error handling
- **Enhanced PowerShell Launchers**:
  - Renamed and specialized PowerShell scripts:
    - `start_nx_app_pass.ps1` - Launches Nextcloud App Password Manager
    - `start_http_bearer_app.ps1` - Launches HTTP Bearer Token Generator
  - Improved virtual environment detection and activation
  - Automatic dependency installation from `requirements.txt`
  - Better error handling and user feedback
- **Project Structure Improvements**:
  - Added `requirements-dev.txt` for development dependencies
  - Enhanced project documentation and file organization
  - Updated copyright and licensing information

### Changed
- **Project Scope**: Expanded from single-purpose to dual-purpose authentication toolkit
- **File Naming**: Renamed main application file from `streamlit_app.py` to `streamlit_nx_app_pass.py`
- **Documentation**: Comprehensive README.md update reflecting new dual-application structure
- **Dependencies**: Updated and pinned dependency versions for better stability

### Enhanced
- **User Experience**: Improved UI consistency across both applications
- **Error Handling**: Enhanced error reporting and user guidance in both tools
- **Security**: Added comprehensive input validation and secure credential handling

## [1.0.0] - 2025-05-09

### Added
- Initial release of the Nextcloud App Password Manager
- Support for registering new application passwords
- Support for unregistering existing application passwords
- User-friendly web interface built with Streamlit
- PowerShell script for easy application launching
- Automatic virtual environment detection
- Comprehensive error handling and user feedback
- Detailed request and response information display
- Secure password handling with masked input fields
- Clear instructions and user guidance
- MIT License and copyright information

### Security
- Secure handling of credentials (not stored, only used for API requests)
- Password masking in the UI
- HTTPS communication with Nextcloud server
- Clear warnings about saving generated passwords securely

## [Unreleased]

### Planned Features
- **Nextcloud App Password Manager**:
  - List all existing application passwords
  - Batch operations for multiple passwords
  - Support for two-factor authentication
  - OAuth integration
  - Session persistence for Nextcloud URL
- **HTTP Bearer Token Generator**:
  - Support for other authentication methods (API keys, JWT tokens)
  - Token expiration tracking and renewal
  - Bulk token generation for multiple services
  - Token storage and management
- **Common Features**:
  - Dark mode support
  - Localization support (multiple languages)
  - Configuration file for default settings
  - Enhanced error reporting with troubleshooting suggestions
  - Mobile-friendly responsive design
  - Command-line interface option
  - Docker containerization
  - Web-based deployment options

---

Copyright 2025 harokku999@gmail.com | MIT License