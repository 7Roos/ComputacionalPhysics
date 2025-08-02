import torch
from TTS.api import TTS
import os
import subprocess # Get device
import warnings # No início do seu script principal
import sys

# Salvar stderr original
original_stderr = sys.stderr
# Redirecionar stderr para /dev/null
sys.stderr = open(os.devnull, 'w')

# Suprimir apenas os avisos do FutureWarning para torch.load
#warnings.filterwarnings("ignore", message=".*torch.load.*weights_only=False.*", category=FutureWarning)


device = "cuda" if torch.cuda.is_available() else "cpu"


# Listar modelos
def listar_modelos():
    """Lista os modelos disponíveis do Coqui TTS."""
    resultado = subprocess.run(["tts", "--list_models"], capture_output=True, text=True)
    print(resultado.stdout)


def generate_audio(text, model_name, output_path):
    """Generates audio from text using the specified model.

    Args:
      text: The text to be converted to audio.
      model_name: The name of the model to use.
      output_path: The path to save the output audio file.
    """

    tts = TTS(model_name=model_name).to(device)
    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker="Luis Moray",
        language="en",
    )

    return output_path


# Example usage:
text = "To sum up. Why Fortran? Its enduring legacy in scientific computing and continued relevance today? Firstly, Fortran is a language that has been around for decades and has a strong presence in the scientific computing community. It is known for its efficiency and performance, making it a popular choice for numerical simulations and high-performance computing tasks. In great part, this is due to the early limitations and the importance of efficient memory usage in the context of limited computer resources at the beginning of programming. There are more than 5 decades of history and improvement of the language. Despite being a simple type, the integer data type is fundamental in programming, serving as the foundation for more complex operations, data structures, and providing key performance optimizations in several cases. The linting tools, such as the 'Modern Fortran' extension, are essential for catching potential errors and improving code quality. They help ensure that the code adheres to best practices and standards, making it easier to maintain and understand. Knowing how to interpret the output of the compiler and the linter is crucial for resolving errors and warnings effectively. Understanding the error messages and warnings helps programmers identify: potential runtime errors at compile time, deprecated or dangerous practices, performance optimization opportunities, and standards compliance issues. We are done!"

# EN-US:
#model_name = "tts_models/en/ljspeech/vits"
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
output_path = "23_resume.wav"
generate_audio(text, model_name, output_path)

# Restaurar stderr
sys.stderr = original_stderr

## Speaker xtts
'''
spks = [
    "Claribel Dervla",
    "Daisy Studious",
    "Gracie Wise",
    "Tammie Ema",
    "Alison Dietlinde",
    "Ana Florence",
    "Annmarie Nele",
    "Asya Anara",
    "Brenda Stern",
    "Gitta Nikolina",
    "Henriette Usha",
    "Sofia Hellen",
    "Tammy Grit",
    "Tanja Adelina",
    "Vjollca Johnnie",
    "Andrew Chipper",
    "Badr Odhiambo",
    "Dionisio Schuyler",
    "Royston Min",
    "Viktor Eka",
    "Abrahan Mack",
    "Adde Michal",
    "Baldur Sanjin",
    "Craig Gutsy",
    "Damien Black",
    "Gilberto Mathias",
    "Ilkin Urbano",
    "Kazuhiko Atallah",
    "Ludvig Milivoj",
    "Suad Qasim",
    "Torcull Diarmuid",
    "Viktor Menelaos",
    "Zacharie Aimilios",
    "Nova Hogarth",
    "Maja Ruoho",
    "Uta Obando",
    "Lidiya Szekeres",
    "Chandra MacFarland",
    "Szofi Granger",
    "Camilla Holmström",
    "Lilya Stainthorpe",
    "Zofija Kendrick",
    "Narelle Moon",
    "Barbora MacLean",
    "Alexandra Hisakawa",
    "Alma María",
    "Rosemary Okafor",
    "Ige Behringer",
    "Filip Traverse",
    "Damjan Chapman",
    "Wulf Carlevaro",
    "Aaron Dreschner",
    "Kumar Dahl",
    "Eugenio Mataracı",
    "Ferran Simen",
    "Xavier Hayasaka",
    "Luis Moray",
    "Marcos Rudaski",
]
'''
# PT-BR:
# model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
# Dividir o texto em sentenças
# sentences = text.split(".")
# sentences = [
#    sentence.strip() for sentence in sentences if sentence.strip()
# ]  # Remover sentenças vazias e espaços em branco

# Gerar áudio para cada sentença
# for i, sentence in enumerate(sentences):
#    output_path = f"03_ProbSolRec_{i}.wav"
#    generate_audio(sentence, model_name, output_path)
#    print(f"Áudio gerado para a sentença {i + 1}: {output_path}")

# print("Processo concluído!")

# Bons modelos:
# tts_models/en/ljspeech/tacotron2-DDC
# tts_models/en/ljspeech/tacotron2-DDC_ph
# tts_models/en/ljspeech/vits - melhor performance com dicção
