# -*- coding: utf-8 -*-

from Liquirizia.Serializer import Serializer

__all__ = (
	'Encoder'
)


class Encoder(Serializer):
	"""
	Encoder Class for Text
	"""

	def __call__(self, obj):
		return str(obj)
