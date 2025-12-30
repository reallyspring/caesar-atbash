import string

alphabet = string.ascii_letters

class AtbashDescriptor:
    def __init__(self):
        self.value = ""

    def __set__(self, instance, value):
        result = ""
        for ch in value:
            if ch in alphabet:
                index = alphabet.index(ch)
                result += alphabet[-index - 1]
            else:
                result += ch
        self.value = result

    def __get__(self, instance, owner):
        return self.value

class AtbashCipher:
    text = AtbashDescriptor()

a = AtbashCipher()
a.text = "hello world"
print(a.text)

a.text = "svool dliow"
print(a.text)
