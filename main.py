import threading
import cv2
from deepface import DeepFace

# Global variables
face_match = False
lock = threading.Lock()  # Lock for thread-safe access

def check_face(frame, reference_img):
    global face_match
    try:
        # Perform face verification
        result = DeepFace.verify(frame, reference_img)
        
        # Update face_match variable with the result
        with lock:
            face_match = result['verified']
    except Exception as e:
        # Handle exceptions during face recognition
        print("Error in face recognition:", e)

def main():
    # Load reference image
    REFERENCE_IMG_PATH = "reference_file_path.jpg"
    reference_img = cv2.imread(REFERENCE_IMG_PATH)
    if reference_img is None:
        # Handle failure to load reference image
        print("Error: Failed to load reference image.")
        return

    # Open webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        # Handle failure to open camera
        print("Error: Failed to open camera.")
        return

    # Set webcam frame dimensions
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Initialize frame counter
    counter = 0

    while True:
        # Capture frame from webcam
        ret, frame = cap.read()
        if not ret:
            # Handle failure to capture frame
            print("Error: Failed to capture frame.")
            break

        # Perform face recognition every 30 frames
        if counter % 30 == 0:
            try:
                # Start a new thread for face recognition
                threading.Thread(target=check_face, args=(frame.copy(), reference_img.copy())).start()
            except Exception as e:
                # Handle errors in starting thread
                print("Error in starting thread:", e)
        
        # Increment frame counter
        counter += 1

        # Display match status on frame
        with lock:
            if face_match:
                cv2.putText(frame, "Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "NO Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # Display frame
        cv2.imshow("video", frame)

        # Check for key press to quit
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Release webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Call main function
    main()
