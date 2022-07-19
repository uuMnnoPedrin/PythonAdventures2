import os
ASSETS_DIR = os.path.join('asset')

class PrintAsset:
    def art(self, art_name:str):
        with open(f"{ASSETS_DIR}/{art_name}.txt","r") as a:
            for line in a:
                print(line.rstrip())

_inst = PrintAsset()
art = _inst.art
