import heapq
from collections import Counter
import struct

class Node:
    """Узел дерева Хаффмана"""
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):

        return self.freq < other.freq

def encode(msg: str) -> tuple[str, dict[str, str]]:
    """Кодирует строку методом Хаффмана"""
    if not msg:
        return "", {}

    # Считаем, сколько раз встречается каждая буква
    freq = Counter(msg)

    # Создаём кучу из узлов
    heap = [Node(freq[char], char) for char in freq]
    heapq.heapify(heap)

    # Строим дерево Хаффмана
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Генерируем коды из дерева
    huffman_codes = {}

    def make_codes(node, code=""):
        if node.char is not None:
            huffman_codes[node.char] = code or "0"
        else:
            make_codes(node.left, code + "0")
            make_codes(node.right, code + "1")

    if heap:
        make_codes(heap[0])

    # Кодируем сообщение
    encoded = ''.join(huffman_codes[char] for char in msg)

    return encoded, huffman_codes

def decode(encoded: str, table: dict[str, str]) -> str:
    """Декодирует строку по таблице Хаффмана"""
    if not encoded:
        return ""

    reverse_table = {code: char for char, code in table.items()}

    result = []
    current_code = ""

    for bit in encoded:
        current_code += bit
        if current_code in reverse_table:
            result.append(reverse_table[current_code])
            current_code = ""

    return ''.join(result)

def bits_to_bytes(bits: str) -> bytes:
    """Превращает строку бит '0101' в байты b'\\x05'"""
    if not bits:
        return b''

    bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = int(bits[i:i+8], 2)
        byte_array.append(byte)

    return bytes(byte_array)

def bytes_to_bits(byte_data: bytes, num_bits: int) -> str:
    """Превращает байты обратно в строку бит"""
    bits = ''.join(f'{byte:08b}' for byte in byte_data)
    return bits[:num_bits]

def encode_file(input_path: str, output_path: str):
    """Сжимает файл"""
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Кодируем текст
    encoded_bits, table = encode(text)

    # Готовим данные для записи
    table_bytes = bytearray()

    # Превращаем таблицу в байты
    for char, code in table.items():
        char_bytes = char.encode('utf-8')
        # [длина символа][символ][длина кода][код]
        table_bytes.append(len(char_bytes))
        table_bytes.extend(char_bytes)
        table_bytes.append(len(code))
        table_bytes.extend(bits_to_bytes(code))

    with open(output_path, 'wb') as f:
        f.write(struct.pack('II', len(table), len(encoded_bits)))
        f.write(table_bytes)
        f.write(bits_to_bytes(encoded_bits))

def decode_file(input_path: str, output_path: str):
    """Восстанавливает файл"""
    with open(input_path, 'rb') as f:
        table_size, num_bits = struct.unpack('II', f.read(8))

        table = {}
        for _ in range(table_size):
            char_len = f.read(1)[0]
            char = f.read(char_len).decode('utf-8')
            code_len = f.read(1)[0]

            bytes_needed = (code_len + 7) // 8
            code_bytes = f.read(bytes_needed)
            code = bytes_to_bits(code_bytes, code_len)

            table[char] = code

        bytes_needed = (num_bits + 7) // 8
        encoded_bytes = f.read(bytes_needed)
        encoded_bits = bytes_to_bits(encoded_bytes, num_bits)


    decoded_text = decode(encoded_bits, table)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decoded_text)

if __name__ == "__main__":
    text = "hello world"
    print(f"Исходный текст: {text}")

    encoded, table = encode(text)
    print(f"Закодирован: {encoded}")
    print(f"Таблица кодов: {table}")

    decoded = decode(encoded, table)
    print(f"Декодирован: {decoded}")
    print(f"Совпадает: {text == decoded}")
    print()

    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("Hello world!")

    encode_file('test.txt', 'compressed.bin')
    print("Файл сжат: test.txt → compressed.bin")

    decode_file('compressed.bin', 'restored.txt')
    print("Файл восстановлен: compressed.bin → restored.txt")

    with open('test.txt', 'r', encoding='utf-8') as f1, \
         open('restored.txt', 'r', encoding='utf-8') as f2:
        print(f"Файлы одинаковы: {f1.read() == f2.read()}")
