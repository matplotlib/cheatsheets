from pathlib import Path

from matplotlib.font_manager import fontManager


def setup():
    root_dir = Path(__file__).parent.parent.resolve()
    for font in root_dir.glob('fonts/*/*.[ot]tf'):
        fontManager.addfont(font)
