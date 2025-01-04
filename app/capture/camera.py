import cv2

def capture_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_frame.jpg", frame)
    cap.release()
    return "captured_frame.jpg"