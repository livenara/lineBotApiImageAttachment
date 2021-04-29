import requests

def lineApi(lineToken, message, image):
    
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + lineToken}

    if not image:
        # messageOnly
        requests.post(line_notify_api, data=payload, headers=headers)
    else:
        # messageAndImage
        files = {'imageFile': open(image, 'rb')}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

if __name__ == '__main__':

    lineToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    message = 'sendMessege'
    image = 'image.jpg' # or fullPath

    lineApi(lineToken, message, image)