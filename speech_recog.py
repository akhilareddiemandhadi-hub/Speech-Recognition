import speech_recognition as sr
from pydub import AudioSegment

# Convert your recorded file to PCM WAV first
# If you recorded "sample.wav" with Voice Recorder, convert it:
sound = AudioSegment.from_file("sample.wav")  # works even if it's M4A/WMA
sound = sound.set_frame_rate(16000).set_channels(1).set_sample_width(2)
sound.export("sample_pcm.wav", format="wav")

# Now use the PCM file
r = sr.Recognizer()
with sr.AudioFile("sample_pcm.wav") as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand")