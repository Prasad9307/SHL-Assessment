import whisper
import language_tool_python

# Load Whisper and LanguageTool
model = whisper.load_model("base")
tool = language_tool_python.LanguageTool('en-US')

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

def check_grammar(text):
    matches = tool.check(text)
    return matches

def calculate_score(text, issues):
    words = len(text.split())
    if words == 0:
        return 0
    error_density = len(issues) / words
    score = max(0, 5 * (1 - error_density))  # Scale to 0-5
    return score
