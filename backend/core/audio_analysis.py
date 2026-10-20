import numpy as np


class AudioAnalyzer:
    def __init__(self, silence_db=-60, speech_db=-35):
        self.silence_db = silence_db  # below this = silence
        self.speech_db = speech_db    # above this = active speech
        self.history = []

    def classify(self, feature):
        db = feature["db"]
        if db < self.silence_db:
            return "silence"
        if db < self.speech_db:
            return "background_noise"
        return "speech"

    def add(self, feature):
        label = self.classify(feature)
        self.history.append({**feature, "label": label})
        return label

    def summary(self):
        if not self.history:
            return None
        dbs = np.array([h["db"] for h in self.history])
        labels = [h["label"] for h in self.history]
        n = len(labels)
        return {
            "avg_noise_db": round(float(dbs.mean()), 1),
            "amplitude_variation": round(float(dbs.std()), 2),
            "silence_ratio": round(labels.count("silence") / n, 2),
            "noise_ratio": round(labels.count("background_noise") / n, 2),
            "speech_ratio": round(labels.count("speech") / n, 2),
            "speech_segments": self._count_segments(labels),
        }

    def _count_segments(self, labels):
        count, prev = 0, False
        for l in labels:
            is_speech = l == "speech"
            if is_speech and not prev:
                count += 1
            prev = is_speech
        return count