import os

os.system('cmd /k "cd ../ & py -m twine upload --skip-existing --repository testpypi dist/*"')
