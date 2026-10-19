import math
import time


class FaceTracker:
    def __init__(self, max_distance=80, max_missing=15):
        self.next_id = 1
        self.tracks = {}  # id -> {"center", "bbox", "missing"}
        self.max_distance = max_distance
        self.max_missing = max_missing

    def update(self, detections):
        now = time.time()
        results = []
        used_ids = set()

        for d in detections:
            x, y, w, h = d["bbox"]
            center = (x + w / 2, y + h / 2)

            best_id, best_dist = None, self.max_distance
            for tid, t in self.tracks.items():
                if tid in used_ids:
                    continue
                dist = math.dist(center, t["center"])
                if dist < best_dist:
                    best_id, best_dist = tid, dist

            if best_id is None:
                best_id = self.next_id
                self.next_id += 1

            used_ids.add(best_id)
            self.tracks[best_id] = {
                "center": center,
                "bbox": (x, y, w, h),
                "missing": 0,
            }
            results.append(
                {"id": best_id, "bbox": (x, y, w, h), "timestamp": now}
            )

        for tid in list(self.tracks):
            if tid not in used_ids:
                self.tracks[tid]["missing"] += 1
                if self.tracks[tid]["missing"] > self.max_missing:
                    del self.tracks[tid]

        return results