import os #conversao basica de arquivos de video e audio. ex:mp3,mp4,ts,mov
import aspose.words as aw #conversao de imagem e pdfs

def converter_video():
    print('insira o nome do arquivo')
    arquivo = input(" ")
    print('formado\nmov\nmp4\nmp3\nts')
    tipo =  input(" ")
    print = ('qual o novo nome do arquivo?')
    nome = input(' ')
    os.rename(arquivo,f'{nome}.{tipo}' )
    print('arquivo convertido')

while True:
    print('que tipo de arquivo\n[1]video')
    r = int(input(' '))
    if r == 1:
        converter_video()

