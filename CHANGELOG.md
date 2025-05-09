# Changelog

All notable changes to the Nextcloud App Password Manager will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### UnPlanned Features
- List all existing application passwords
- Batch operations for multiple passwords
- Dark mode support
- Localization support
- Configuration file for default settings
- Session persistence for Nextcloud URL
- Enhanced error reporting with troubleshooting suggestions
- Support for two-factor authentication
- OAuth integration
- Mobile-friendly responsive design
- Command-line interface option

---

Copyright 2025 harokku999@gmail.com | MIT License