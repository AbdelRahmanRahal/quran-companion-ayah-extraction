from typing import override

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QResizeEvent
from PySide6.QtWidgets import QLabel, QSizePolicy


class PreviewWidget(QLabel):
	"""
	A custom QLabel widget that displays an image with responsive scaling.

	This widget maintains a high-resolution source image and dynamically scales
	it to fit the current widget dimensions while preserving the aspect ratio
	and using smooth transformation.
	"""

	def __init__(self) -> None:
		"""Initializes the preview widget with alignment and size policies."""
		super().__init__()
		self.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
		self.setMinimumSize(600, 300)

		# The source of truth for the displayed image
		self._pixmap: QPixmap | None = None

	def set_image(self, img: QImage) -> None:
		"""
		Sets the source image for the preview.

		Args:
			img (QImage): The high-resolution image to display.
		"""
		self._pixmap = QPixmap.fromImage(img)
		self._update_display()

	@override
	def resizeEvent(self, event: QResizeEvent) -> None:
		"""
		Handles widget resize events to update the displayed image scaling.

		Args:
			event (QResizeEvent): The resize event triggered by Qt.
		"""
		super().resizeEvent(event)
		self._update_display()

	def _update_display(self) -> None:
		"""
		Scales the source image to fit the current widget size and updates the display.

		Uses SmoothTransformation for high-quality scaling and KeepAspectRatio
		to prevent distortion.
		"""
		if self._pixmap and not self._pixmap.isNull():
			scaled = self._pixmap.scaled(
				self.size(),
				Qt.AspectRatioMode.KeepAspectRatio,
				Qt.TransformationMode.SmoothTransformation,
			)
			self.setPixmap(scaled)
