import requests
from pywebio import start_server
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_html, put_image, put_buttons  # Import put_buttons
from pywebio import config

css="""
body{
background-color: black;
Color:red;
}
"""
@config(css_style=css)

def main():
    # Define phone number
    phone_number = input("Enter your phone number: ")

    # Define headers for the request
    head = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "ibiza.ooredoo.dz",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.3"
    }

    # Define data for the request with phone number
    data_request = {
        "client_id": "ibiza-app",
        "grant_type": "password",
        "mobile-number": phone_number,
        "language": "EN"
    }

    # Send the POST request to request OTP
    response_request_otp = requests.post('https://ibiza.ooredoo.dz/auth/realms/ibiza/protocol/openid-connect/token', headers=head, data=data_request)

    # Check if the request was successful
    otp = input("Enter the OTP sent to your phone: ")  # Ask user to input the OTP

    # Define data for the request with phone number and OTP
    data_login = {
        "client_id": "ibiza-app",
        "grant_type": "password",
        "mobile-number": phone_number,
        "otp": otp,  # Include the OTP entered by the user
        "language": "EN"
    }

    # Send the POST request to get the access token
    response_login = requests.post('https://ibiza.ooredoo.dz/auth/realms/ibiza/protocol/openid-connect/token', headers=head, data=data_login)

    # Extract token from the response
    token = response_login.json().get('access_token')

    if token:
        print("Token obtained successfully!")

        # Define headers for the second request with the token
        head_with_token = {
            "Authorization": f"Bearer {token}",
            "language": "EN",
            "request-id": "73947089-ba6b-46d6-83fd-b3d3a8962889",
            "flavour-type": "gms",
            "Content-Type": "application/json; charset=utf-8",
            "Content-Length": "32",
            "Host": "ibiza.ooredoo.dz",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.3"
        }

        # Define data for the second request
        data_second_request = {
            "skipMgm": False,
            "mgmValue": "0.1.0.1.0.1.0"
        }

        # Send the POST request with the access token
        response_second_request = requests.post('https://ibiza.ooredoo.dz/api/v1/mobile-bff/users/mgm/info/apply', headers=head_with_token, json=data_second_request)

        # Define the function to handle the button click
        def reactivate_service():
            # Send the POST request again with the same parameters
            response_second_request = requests.post('https://ibiza.ooredoo.dz/api/v1/mobile-bff/users/mgm/info/apply', headers=head_with_token, json=data_second_request)
            # Print the response
            print(response_second_request.json())
            put_text("Service reactivated successfully!")
        
        # Add a button for reactivating the service
        put_buttons(['Reactivate Service'], [reactivate_service])

        put_image('https://media.tenor.com/6UTiFXjmSOAAAAAM/internet-cancel.gif ', width='100%')

        put_text("تمت العملية بنجاح 1 جيقا 😍😍")
    else:
        print("Failed to obtain token.")

if name == 'main':
    start_server(main, port=8080)