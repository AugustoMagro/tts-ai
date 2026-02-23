from kokoro import KPipeline
import soundfile as sf
import numpy as np

def audio_generator(text: str, voice) -> str:
    lang_code = "p"
    pipeline = KPipeline(lang_code=lang_code, repo_id='hexgrad/Kokoro-82M')

    audio_chunks = []

    generator = pipeline(text, voice=voice)
    for _, _, audio in generator:
        audio_chunks.append(audio)

    audio_completo = np.concatenate(audio_chunks)
    sf.write("audio.wav", audio_completo, 24000)
    return "Audio gravado"