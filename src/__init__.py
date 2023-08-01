# -*- coding: utf-8 -*-

from .Encoder import Encoder
from .Decoder import Decoder

from Liquirizia.Serializer import SerializerHelper

__all__ = (
	'Encoder',
	'Decoder',
)

SerializerHelper.Set('text/plain', Encoder, Decoder)
SerializerHelper.Set('text', Encoder, Decoder)
SerializerHelper.Set('text/html', Encoder, Decoder)
SerializerHelper.Set('html', Encoder, Decoder)
