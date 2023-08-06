from random import seed, shuffle, randbytes
from operator import xor

class BitArray:
	def __init__(self, _bytes: bytes) -> None:
		self.data = self.to_bits(_bytes)
	def to_bits(self, _bytes: bytes) -> list[int]:
		result = []
		for b in _bytes:
		    result.extend(map(int, f'{b:08b}'))
		return result
	def to_bytes(self) -> bytes:
		return bytes(int(''.join(str(bit) for bit in bits), 2) for bits in [self.data[i:i + 8] for i in range(0, len(self.data), 8)])
	def __str__(self) -> str:
		return str([self.data[i:i + 8] for i in range(0, len(self.data), 8)]).replace(', ', '').replace('[', ' ').replace(']', '')[2:]

	def _genSeed(self, password: str) -> int:
		return sum([ord(x)**2 for x in password])

	def bitEncode(self, password):
		mask = list(range(len(self.data)))
		seed(password)
		shuffle(mask)
		result = [0] * len(self.data)
		for d in range(len(self.data)):
			result[mask[d]] = self.data[d]
		self.data = result
		return self

	def bitDecode(self, password):
		mask = list(range(len(self.data)))
		seed(password)
		shuffle(mask)
		result = []
		for d in mask:
			result.append(self.data[d])
		self.data = result
		return self
	
	def xorEncode(self, key=b''):
		byts = self.to_bytes()
		mask = randbytes(len(byts))
		enc = bytes([xor(s, mask[i]) for (i, s) in enumerate(byts)])
		self.data = self.to_bits(enc)
		return mask
	def xorDecode(self, key):
		data = bytes([xor(s, key[i]) for (i, s) in enumerate(self.to_bytes())])
		self.data = self.to_bits(data)
		return self
