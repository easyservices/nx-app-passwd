# Nextcloud App Password Manager - User Guide

This guide provides step-by-step instructions for using the Nextcloud App Password Manager to create and manage application passwords for your Nextcloud account.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Registering a New App Password](#registering-a-new-app-password)
4. [Unregistering an Existing App Password](#unregistering-an-existing-app-password)
5. [Understanding the Results](#understanding-the-results)
6. [Troubleshooting](#troubleshooting)
7. [Frequently Asked Questions](#frequently-asked-questions)

## Introduction

Nextcloud App Password Manager is a tool that helps you create and manage application-specific passwords for your Nextcloud account. These passwords allow third-party applications to access your Nextcloud account without using your main password, enhancing security by limiting access and allowing you to revoke specific application access when needed.

## Getting Started

### Launching the Application

1. Open a terminal or PowerShell window
2. Navigate to the application directory
3. Run the application using the provided script:

   ```
   .\runMe.ps1
   ```

   Or manually with:

   ```
   streamlit run streamlit_app.py
   ```

4. The application will open in your default web browser at http://localhost:8501

![Application Launch](https://via.placeholder.com/800x450.png?text=Application+Launch)

### Understanding the Interface

The application interface consists of two main sections:

1. **Sidebar** (left): Contains input fields and operation selection
2. **Main Panel** (right): Displays results, instructions, and application information

![Application Interface](https://via.placeholder.com/800x450.png?text=Application+Interface)

## Registering a New App Password

Follow these steps to create a new application password:

1. **Enter Nextcloud Information**:
   - In the sidebar, enter your Nextcloud URL (e.g., https://nextcloud.example.com)
   - Enter your Nextcloud username
   - Enter your Nextcloud password
   - Provide a name for the application (this will appear in your Nextcloud security settings)

   ![Enter Information](https://via.placeholder.com/800x450.png?text=Enter+Information)

2. **Select Operation**:
   - Ensure "Register a new app" is selected in the operation radio buttons

   ![Select Register Operation](https://via.placeholder.com/800x450.png?text=Select+Register+Operation)

3. **Submit Request**:
   - Click the "Submit Request" button
   - The application will display a spinner while processing your request

   ![Submit Request](https://via.placeholder.com/800x450.png?text=Submit+Request)

4. **View Results**:
   - If successful, you'll see a success message and the response from Nextcloud
   - Your new application password will be displayed in a highlighted box
   - **IMPORTANT**: Copy and save this password immediately as it will not be shown again

   ![Registration Success](https://via.placeholder.com/800x450.png?text=Registration+Success)

5. **Save Your Password**:
   - Store the generated password securely
   - Use this password in your application instead of your main Nextcloud password

## Unregistering an Existing App Password

To revoke an existing application password:

1. **Enter Nextcloud Information**:
   - In the sidebar, enter your Nextcloud URL
   - Enter your Nextcloud username
   - Enter your Nextcloud password
   - Enter the name of the application whose password you want to revoke

   ![Enter Information](https://via.placeholder.com/800x450.png?text=Enter+Information)

2. **Select Operation**:
   - Select "Unregister an existing app" in the operation radio buttons

   ![Select Unregister Operation](https://via.placeholder.com/800x450.png?text=Select+Unregister+Operation)

3. **Submit Request**:
   - Click the "Submit Request" button
   - The application will display a spinner while processing your request

   ![Submit Unregister Request](https://via.placeholder.com/800x450.png?text=Submit+Unregister+Request)

4. **View Results**:
   - If successful, you'll see a success message and the response from Nextcloud
   - The application password has now been revoked and can no longer be used

   ![Unregistration Success](https://via.placeholder.com/800x450.png?text=Unregistration+Success)

## Understanding the Results

### Request Details

The "Request Details" section shows information about your request:
- The URL being accessed
- The User-Agent (application name) being used
- The username being authenticated
- The operation being performed

![Request Details](https://via.placeholder.com/800x450.png?text=Request+Details)

### Response

The "Response" section shows the raw response from the Nextcloud server:
- For successful requests, this will be a JSON object with status information
- For registration requests, this includes the generated application password
- For errors, this may contain additional information about what went wrong

![Response Details](https://via.placeholder.com/800x450.png?text=Response+Details)

## Troubleshooting

### Common Error Messages

1. **"All fields are required"**
   - Ensure you've filled in all the required fields in the sidebar

2. **"The request timed out after 30 seconds"**
   - Check your internet connection
   - Verify that your Nextcloud server is online and responsive

3. **"Could not connect to the server"**
   - Verify that the Nextcloud URL is correct and includes the protocol (https://)
   - Check your internet connection
   - Ensure your Nextcloud server is online

4. **"Authentication failed"**
   - Double-check your username and password
   - Ensure your account is not locked or disabled

5. **"Access forbidden"**
   - Your account may not have permission to create application passwords
   - Contact your Nextcloud administrator

### Checking Your Nextcloud Settings

You can verify application passwords in your Nextcloud account:

1. Log in to your Nextcloud account in a web browser
2. Go to Settings > Security
3. Scroll down to the "Devices & sessions" section
4. You should see your applications listed here
5. You can manually revoke access here as well

## Frequently Asked Questions

### What is an application password?

An application password is a special password that gives a specific application access to your Nextcloud account. Unlike your main password, app passwords:
- Can be revoked individually without changing your main password
- Are specific to one application
- Provide better security by limiting what the application can access

### Why use application passwords?

Application passwords enhance security by:
- Allowing you to revoke access for a specific application without affecting others
- Preventing third-party applications from storing your main password
- Creating an audit trail of which applications are accessing your account

### How secure are application passwords?

Application passwords are as secure as your main account. They provide:
- The same level of encryption as your main password
- The ability to be revoked if compromised
- Limited scope to specific applications

### Can I see my application passwords again after creation?

No, for security reasons, application passwords are only displayed once at the time of creation. If you lose an application password, you'll need to create a new one and update your application.

### How many application passwords can I create?

Nextcloud does not impose a specific limit on the number of application passwords you can create. However, it's good practice to:
- Only create passwords for applications you actively use
- Regularly review and revoke unused application passwords

---

Copyright 2025 harokku999@gmail.com | MIT License