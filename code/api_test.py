import requests
import base64
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'ojHPqhcn9kRejlZPHJC7rGGEwcK2kl6MZRtOgF12nFa4Qmy4RZ'

# Set the API endpoint for identification
identification_url = 'https://api.plant.id/v2/identify'

# Set the API endpoint for retrieving identification results
get_result_url = 'https://api.plant.id/v2/get_identification_result/'

def make_identification_request(images_base64, latitude=None, longitude=None, modifiers=None, plant_details=None):
    # Prepare the payload
    payload = {
        'images': images_base64,
        'latitude': latitude,
        'longitude': longitude,
        'modifiers': modifiers,
        'plant_details': plant_details
    }

    # Set up the headers with the API key
    headers = {'Api-Key': api_key}

    # Make a POST request to the identification endpoint
    response = requests.post(identification_url, headers=headers, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and return the identification response
        return response.json()
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def get_identification_result(identification_id):
    # Set up the headers with the API key
    headers = {'Api-Key': api_key}

    # Make a POST request to the get result endpoint
    response = requests.post(get_result_url + identification_id, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and return the identification result
        return response.json()
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
    
def get_most_probable_plant(response_data):
    # Parse the JSON response
    

    # Check if suggestions are present in the response
    if 'suggestions' in response_data and len(response_data['suggestions']) > 0:
        # Get the suggestion with the highest probability
        most_probable_suggestion = max(response_data['suggestions'], key=lambda x: x['probability'])

        # Return the plant_name of the most probable suggestion
        return most_probable_suggestion['plant_name']
    else:
        # Return None if no suggestions are available
        return None

# Example usage
# Encode an image as base64 (replace 'path/to/your/image.jpg' with the actual path to your image file)
with open('images/lettuce.jpg', 'rb') as image_file:
    images_base64 = [base64.b64encode(image_file.read()).decode('utf-8')]

# Make the identification request
identification_response = make_identification_request(images_base64, latitude=12.34, longitude=56.78, modifiers=['speed'], plant_details=['common_names'])

if identification_response:
    # Get the identification ID from the response
    identification_id = identification_response['id']
    
    # Get the identification result asynchronously
    result = get_identification_result(str(identification_id))

    if result:
        print(f"YOUR PLANT IS: {get_most_probable_plant(result)}")
    else:
        print("NO PLANT FOR YOU MOTHERFUCKER")
