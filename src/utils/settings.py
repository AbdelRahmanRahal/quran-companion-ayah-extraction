from pathlib import Path

from PySide6.QtGui import QColor

# ---------------------------------------------------------------------------- #
#                                     Paths                                    #
# ---------------------------------------------------------------------------- #
BASE_DIR = Path(__file__).parents[2]
ASSETS_DIR = BASE_DIR / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
DB_PATH = ASSETS_DIR / "glyphs.db"

# ---------------------------------------------------------------------------- #
#                                    Palette                                   #
# ---------------------------------------------------------------------------- #
C_BG_TOP = QColor("#0f0c1a")
C_BG_BOTTOM = QColor("#1a1228")
C_GOLD_LIGHT = QColor("#e8c97a")
C_GOLD_DARK = QColor("#b8922a")
C_CREAM = QColor("#f5ede0")
C_FRAME_OUTER = QColor("#c9a84c")
C_FRAME_INNER = QColor("#7a5c1e")
C_DIVIDER = QColor("#6b4f1e")

# ---------------------------------------------------------------------------- #
#                                   Renderer                                   #
# ---------------------------------------------------------------------------- #
IMG_W = 900
PADDING = 54

