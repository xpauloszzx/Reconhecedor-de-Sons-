import wave
import os

# Diretório contendo os arquivos de áudio .wav
diretorio =  r'D:\Users\psgs\Documents\audio'

# Lista para armazenar os arquivos de áudio abertos
audios = []
i = 0
# Itera sobre todos os arquivos no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.wav'):
        # Abre o arquivo de áudio
        caminho_arquivo = os.path.join(diretorio, arquivo)
        audio = wave.open(caminho_arquivo, 'rb')
        audios.append((arquivo, audio))  # Adiciona tupla (nome do arquivo, objeto de áudio)
        i=i+1

# Exemplo de como acessar algumas informações sobre os arquivos de áudio abertos
for nome_arquivo, audio in audios:
    print("Nome do arquivo:", nome_arquivo)
    print("Número de canais:", audio.getnchannels())
    print("Taxa de amostragem:", audio.getframerate())
    print("Número de quadros:", audio.getnframes())
    print("Duração (segundos):", audio.getnframes() / audio.getframerate())
    audio.close()
print(i)
print(audios)