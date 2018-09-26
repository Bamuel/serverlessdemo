import boto3
import json
import base64



# create the Rekognition boto3 client
rekognition_client=boto3.client('rekognition', region_name="ap-southeast-2")

def lambda_handler(event, context):
    # get the base64-encoded image from the event and convert it back to binary
    binary_image = base64.decodestring(event['picture'].encode())
    
    # make the call to RecognizeCelebrities API
    response = rekognition_client.recognize_celebrities(
        Image={
            'Bytes': binary_image
        }
    )
    # get the response from the API call and return only the first result
    if len(response['CelebrityFaces']) == 0:
        return {
            'name': None,
            'confidence': 'NaN',
            'link': 'NaN'
        }
    else:
        return {
            #Todo add a for loop with the max len(response['CelebrityFaces']) then make it generate through a for loop
            #I wish i could do this but im struggling with the Python Syntax
            #and i want to use my time on the other questions
            'name': response['CelebrityFaces'][0]['Name'],
            'confidence': response['CelebrityFaces'][0]['MatchConfidence'],
            'link': response['CelebrityFaces'][0]['Urls'],
            'name1': response['CelebrityFaces'][1]['Name'],
            'confidence1': response['CelebrityFaces'][1]['MatchConfidence'],
            'link1': response['CelebrityFaces'][1]['Urls']
        }
    
