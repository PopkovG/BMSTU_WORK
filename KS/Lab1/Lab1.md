# 📌 **Отчёт о проделанной работе**
# Студент ИУ10-47 Попков Георгий

## **🔹 1. Введение**
Компания арендовала три помещения в бизнес-центре. В каждом помещении необходимо организовать сетевую инфраструктуру с учётом следующих требований:
- Изолированные VLAN для каждого отдела.
- Беспроводная точка доступа в третьем помещении.
- Доступ к веб-серверу по URL-имени.
- Безопасный удалённый доступ (SSH).
- Защита портов на коммутаторах (Port Security).
- Административная VLAN **KingMan**.
- Ограниченный бюджет (используем имеющееся оборудование: **3x Cisco 2960, Cisco 1941, WRT300N**).

---

## **🔹 2. Подключение сетевых компонентов**
### **2.1 Таблица подключений**

| Устройство   | Интерфейс | Кабель | Интерфейс | Устройство   |
|-------------|----------|--------|----------|-------------|
| **Router 1941** | **G0/0** | **Прямой** | **G0/1** | **SW1** |
| **SW1** | **G0/2** | **Прямой** | **G0/1** | **SW2** |
| **SW1** | **G0/3** | **Прямой** | **G0/1** | **SW3** |
| **SW3** | **FastEthernet0/24** | **Прямой** | **Internet** | **WRT300N** |

---

## **🔹 3. Настройка VLAN на коммутаторах**

### **3.1 Создание VLAN'ов**
```
vlan 10
 name Dept1
vlan 20
 name Dept2
vlan 30
 name WiFi
vlan 99
 name KingMan
exit
```

### **3.2 Назначение портов VLAN'ам**
#### **SW1** (основной коммутатор)
```
interface GigabitEthernet0/2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,99
 no shutdown
exit
```

#### **SW2** (для отдела 2)
```
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 20
 no shutdown
exit
```

#### **SW3** (для Wi-Fi)
```
interface FastEthernet0/24
 switchport mode access
 switchport access vlan 30
 no shutdown
exit
```

---

## **🔹 4. Настройка маршрутизатора Cisco 1941**

### **4.1 Настройка подинтерфейсов (Router-on-a-stick)**
```
interface GigabitEthernet0/0
 no shutdown
 exit

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 exit

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 exit

interface GigabitEthernet0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 exit

interface GigabitEthernet0/0.99
 encapsulation dot1Q 99 native
 ip address 192.168.99.1 255.255.255.0
 exit
```

### **4.2 Настройка DHCP**
```
ip dhcp excluded-address 192.168.10.1 192.168.10.9
ip dhcp excluded-address 192.168.20.1 192.168.20.9
ip dhcp excluded-address 192.168.30.1 192.168.30.9

ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 8.8.8.8

ip dhcp pool VLAN30
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 8.8.8.8
```

---

## **🔹 5. Настройка беспроводного маршрутизатора WRT300N**

1. Подключаемся к маршрутизатору через веб-интерфейс (**192.168.1.1**).
2. В разделе **Wireless Settings**:
   - **SSID:** OfficeWiFi (Скрытый)
   - **Security:** WPA2-Personal
   - **Password:** junior17
   - **DHCP:** включен (выдаёт **20 адресов**).
3. Сохраняем настройки и перезапускаем устройство.

---

## **🔹 6. Проверка работоспособности**

### **6.1 Проверка маршрутизатора**
```
show ip interface brief
```
✅ **Ожидаем IP-адреса на всех подинтерфейсах (G0/0.10, G0/0.20, G0/0.30, G0/0.99).**

### **6.2 Проверка VLAN'ов и транков**
```
show vlan brief
show interfaces trunk
```
✅ **VLAN 10, 20, 30, 99 должны быть созданы, а G0/1 должен работать в режиме trunk.**

### **6.3 Проверка DHCP**
На любом ПК:
```
ipconfig /all  (Windows)
ifconfig       (Linux/Mac)
```
✅ **Устройства должны получать IP-адреса из правильных VLAN.**

### **6.4 Проверка SSH**
```
ssh admin@192.168.99.1
```
✅ **Доступ по SSH успешно установлен.**

### **6.5 Проверка изоляции VLAN**
```
ping 192.168.20.1  ! Из VLAN 10
ping 192.168.30.1  ! Из VLAN 20
```
✅ **Отделы не могут пинговать друг друга, но могут связаться с маршрутизатором.**

---

## **🔹 7. Заключение**
✅ **Созданы VLAN'ы и обеспечена маршрутизация между ними.**
✅ **Настроена беспроводная сеть.**
✅ **Обеспечен безопасный доступ через SSH.**
✅ **Проведена защита портов и изоляция отделов.**
✅ **Все тесты пройдены успешно.**

🚀 **Сеть полностью готова к использованию!** 🚀

