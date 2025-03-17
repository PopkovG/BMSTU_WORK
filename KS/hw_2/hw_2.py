info = {
    "00:50:56:00:00:fd": "VMware, lnc",
    
}


def mac_address(key):
    return info.get(key, "Компания с таким MAC-адресом не найдена")

while True:
    mac = input("Введите MAC-адрес (или 'exit' для выхода): ").lower()

    if mac == 'exit':
        print("Выход из программы.")
        break

    value = mac_address(mac)
    print(f"Компания: {value}")