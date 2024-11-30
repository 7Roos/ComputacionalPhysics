import torch
from TTS.api import TTS

# Get device
import subprocess

device = "cuda" if torch.cuda.is_available() else "cpu"


# Listar modelos
def listar_modelos():
    """Lista os modelos disponíveis do Coqui TTS."""
    resultado = subprocess.run(["tts", "--list_models"], capture_output=True, text=True)
    print(resultado.stdout)


# listar_modelos()


def generate_audio(text, model_name, output_path):
    """Generates audio from text using the specified model.

    Args:
      text: The text to be converted to audio.
      model_name: The name of the model to use.
      output_path: The path to save the output audio file.
    """

    tts = TTS(model_name=model_name).to(device)
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path


# Example usage:
text = "If you want to use this script, modify it to your needs, or refactor it (there are things to improve), I made this project available on GitHub (link in the description). Happy installation!"

model_name = "tts_models/en/ljspeech/vits"
output_path = "12_end.wav"

generate_audio(text, model_name, output_path)

# Bons modelos:
#tts_models/en/ljspeech/tacotron2-DDC
#tts_models/en/ljspeech/tacotron2-DDC_ph 
#tts_models/en/ljspeech/vits - melhor performance com dicção