# -*- coding: utf-8 -*-

from Liquirizia.Serializer import SerializerHelper
import Liquirizia.Serializer.Implements.Text


if __name__ == '__main__':

  encoded = SerializerHelper.Encode(True, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0.0, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode('String', format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode([], format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode((), format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode({}, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  # TODO : Support DataModelObject
