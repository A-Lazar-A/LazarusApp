import os
import re

def kek():
    id = QFontDatabase.addApplicationFont(":/fonts/TiltPrism-Regular-VariableFont_XROT,YROT.ttf")
    family = QFontDatabase.applicationFontFamilies(id)[0]

    font = QFont(family)
def generate(path: str):
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)
    for it in ui_list:
        file_path = os.path.join(path, it)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} > {path}{os.sep}{file_name_without_extension}.py'
        os.popen(cmd)


if __name__ == '__main__':
    generate(os.path.dirname((os.path.abspath(__file__))))

