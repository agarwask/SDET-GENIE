from NorenRestApiPy.NorenApi import NorenApi




# STEP 1 : Get secret key and whitelist your IP from the below URL
# https://trade.shoonya.com/


# STEP 2 : Install the NorenRestApiOAuth package using pip
# pip install NorenRestApiOAuth


# STEP 3 : Get the auth code by visiting the below URL in browser and login with your credentials
# https://trade.shoonya.com/OAuthlogin/investor-entry-level/login?api_key=FAXXXXX_U&route_to=FAXXXXX


#credentials

auth_code = "" # replace with the auth code you in  redirect url
user_id =  'FAXXXXX'   # replace with your user id, which is same as client id without _U at the end


cred = {
    'client_id': f'{user_id}_U',
    'Secret_Code': 'secret_key_from_shoonya_dashboard', # replace with the secret key you get from shoonya api dashboard
    'UID': user_id,
    'oauth_url': f'https://api.shoonya.com/NorenWClientAPI/authenticate/{user_id}_U'
}



class NorenApiPy(NorenApi):
    def __init__(self):
        super().__init__(host='https://api.shoonya.com/NorenWClientAPI/', websocket='wss://api.shoonya.com/NorenWS/')

api = NorenApiPy()

# apikey_url = api.getOAuthURL(cred['oauth_url'],cred['client_id'])
# print(apikey_url)
result = api.getAccessToken(auth_code, cred['Secret_Code'], cred['client_id'], cred['UID'])
if result is not None:
    acc_tok, usrid, ref_tok, actid = result
    print(f"""\nAccess token is : {acc_tok} \nRefresh token is : {ref_tok} \nUser ID token is : {usrid} \nAccount ID is : {actid} \n""")
    # Update values
    cred['Access_token'] = acc_tok
    cred['Account_ID'] = actid
else:
    print("Failed to retrieve access token.")

print(cred)

# update headers with the access token
injected_headers = api.injectOAuthHeader(cred['Access_token'],cred['UID'],cred['Account_ID'])



# Place Order 

ret = api.place_order(buy_or_sell='B', product_type='C',
                        exchange='NSE', tradingsymbol='CANBK-EQ', 
                        quantity=1, discloseqty=0,price_type='LMT', price=127.00, trigger_price=0,
                        retention='DAY', remarks='my_order_001')
print(f'order response : {ret}' )


print("\n #################################")

# Order  Book
print(api.get_order_book())

print("\n #################################")

# Quotes  
print(api.get_quotes(exchange='NSE', token='26009'))







