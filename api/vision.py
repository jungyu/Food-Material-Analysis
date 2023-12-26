from google.cloud import vision
import os

client = vision.ImageAnnotatorClient()

class Vision:
    def __init__(self):
      self.status = "TEXT"
    def detect_text(url_path):
      print(url_path)
