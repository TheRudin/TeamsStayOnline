# TeamsStayOnline
This is the way to stay online in teams.

Make sure to replace <your_access_token> with your valid access token that has the necessary Microsoft Graph API permissions to update presence, and <your_user_id> with the ID of the user whose presence you want to manage.

To obtain an access token, you'll need to register an application in Azure Active Directory and request the required permissions for the Microsoft Graph API. Once you have the access token, you can use it in the script.

Please note that you need to handle obtaining the access token securely and programmatically refreshing it when it expires. Additionally, ensure that you comply with Microsoft's policies and guidelines when using the Microsoft Graph API.

## How to get User ID and Access Token

1. Register an application: Go to the Azure portal (https://portal.azure.com) and register a new application in Azure Active Directory (AAD). This registration will provide you with the necessary credentials to authenticate your script and obtain an access token.

2. Grant necessary permissions: In the Azure portal, navigate to your registered application and grant the required permissions to interact with the Microsoft Graph API. For this script, you'll need to grant the Presence.ReadWrite.All permission to manage presence.

3. Obtain the access token: To obtain the access token programmatically, you'll need to authenticate using the Microsoft Identity platform (formerly Azure AD v2.0). You can use the OAuth 2.0 client credentials grant flow to obtain the token. Here's an example of how you can obtain the access token using the requests library in Python:
```
import requests
import json

# Set your application's credentials
client_id = "<your_client_id>"
client_secret = "<your_client_secret>"
tenant_id = "<your_tenant_id>"

# Set the token endpoint URL
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Set the API scope and grant type
scope = "https://graph.microsoft.com/.default"
grant_type = "client_credentials"

# Make a POST request to the token endpoint to obtain the access token
response = requests.post(
    token_url,
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
        "grant_type": grant_type
    }
)

# Parse the response and extract the access token
access_token = response.json()["access_token"]
```

Replace <your_client_id>, <your_client_secret>, and <your_tenant_id> with your application's respective values.

4. Obtain the user ID: The user ID represents the user whose presence you want to manage. You can retrieve the user ID programmatically using the Microsoft Graph API. Here's an example of how you can retrieve the user ID using the access token:

```
# Set the user endpoint URL
user_url = "https://graph.microsoft.com/v1.0/me"

# Set the authorization header with the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Make a GET request to retrieve the user details
response = requests.get(user_url, headers=headers)

# Parse the response and extract the user ID
user_id = response.json()["id"]
```

Now you have the user ID and access token required to execute the script. Replace <your_user_id> and <your_access_token> in the script with the respective values you obtained.

© 2023 Kalenda Software Engineering. All rights reserved.
