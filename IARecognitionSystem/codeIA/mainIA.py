import cv2
from simple_facerec import SimpleFacerec

# Encode images from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("Images/")

# Load the camera try 1 or 0 if a camera on the computer otherwise, 2, 3...
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Face detection
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Shows the person's name
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

        # Displays the rectangle around the detected face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
    # Allows you to open the small window (camera return)
    cv2.imshow("Frame", frame)

    # Allows exit from the loop using the ascii 27 (esc) key
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()