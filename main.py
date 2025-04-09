import face_recognition
import os

# Load the target image (Beyoncé)
target_image = face_recognition.load_image_file("beyonce_target.jpg")
target_encoding = face_recognition.face_encodings(target_image)[0]

# Directory with test images
test_dir = "test_images"

for filename in os.listdir(test_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(test_dir, filename)
        test_image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(test_image)

        if encodings:
            result = face_recognition.compare_faces([target_encoding], encodings[0])
            print(f"{filename}: {'MATCH'
