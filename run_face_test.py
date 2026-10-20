import cv2
from backend.core.face_detection import FaceDetector
from backend.core.face_tracker import FaceTracker
from backend.core.attendance import AttendanceManager

detector = FaceDetector()
tracker = FaceTracker()
attendance = AttendanceManager(threshold=5.0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    tracked = tracker.update(detector.process_frame(frame))
    attendance.update(tracked)
    for t in tracked:
        x, y, w, h = t["bbox"]
        r = attendance.get(t["id"])
        label = f"ID {t['id']} {r['presence_seconds']:.0f}s {r['status']}"
        color = (0, 255, 0) if r["status"] == "present" else (0, 165, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

attendance.save()
cap.release()
cv2.destroyAllWindows()