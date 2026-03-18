import os
import sqlite3


class GlyphsDB:
	"""
	A handler for interacting with the Quranic glyphs SQLite database.

	This class provides methods to retrieve specific Ayah text (glyphs),
	Surah name glyphs, and page mapping information based on the QCF V1 standard.

	DB Schema:
		ayah_glyphs		(id, surah, ayah, qcf_v1, qcf_v2)
		surah_glyphs	(id, surah, qcf_v1, qcf_v2)
		coordinates_v1	(page, surah, ayah, start_pos, end_pos)
		pages			(page_no, qcf_v1, qcf_v2)
		juz_glyphs		(page, juz, qcf_v1, qcf_v2, text)

	Attributes:
		_conn (sqlite3.Connection): The connection object to the SQLite database.
	"""

	def __init__(self, path: str) -> None:
		if not os.path.exists(path):
			raise FileNotFoundError(f"glyphs.db not found at: {path}")

		self._conn = sqlite3.connect(path)
		self._conn.row_factory = sqlite3.Row

		self.MAX_SURAH = 114

	def ayah_data(self, surah: int, ayah: int) -> tuple[str, str | None, int]:
		"""
		Retrieves the Surah name glyph, Ayah text glyphs, and the page number for a specific Ayah.

		Args:
			surah (int): The Surah number (1-114).
			ayah (int): The Ayah number.

		Returns:
			tuple[str, str | None, int]: A tuple containing (surah_glyph, ayah_glyphs, page_number).
		"""
		cur = self._conn.cursor()

		# Surah name glyph
		cur.execute("SELECT qcf_v1 FROM surah_glyphs WHERE surah=?", (surah,))
		row = cur.fetchone()
		surah_glyph = row["qcf_v1"] if row else "?"

		# Ayah glyphs
		cur.execute(
			"SELECT qcf_v1 FROM ayah_glyphs WHERE surah=? AND ayah=?",
			(surah, ayah),
		)
		row = cur.fetchone()
		ayah_glyphs = row["qcf_v1"] if row else None

		# Page number
		cur.execute(
			"SELECT page FROM coordinates_v1 WHERE surah=? AND ayah=?",
			(surah, ayah),
		)
		row = cur.fetchone()
		page = row["page"] if row else 1

		return surah_glyph, ayah_glyphs, page

	def max_ayah(self, surah: int) -> int:
		"""
		Returns the maximum Ayah number available for a given Surah.

		Args:
			surah (int): The Surah number.

		Returns:
			int: The count of Ayahs in the specified Surah.
		"""
		cur = self._conn.cursor()
		cur.execute("SELECT MAX(ayah) AS m FROM ayah_glyphs WHERE surah=?", (surah,))
		row = cur.fetchone()
		return row["m"] if row and row["m"] else 1

	def close(self) -> None:
		"""Closes the database connection."""
		if self._conn:
			self._conn.close()
