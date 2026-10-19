import cv2
from backend.core.face_detection import FaceDetector
from backend.core.face_tracker import FaceTracker

detector = FaceDetector()
tracker = FaceTracker()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    tracked = tracker.update(detector.process_frame(frame))
    for t in tracked:
        x, y, w, h = t["bbox"]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {t['id']}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Face Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()