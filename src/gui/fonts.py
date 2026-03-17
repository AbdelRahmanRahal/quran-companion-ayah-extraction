from pathlib import Path

from PySide6.QtGui import QFontDatabase

from ..utils.settings import FONTS_DIR

_loaded_fonts: dict[str, str] = {}


def load_font(path: Path | str) -> str | None:
	"""
	Loads a font file from the given path into the application's font database.

	Checks if the font is already loaded to prevent duplicates. If not, it attempts
	to load it using QFontDatabase.

	Args:
		path (Path | str): The file path to the font (e.g., .ttf or .otf).

	Returns:
		str | None: The font family name if successfully loaded, otherwise None.
	"""
	path_str = str(path)
	if path_str in _loaded_fonts:
		return _loaded_fonts[path_str]

	if not Path(path).exists():
		return None

	fid = QFontDatabase.addApplicationFont(path_str)
	if fid < 0:
		return None

	families = QFontDatabase.applicationFontFamilies(fid)
	if not families:
		return None

	_loaded_fonts[path_str] = families[0]
	return families[0]


def page_font_family(page: int) -> str | None:
	"""
	Retrieves the font family name for a specific Quran page.

	Constructs the font filename based on the page number (e.g., 'p1.ttf')
	and attempts to load it.

	Args:
		page (int): The page number.

	Returns:
		str | None: The font family name for the page, or None if loading fails.
	"""
	return load_font(FONTS_DIR / f"p{page}.ttf")


def bsml_font_family() -> str | None:
	"""
	Retrieves the font family name for the Basmala and Surah headers.

	Attempts to load 'bsml.ttf' from the fonts directory.

	Returns:
		str | None: The font family name, or None if loading fails.
	"""
	return load_font(FONTS_DIR / "bsml.ttf")
