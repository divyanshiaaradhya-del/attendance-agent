import time
import numpy as np
import sounddevice as sd
import librosa


class AudioCapture:
    def __init__(self, sample_rate=16000, chunk_seconds=1.0):
        self.sample_rate = sample_rate
        self.chunk_seconds = chunk_seconds

    def record_chunk(self):
        frames = int(self.sample_rate * self.chunk_seconds)
        ts = time.time()
        data = sd.rec(frames, samplerate=self.sample_rate,
                      channels=1, dtype="float32")
        sd.wait()
        return {"timestamp": ts, "samples": data[:, 0]}

    def extract_features(self, chunk):
        y = chunk["samples"]
        rms = float(librosa.feature.rms(y=y).mean())
        return {
            "timestamp": chunk["timestamp"],
            "amplitude_rms": round(rms, 5),
            "peak": round(float(np.max(np.abs(y))), 5),
            "db": round(20 * np.log10(rms + 1e-10), 1),
        }