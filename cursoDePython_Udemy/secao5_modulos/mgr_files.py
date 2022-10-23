import os
import shutil


def search():
    search_path = input(r'Qual o caminho da busca? ')
    search_path = search_path.replace('"', '').replace("'", '').strip()

    search_term = input('Qual o termo da busca? ')

    def format_size(size):
        base = 1024
        kilo = base
        mega = base ** 2
        giga = base ** 3
        tera = base ** 4
        peta = base ** 5

        if size < kilo:
            sigla = 'B'
        elif size < mega:
            size /= kilo
            sigla = 'K'
        elif size < giga:
            size /= mega
            sigla = 'M'
        elif size < tera:
            size /= giga
            sigla = 'G'
        elif size < peta:
            size /= tera
            sigla = 'T'
        else:
            size /= peta
            sigla = 'P'

        return f'{round(size)}{sigla}'

    for root, dirs, files in os.walk(search_path):
        for file in files:
            if search_term in file:
                try:
                    file_abspath = os.path.join(root, file)
                    file_name, file_ext = os.path.splitext(file)
                    file_size = os.path.getsize(file_abspath)
                    file_size_f = format_size(file_size)
                    print()
                    print('Encontrei o arquivo:', file, file_size_f)
                    print('Caminho do arquivo:', file_abspath)
                    print('Nome do arquivo:', file_name)
                    print('Extensão do arquivo:', file_ext)
                    print('Tamanho em bytes:', file_size)
                    print('Tamanho formatado:', file_size_f)

                except PermissionError:
                    print('Você não tem permissão neste arquivo/dirétorio.')
                except FileNotFoundError:
                    print('Arquivo não encontrado.')
                except Exception as e:
                    print('Erro desconhecido:', e)


def copy_file():
    original_path = input(r'Qual o caminho da pasta/arquivo? ')
    new_path = input(r'Qual o caminho será copiado a pasta/arquivo? ')

    try:
        os.mkdir(original_path)
    except FileExistsError:
        pass

    for root, dirs, files in os.walk(original_path):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(new_path, file)
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso!')


def move_file():
    original_path = input(r'Qual o caminho da pasta/arquivo? ')
    new_path = input(r'Para qual caminho será movida a pasta/arquivo? ')

    try:
        os.mkdir(original_path)
    except FileExistsError:
        pass

    for root, dirs, files in os.walk(original_path):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(new_path, file)
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso!')


def remove_file():
    original_path = input(r'Qual o caminho para exclusão da pasta/arquivo? ')

    for root, dirs, files in os.walk(original_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f'Arquivo {file} excluído com sucesso!')


print('Digite 1 para para procurar um arquivo\n'
      'Digite 2 para mover um arquivo\n'
      'Digite 3 para copiar um arquivo\n'
      'Digite 4 para excluir um arquivo')

print(r'Exemplo de caminho "C:\Users\Matheus\Downloads\Documents"')

try:
    option = int(input('Qual a opção escolhida? '))
except ValueError:
    print('Só aceita números de 1 a 4')

if option == 1:
    search()
elif option == 2:
    move_file()
elif option == 3:
    copy_file()
elif option == 4:
    remove_file()
else:
    print('Digite uma opção válida!!')
