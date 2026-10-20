# run_fusion_test.py
from backend.core.signal_fusion import SignalFusion
import time

fusion = SignalFusion()

print("Testing Signal Fusion...")

# First snapshot of data
vision1 = {"face_count": 1, "movement": "low"}
audio1 = {"label": "speech", "db": -45}
result1 = fusion.sync_signals(vision1, audio1)
print("Data 1:", result1)

time.sleep(1) # wait 1 second to see the timestamp change

# Second snapshot of data
vision2 = {"face_count": 1, "movement": "high"}
audio2 = {"label": "silence", "db": -80}
result2 = fusion.sync_signals(vision2, audio2)
print("Data 2:", result2)