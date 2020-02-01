# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def detect_objects(img_content):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=img_content)

    # Performs label detection on the image file
    objects = client.object_localization(
        image=image).localized_object_annotations

    object_list = []
    for object_ in objects:
        object_list.append({"name": object_.name, "confidence": object_.score})

    return object_list
