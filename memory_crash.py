import ctypes
from ctypes import wintypes

PAGE_NOACCESS = 0x01

my_buffer = ctypes.c_long(500)
buffer_address = ctypes.addressof(my_buffer)

print(f"Буфер успешно создан по адресу: {hex(buffer_address)}")
print(f"Текущее значение в буфере: {my_buffer.value}")

print("\nОбращаемся к подсистеме памяти: принудительно устанавливаем флаг PAGE_NOACCESS для этой страницы...")
old_protect = wintypes.DWORD()

success = ctypes.windll.kernel32.VirtualProtect(
    ctypes.c_void_p(buffer_address),
    ctypes.sizeof(my_buffer),
    PAGE_NOACCESS,
    ctypes.byref(old_protect)
)

if success:
    print("Флаг защиты успешно изменен на PAGE_NOACCESS!")
    print("Сейчас программа попытается прочитать данные по заблокированному адресу...")

    invalid_read = my_buffer.value
    print(f"Этот текст никогда не напечатается: {invalid_read}")
else:
    print("Не удалось изменить флаги защиты.")