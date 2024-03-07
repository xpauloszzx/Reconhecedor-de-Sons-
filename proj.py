import wave
import os
import shutil
import os


# Diretório contendo os arquivos de áudio .wav
diretorio =  r'D:\Users\psgs\Documents\audio'  #alterar isso pq estavamos no cin

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

# -----------

# Diretório contendo os arquivos de áudio .wav originais
diretorio_origem = r'D:\Users\aab2\Documents\audio' #alterar isso pq estavamos no cin

# Diretório onde os arquivos selecionados serão copiados
diretorio_destino = r'D:\Users\aab2\Documents\copiados' #alterar isso pq estavamos no cin

# Criar o diretório de destino se ele não existir
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

# Lista dos arquivos selecionados
arquivos_selecionados = [arquivo for arquivo in os.listdir(diretorio_origem) if arquivo.endswith('.wav') and '-42.wav' in arquivo]

# Copiar os arquivos selecionados para o diretório de destino
for arquivo in arquivos_selecionados:
    caminho_origem = os.path.join(diretorio_origem, arquivo)
    caminho_destino = os.path.join(diretorio_destino, arquivo)
    shutil.copy2(caminho_origem, caminho_destino)

print("Arquivos copiados com sucesso para:", diretorio_destino)
