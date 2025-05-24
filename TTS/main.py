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
text = "The simplest program we can test in a language is the famous 'Hello World', popularized by Kernighan e Ritchie in his book 'The C Programming Language'. It is possible to write Fortran codes in basic text editors, such as the notepad and directly in the terminal via Nano editor and Vim. However, this is not the ideal approach to programming in today’s world. We must use a tool for this, that is, a code editor, because it offers several important features, such as the syntax highlighting with distinct colors and visual indication of typing errors and logic. In other words, before we start writing our first programs in Fortran, we will need to set up a proper development environment. An excellent choice for this is the popular 'VS Code', which stands out for its expandability through extensions, similar to installing applications on smartphones. Making it a great choice for development in Fortran. In particular, through the 'Modern Fortran' extension, which formats the code and analyzes the syntax before we compile the program. Before we write our first program in Fortran, let’s set up the development environment. For this, we will create a workbook called 'Test'. I have already presented in another video here on the channel (link in the description) how to configure the VS Code to work with Fortran, but we will review some important points. When you start VS Code for the first time for a new project, it will prompt you to specify a folder for your project. You can select an existing directory or create a new one now. This offers a significant advantage: when we open the integrated terminal within VS Code, it automatically positions itself in the path of your project folder. This way, we avoid the need to manually navigate between directories using Linux commands in the terminal, which makes the work much easier, especially for beginners who do not yet master the basic Linux commands."

# EN-US:
#model_name = "tts_models/en/ljspeech/vits"
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
output_path = "02_VScode.wav"
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
