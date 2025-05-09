# Nextcloud App Password API Documentation

This document provides detailed information about the Nextcloud API endpoints used by the Nextcloud App Password Manager application.

## Overview

The Nextcloud App Password Manager interacts with the Nextcloud OCS (Open Collaboration Services) API to manage application passwords. The application uses two main endpoints:

1. Register a new application password
2. Unregister (delete) an existing application password

All API requests use HTTP Basic Authentication with the user's Nextcloud credentials.

## API Base URL

The base URL for all API requests is the user's Nextcloud instance URL, for example:

```
https://nextcloud.example.com
```

## API Endpoints

### 1. Register a New Application Password

Creates a new application password for the authenticated user.

**Endpoint:** `/ocs/v2.php/core/getapppassword`

**Method:** GET

**Headers:**
- `User-Agent`: Application name (provided by the user)
- `OCS-APIRequest`: true
- `Accept`: application/json

**Authentication:**
- Basic Authentication using Nextcloud username and password

**Request Example:**

```http
GET /ocs/v2.php/core/getapppassword HTTP/1.1
Host: nextcloud.example.com
User-Agent: MyApplication
OCS-APIRequest: true
Accept: application/json
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

**Successful Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "ocs": {
    "meta": {
      "status": "ok",
      "statuscode": 200,
      "message": "OK"
    },
    "data": {
      "apppassword": "a8n7d9x6b5c4v3m2l1k0j"
    }
  }
}
```

**Response Parameters:**
- `apppassword`: The generated application password that should be used for authentication in the application

**Error Responses:**

- **401 Unauthorized**: Authentication failed
  ```json
  {
    "ocs": {
      "meta": {
        "status": "failure",
        "statuscode": 401,
        "message": "Unauthorized"
      },
      "data": []
    }
  }
  ```

- **403 Forbidden**: User doesn't have permission
  ```json
  {
    "ocs": {
      "meta": {
        "status": "failure",
        "statuscode": 403,
        "message": "Forbidden"
      },
      "data": []
    }
  }
  ```

### 2. Unregister an Application Password

Deletes an existing application password.

**Endpoint:** `/ocs/v2.php/core/apppassword`

**Method:** DELETE

**Headers:**
- `User-Agent`: Application name (provided by the user)
- `OCS-APIRequest`: true
- `Accept`: application/json

**Authentication:**
- Basic Authentication using Nextcloud username and password

**Request Example:**

```http
DELETE /ocs/v2.php/core/apppassword HTTP/1.1
Host: nextcloud.example.com
User-Agent: MyApplication
OCS-APIRequest: true
Accept: application/json
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

**Successful Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "ocs": {
    "meta": {
      "status": "ok",
      "statuscode": 200,
      "message": "OK"
    },
    "data": []
  }
}
```

**Error Responses:**

- **401 Unauthorized**: Authentication failed
  ```json
  {
    "ocs": {
      "meta": {
        "status": "failure",
        "statuscode": 401,
        "message": "Unauthorized"
      },
      "data": []
    }
  }
  ```

- **404 Not Found**: Application password not found
  ```json
  {
    "ocs": {
      "meta": {
        "status": "failure",
        "statuscode": 404,
        "message": "Not Found"
      },
      "data": []
    }
  }
  ```

## Implementation Notes

### Authentication

The application uses HTTP Basic Authentication for all API requests. The username and password are encoded in base64 and included in the Authorization header:

```python
auth = (username, password)
```

The requests library handles the encoding automatically:

```python
response = requests.get(url, headers=headers, auth=auth)
```

### User-Agent Header

The User-Agent header is set to the application name provided by the user. This helps identify the application in the Nextcloud security settings:

```python
headers = {
    'User-Agent': app_name,
    'OCS-APIRequest': 'true',
    'Accept': 'application/json'
}
```

### Response Handling

The application parses the JSON response to extract the application password:

```python
json_res = response.json()
if json_res["ocs"]["data"]["apppassword"]:
    app_password = json_res["ocs"]["data"]["apppassword"]
```

### Error Handling

The application handles various HTTP error codes with specific messages:

```python
if e.response.status_code == 401:
    error_message += "\nAuthentication failed. Please check your username and password."
elif e.response.status_code == 403:
    error_message += "\nAccess forbidden. You may not have permission to access this resource."
elif e.response.status_code == 404:
    error_message += "\nResource not found. Please check the URL."
```

## Additional Nextcloud API Resources

For more information about the Nextcloud API, refer to the official documentation:

- [Nextcloud OCS API Documentation](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/OCS/index.html)
- [Nextcloud User Authentication API](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/LoginFlow/index.html)

## Security Considerations

- Always use HTTPS for API requests to ensure credentials are encrypted
- Store application passwords securely
- Revoke application passwords when they are no longer needed
- Consider implementing additional security measures like IP restrictions or two-factor authentication

---

Copyright 2025 harokku999@gmail.com | MIT License