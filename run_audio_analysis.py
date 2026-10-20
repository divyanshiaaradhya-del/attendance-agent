import json
from backend.core.audio_capture import AudioCapture
from backend.core.audio_analysis import AudioAnalyzer

audio = AudioCapture()
analyzer = AudioAnalyzer()
print("Recording 15 seconds. Talk, pause, talk again...")
for _ in range(15):
    f = audio.extract_features(audio.record_chunk())
    label = analyzer.add(f)
    print(f["db"], label)

result = {"summary": analyzer.summary(), "segments": analyzer.history}
with open("audio_analysis.json", "w") as fp:
    json.dump(result, fp, indent=2)
print(result["summary"])