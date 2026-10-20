import json
from backend.core.audio_capture import AudioCapture

audio = AudioCapture()
log = []
print("Recording 10 seconds. Talk, then stay quiet...")
for _ in range(10):
    chunk = audio.record_chunk()
    f = audio.extract_features(chunk)
    log.append(f)
    print(f)

with open("audio_features.json", "w") as fp:
    json.dump(log, fp, indent=2)
print("Saved audio_features.json")