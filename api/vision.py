from google.cloud import vision
import os

client = vision.ImageAnnotatorClient()

class Vision:
    def __init__(self):
      self.status = "TEXT"
    def detect_text(path):
        client = vision.ImageAnnotatorClient()

        # [START vision_python_migration_text_detection]
        with open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print("Texts:")

        for text in texts:
            return text.description

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
