# Liquirizia.Serializer.Implements.Text
텍스트 형식으로 통신하기 위한 직렬화 및 비직렬화 도구

## 사용법
```python
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

	encoded = SerializerHelper.Encode([1,2,3], format='text/plain', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode((4,5,6), format='text/plain', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
	print(encoded, decoded)

	_ = {
		'a': True,
		'b': 0,
		'c': 0.0,
		'd': 'String',
		'e': [1,2,3],
		'f': (1,2,3),
		'g': {
			'a': True,
			'b': 0,
			'c': 0.0,
			'd': 'String',
			'e': [1,2,3],
			'f': (1,2,3),
			'g': {}
		}
	}
	encoded = SerializerHelper.Encode(_, format='text/plain', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
	print(encoded, decoded)
```

## 개선사항
* [ ] DataModelObject 지원