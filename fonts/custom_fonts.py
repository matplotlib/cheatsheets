from pathlib import Path

from matplotlib.font_manager import fontManager


HERE = Path(__file__).parent.resolve()
for font in HERE.glob('*/*.[ot]tf'):
    fontManager.addfont(font)
