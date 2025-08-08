# camera_debug.py
import cv2

def preview_camera(device_index=0):
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print("Unable to open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("OBS Preview", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()