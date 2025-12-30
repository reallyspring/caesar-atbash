import string

alphabet = string.ascii_letters + string.digits

class CaesarDescriptor:
    def __init__(self, shift):
        self.shift = shift
        self.value = ""

    def __set__(self, instance, value):
        result = ""
        for ch in value:
            if ch in alphabet:
                index = alphabet.index(ch)
                new_index = (index + self.shift) % len(alphabet)
                result += alphabet[new_index]
            else:
                result += ch
        self.value = result

    def __get__(self, instance, owner):
        return self.value

class CaesarCipher:
    text = CaesarDescriptor(3)

c = CaesarCipher()
c.text = "hello world"
print(c.text)

class CaesarDecrypt:
    text = CaesarDescriptor(-3)

d = CaesarDecrypt()
d.text = "khoor zruog"
print(d.text)
