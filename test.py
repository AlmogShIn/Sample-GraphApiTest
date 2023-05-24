client_id = os.getenv('AZURE_CLIENT_ID')
    tenant_id = os.getenv('AZURE_TENANT_ID')
    client_secret = os.getenv('AZURE_CLIENT_SECRET')
    azure_token = os.getenv('AZURE_TOKEN')

    msal_auth = f"https://login.microsoftonline.com/{tenant_id}"

    msl_scope = ["https://graph.microsoft.com/User.Read.All"]

    msl_app = ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=msal_auth
    )


    result = msl_app.acquire_token_silent(
        scopes=msl_scope,
        account=None
    )
    if not result:
        result = msl_app.acquire_token_for_client(scopes=msl_scope)

    headers = {
        "Authorization": f"Bearer {azure_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        url="https://graph.microsoft.com/v1.0/users/tamir.zitman@intel.com/transitiveMemberOf/microsoft.graph.group?$count=true",
        headers=headers

    )
    json_res = json.dumps(response.json(), indent=4)
    print(json_res)