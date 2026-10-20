import json
import time


class AttendanceManager:
    def __init__(self, threshold=5.0, max_gap=1.0,
                 log_path="attendance_log.json"):
        self.threshold = threshold  # seconds needed to count as present
        self.max_gap = max_gap      # bigger gaps are not counted
        self.log_path = log_path
        self.records = {}

    def update(self, tracked):
        for t in tracked:
            pid, ts = t["id"], t["timestamp"]
            r = self.records.setdefault(pid, {
                "id": pid,
                "first_seen": ts,
                "last_seen": ts,
                "presence_seconds": 0.0,
                "status": "absent",
            })
            gap = ts - r["last_seen"]
            if 0 < gap <= self.max_gap:
                r["presence_seconds"] += gap
            r["last_seen"] = ts
            if r["presence_seconds"] >= self.threshold:
                r["status"] = "present"

    def get(self, pid):
        return self.records.get(pid)

    def save(self):
        out = []
        for r in self.records.values():
            out.append({
                "participant_id": r["id"],
                "first_seen": time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(r["first_seen"])),
                "last_seen": time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(r["last_seen"])),
                "presence_seconds": round(r["presence_seconds"], 1),
                "status": r["status"],
            })
        with open(self.log_path, "w") as f:
            json.dump(out, f, indent=2)