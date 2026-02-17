import cv2
import os
import numpy as np

dataset_path = "dataset"

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
labels = []
names = []
label_id = 0

print("Training started...\n")

# -------------------- LOAD DATASET -------------------- #
for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)

    if not os.path.isdir(folder_path):
        continue

    names.append(folder_name)

    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected_faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
            faces.append(face)
            labels.append(label_id)

    print(f"{folder_name} trained")
    label_id += 1

faces = np.array(faces)
labels = np.array(labels)

print("\nTotal faces trained:", len(faces))

# -------------------- TRAIN MODEL -------------------- #
recognizer = cv2.face.LBPHFaceRecognizer_create(
    radius=1,
    neighbors=8,
    grid_x=8,
    grid_y=8
)

recognizer.train(faces, labels)

print("\nTraining completed")
print("Recognition Started")
print("Press 's' to save screenshot")
print("Press 'q' to quit")

# -------------------- SCREENSHOT SETUP -------------------- #
os.makedirs("screenshots", exist_ok=True)
screenshot_count = 0

# -------------------- START CAMERA -------------------- #
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in detected:
        face = gray_frame[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        # LOWER confidence = better match
        if confidence < 65:
            text = names[label]
            color = (0, 255, 0)
        else:
            text = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame,
                    f"{text} ({int(confidence)})",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2)

    cv2.imshow("Face Recognition Tool", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save screenshot
    if key == ord('s'):
        filename = f"screenshots/screenshot_{screenshot_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        screenshot_count += 1

    # Press 'q' to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
