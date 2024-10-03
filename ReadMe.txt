Participantes:
Gomez Baldoni Santino Nauel 
Nina Condori Cristian
Moreno Matias Ezequiel
David Polchovski

Problemática:

Nuestra problemática a solucionar es la poca libertad y pocas posibilidades de modificación de parámetros que tienen los firmware de fábrica de los routers.


Marco Teórico:
Este Documento va dirigido al público general que quiera estar informado sobre los procesos mostrados en el mismo documento como el flasheo de un router o la creación de un servidor con el protocolo TFTP, a continuación se responderán las preguntas más recurrentes con respecto al proyecto.

¿ Qué es OpenWrt y los programas basados en este ?
OpenWrt es un firmware de código abierto que ofrece una alternativa flexible y personalizable a los firmwares predeterminados de los fabricantes, con mejores capacidades de seguridad y rendimiento.
Sencillamente estos programas sirven para modificar el firmware de un router, dando como resultado la posibilidad de aumentar la libertad.

¿ Que es DD-Wrt ?
DD-Wrt es un firmware que se considera uno de los primeros firmware en estar basados en OpenWrt al ser lanzado en 22 de enero de 2005 y estar basado en firmware Alchemy pero luego extrañamente cambio de base a OpenWrt en 2006, este mismo ofrece Personalización Avanzada,  Regulación de la señal WiFi, Conexión a VPN, Permite la actualización dinámica de DNS, lo que facilita el acceso remoto a la red sin necesidad de recordar direcciones IP cambiantes una interfaz Web Mejorada, etc.

¿ Qué es el protocolo TFTP ?
TFTP es un protocolo para transferir archivos, está diseñado para ser pequeño y fácil de implementar; por lo tanto, carece de la mayoría de las funciones de un FTP regular.

¿ Qué es un router ?
Un router es un dispositivo de hardware que sirve de punto de conexión entre una red local e Internet. Los routers gestionan o «enrutan», el tráfico web y los datos entre dispositivos de diferentes redes, y permiten que varios dispositivos compartan la misma conexión a Internet.

¿ Qué son los protocolos ?
Los protocolos son un conjunto de reglas, para enrutar y direccionar paquetes de datos para que puedan viajar a través de las redes y llegar al destino correcto.

¿ Qué es el protocolo FTP ?
Es un protocolo de red para la transferencia de archivos entre sistemas conectados a una red TCP. 

¿ Qué es una red TCP ?
Es una red de equipos que consiste en dos anfitriones (hosts) se conectan e intercambian flujos de datos. TCP garantiza la entrega de datos y paquetes en el mismo orden en que se enviaron.

¿ Qué es un archivo .bin para routers ?
Un archivo .bin, también conocido como archivo binario, es un tipo de archivo que contiene el firmware o software del router. Este archivo se utiliza para actualizar o modificar el firmware del router y habilitar funciones adicionales.
Los archivos .bin son específicos para cada modelo de router y marca. No se puede utilizar un archivo .bin de un router en otro modelo diferente.

¿ Qué es un host ?
Es cualquier computadora o máquina conectada a una red mediante un número de IP definido y un dominio, que ofrece recursos, información y servicios a sus usuarios.

¿ Que es un firmware de router ?
 El firmware es una de las partes más importantes de nuestro router, es el encargado de gestionar todas las conexiones de red de manera óptima y también de evitar o mitigar ataques que nos puedan hacer desde Internet.

¿ Qué quiere decir “flashear un router” ?
Es la acción de escribir en una memoria flash, mediante un cable y programa especial. Con ello podemos instalar un nuevo firmware al router

¿ En qué consiste el proyecto ?
Este proyecto consiste en modificar routers para que tengan muchísima más libertad de modificación de parámetros y además que por default todos los routers que tocan el programa que creamos tengan una misma configuración ideal.

¿ Qué quiere decir licencia GPL en routers ?
La licencia GPL en routers permite a los usuarios acceder y modificar el software de sus routers, promoviendo así un entorno de desarrollo abierto y colaborativo.







Las primer solución que habíamos encontrado la dividimos en tres partes:

La primera parte es flashear un router y probar distintos firmware de flasheo (lo dividimos en más partes) para eso 

La segunda parte: debemos configurar un servidor TFTP (Trivial File Transfer Protocol) en una máquina local.

La tercera parte es aprender a hacer archivos con la extensión .Bin que puedan modificar el firmware del router para poder hacer que los routers que pasan por este firmware puedan ser modificados con parámetros ideales. 

Problemática real:

El problema con los routers de la técnica 11 es que no aprovechan al máximo su potencia y el firmware que tienen por defecto no tiene todas las funcionalidades en lo posible, por eso es que ideamos este proyecto el cual aprovechará la potencia de los routers al máximo.

Por ahora no tenemos claro por qué router empezar ya que como contamos antes intentamos probar con el Mitrastar dsl-2401hn2-e1c, un TP-link y un Linksys pero en todos nos encontramos con distintas dificultades. Lo ideal es que este proyecto funcione en routers viejos.

Lamentable se pierde seguridad cuando se concentran los recursos del router en llevar su potencia al máximo.

No sabemos qué características nuevas agregarían las actualizaciones con respecto a las ya existentes. tampoco sabemos el alcance de estas futuras actualizaciones.

Lo más probable es que actualicemos cada router manualmente, por lo menos al principio, ya que hacer un proceso automatizado para cada router es muy complejo y las variables son casi ilimitadas.

Todavía no sabemos qué pruebas vamos a realizar para saber que un router mejoró antes y después de la actualización

No hay plan de contingencia aun en caso de que la actualización falle, lo peor es que en ciertos routers el firmware puede brikear (dejar inutil al router).

Los únicos recursos que necesitamos son routers, computadoras y tiempo, todos recursos que la técnica 11 ya ofrece, a medida que avanzamos mostraremos capturas de las actualizaciones, software, etc, que vayamos investigando
No esperamos que el impacto de estas actualizaciones sea algo grande, solamente que aproveche el potencial completo de los routers.










Fundamentación:

Los procedimientos varían muchísimo pero lo más común es que para quemar el firmware de OpenWrt en el router necesitarás configurar un servidor TFTP en una máquina local.
Hay varias opciones diferentes de servidores TFTP para descargar y ejecutar, todo lo que necesitas hacer es encontrar el que mejor se adapte a tus necesidades. El servidor TFTP, después de instalado, debe configurarse para funcionar en la IP 192.168.0.66 (puerto 69). Inserta el archivo de firmware dentro de la carpeta del servidor TFTP y sigue las instrucciones a continuación:
Pasos a seguir:

Ejecuta el servidor TFTP y agrega el archivo de firmware en la carpeta. Renombra el archivo de firmware a tp_recovery.bin (de lo contrario, el router no lo encontrará).
Conecta el router (mientras esté apagado) por uno de los puertos LAN a la máquina que ejecuta el servidor TFTP.
Mantén presionado el botón de reinicio mientras enciendes el router. El router buscará el servidor TFTP y descarga cualquier archivo tp_recovery.bin que encuentre. Mientras se transfiere el archivo, los LED del router comenzarán a parpadear.
Si la descarga se realiza correctamente, el router quemará automáticamente el nuevo firmware y se reiniciará.

Para poder hacer un programa .bin debemos modificar la configuración .bin del firmware del router que queremos modificar, básicamente no se puede crear el .bin desde cero, más bien hay que modificar un .bin existente.

Configurar servidor TFTP en Windows video para configurar servidor TFTP en windows
Instalar nuevo firmware al router TP-LINK TL-WR840N ver-6.20

Crear un archivo .bin para manipular routers
Para crear un archivo .bin para manipular un router, necesitas seguir estos pasos:
Obtén el código fuente modificado del firmware del router. 
Esto generalmente implica descargar un firmware alternativo o personalizado creado por desarrolladores de la comunidad.
Compila el código fuente modificado en un archivo .bin. Esto requiere herramientas de desarrollo y conocimientos técnicos. Generalmente se hace usando un entorno Linux.
Verifica que el archivo .bin sea compatible con tu modelo de router. Asegúrate de que el archivo tenga el nombre y formato correcto.
Carga el archivo .bin en el router usando la interfaz web de administración. Esto se hace en la sección de actualización de firmware.
Reinicia el router para que los cambios surtan efecto.
Algunos puntos importantes:
Manipular el firmware de un router puede dejar inservible al dispositivo si no se hace correctamente. Procede con precaución.
Después de cargar un archivo .bin, si restauras el router a valores de fábrica, deberás volver a cargar el archivo .bin. Por eso es importante tener una copia de seguridad.
La actualización oficial del firmware es la solución más estable. Usar archivos .bin modificados es para usuarios avanzados que conocen los riesgos.

Hoy en día aunque el tema sea bastante nicho, hay herramientas como Openwrt que permiten modificar firmwares existentes para crear tu propio firmware con tus propios arreglos.
https://openwrt.org/docs/guide-developer/toolchain/start
ya viene con un manual dividido en partes para poder aprender a modificar firmware.
No solo tiene herramientas para modificar y crear firmware, tiene también herramientas para hacer tus propios paquetes de compilar desde la fuente un firmware completo para todas las arquitecturas que desee admitir





Avances 11 de julio: 

Intentamos aplicarle firmwares tipo Openwrt a un router de TP-link pero este router era tan bajo de especificaciones que tuvimos que buscar otra alternativa y reemplazarlo con un Linksys wrt54g el cual funcionaba con el firmware DD-wrt pero no iba con nuestro objetivo de reciclar routers y tuvimos que cambiar a el router Mitrastar dsl-2401hn2-e1c el cual tenía un problema de actualización de firmware muy específico y no pudimos terminar de solucionarlo.


Avances del día 15 de agosto:
Intentamos flashear un router TP Link modelo TL-WR340GD a través de un servidor TFTP.
Para ello descargamos e instalamos un software llamado TFTPD64
Una vez descargado debemos buscar un firmware compatible con el router, en nuestro caso descargamos https://www.tp-link.com/ar/support/download/tl-wr340gd/v3/#Firmware ya que este router era de versión 3.
conectamos el router a una computadora con un cable RJ45 (el router no debe estar conectado a una corriente electrica)
Una vez descargado todo ejecutamos el software y le agregamos el firmware compatible a la carpeta TFTPD64. Luego entramos a configuraciones y  en la parte de conexiones de red entramos a las propiedades del ethernet. Seleccionamos la opción “habilitar el protocolo de internet versión 4 (TCP/IPV4)”, entramos a sus propiedades y lo configuramos de la siguiente manera.

Hecho esto debemos mantener el botón de reinicio del router mientras lo enchufamos al tomacorrientes (el FTFPD64 debe estar en ejecución) y debería empezar la transferencia y el router tendría su nuevo firmware.

Avances del día 16 de agosto:

Hoy, por primera vez logramos reemplazar el firmware del router de fábrica por el de DD-WRT el cual implementa Aumento de la potencia de transmisión, Soporte para IPv6, WDS, Permite crear redes inalámbricas de malla extendiendo la cobertura de la red
Permite controlar y priorizar el ancho de banda para diferentes aplicaciones y dispositivos, Incluye integración de VPN y opciones de acceso remoto seguro, entre muchísimas otras características.
Seguimos las instrucciones sacadas directamente del manual de DD-WRT, traducidas por Perplexity:

NOTA: Durante la configuración o el flasheo de un router, lo único que debe estar conectado al router es la computadora a través del cable Ethernet y la alimentación.
A PESAR DE OTRAS INSTRUCCIONES EN OTRAS PARTES, REALMENTE NECESITAS CREAR UNA IMAGEN VX PERSONALIZADA para tu router. Si no lo haces, obtendrás una dirección MAC genérica en tu router y una dirección MAC genérica significará que la mayoría de los ISP no te permitirán conectarte a Internet. Aquí te explicamos cómo hacerlo correctamente:
Ve a este hilo y descarga los archivos comprimidos en GV5Flash.zip: http://www.dd-wrt.com/phpBB2/viewtopic.php?t=58231 (Si recibes una advertencia de malware de tu antivirus, ignórala. El archivo está limpio y no contiene malware).
Lee el anuncio del pavo real que se encuentra aquí: http://www.dd-wrt.com/phpBB2/viewtopic.php?t=51486.
Realiza un reinicio HARD en el router de acuerdo con la nota 1 del anuncio del pavo real (30/30/30).
Establece una IP estática en tu computadora a 192.168.1.7. La máscara de subred debe ser 255.255.255.0.
Conecta el cable LAN desde tu computadora a un puerto LAN de tu router. Asegúrate de que tu router esté enchufado. No debe haber nada conectado a tu computadora o al router, excepto el cable LAN entre ellos. Apaga tu firewall y cualquier conexión inalámbrica de la computadora.
Descomprime el archivo que descargaste en el paso uno y colócalo en una ubicación que puedas encontrar fácilmente en tu computadora.
Descomprime el archivo VXImgToolGui.zip en la misma carpeta donde colocaste los otros archivos que descargaste.
Inicia VXImgToolGui.exe.
Asegúrate de que el botón superior esté a la izquierda para WRT54G, no a la derecha para WRT54GS.
Coloca la dirección MAC de la parte inferior de tu router en el cuadro que dice "Desired MAC" (Consejo: También puedes copiar/pegar la dirección MAC desde la página de estado del firmware de Linksys \ Red local).
Haz clic en los tres puntos junto a "output image" y guarda el archivo como My54gImage.bin en la misma carpeta donde se encuentran los demás archivos.
Realiza un ciclo de energía en el router (desenchufa la alimentación del router durante 30 segundos y luego vuelve a enchufarlo).
Abre tu navegador en 192.168.1.1 ingresando esa dirección en la ventana de dirección de tu navegador. Deberías abrir la interfaz web de Linksys y NO una página que diga Modo de Gestión. Si ves el modo de gestión, vuelve a hacer un ciclo de energía en el router.
Ingresa "root" como nombre de usuario y "admin" como contraseña.
Ve a Administración y Actualización de Firmware.
Navega hasta la carpeta que estás usando y selecciona vxworks_prep_03.bin.
Haz clic en actualizar.
Espera CINCO MINUTOS COMPLETOS. Sal a dar un paseo. NO TOQUES ese router durante CINCO MINUTOS.
Cuando hayan pasado cinco minutos completos, realiza un ciclo de energía en el router.
Navega nuevamente a 192.168.1.1. Si obtienes una ventana en blanco, borra la caché de tu navegador. AHORA deberías estar en la ventana del MODO DE GESTIÓN.
Selecciona el archivo My54gImage.bin que creaste. Haz clic en Aplicar.
Espera el mensaje de "Actualización Exitosa" y luego ESPERA CINCO MINUTOS COMPLETOS nuevamente. NO TOQUES tu router.
Inicia tftp.exe.
Ingresa 192.168.1.1 como la dirección en el cuadro superior de tftp.exe.
Deja la contraseña en blanco.
Selecciona el firmware 12548 Newd_Micro.bin.
Establece los reintentos en 99.

Realiza un ciclo de energía en el router.
Cuenta hasta 2.
Haz clic en actualizar.
Cuando obtengas un éxito, espera CINCO MINUTOS COMPLETOS.
Si no obtienes éxito, repite desde el paso 20(4) hasta este. Si aún no obtienes éxito, borra la caché de tu navegador. Intenta usar un navegador diferente también, para navegar a 192.168.1.1.
Cuando puedas acceder a la interfaz web de dd-wrt usando un navegador en 192.168.1.1, realiza un ciclo de energía en el router.
Cuando nuevamente puedas acceder a la interfaz web de dd-wrt usando un navegador en 192.168.1.1, realiza otro reinicio HARD en el router.
Restablece la conexión Ethernet de tu computadora a IP automática y DNS automático.
Avances del día 12 de septiembre:
Flasheamos otro router, en este caso un Linksys WRT54G V6, hicimos exactamente los mismos pasos que con el Linksys WRT54G V5

Avances del día 5 y 19 de septiembre:
Decidimos probar OpenWrt con un router TP-Link modelo TL-WA830RE Versión 2.0 ya que vimos que este router era compatible. :
Los pasos a seguir para reemplazar el firmware del TP-link son los siguientes:

1- Conéctate al router: Conecta tu computadora al router mediante un cable Ethernet para evitar problemas durante la instalación.

2- Accede a la interfaz web: Abre un navegador y dirígete a la dirección IP del router (generalmente `192.168.0.254`). Inicia sesión con las credenciales predeterminadas (usuario: `admin`, contraseña: `admin`).

3- Carga el firmware:
   - Ve a la sección de actualización del firmware en la interfaz web.
   - Cambia el nombre del archivo descargado a `openwrt.bin` para facilitar el proceso.
   - Selecciona el archivo y comienza el proceso de actualización.

4- Espera a que se complete: No interrumpas el proceso de actualización, ya que esto puede dañar el dispositivo.

5- Reinicia el router: Una vez completada la instalación, reinicia el router y accede nuevamente a la interfaz web usando la nueva dirección IP asignada por OpenWrt (normalmente `192.168.1.1`).

Limitaciones: Debido a las especificaciones de hardware del TL-WA830RE, experimentamos limitaciones en funcionalidades avanzadas y rendimiento general.
 
Objetivo
Nuestro principal objetivo con este proyecto es lograr que todos los routers que pasan por nuestro programa logren sus máximas capacidades, en algo más optimizado o simplemente que se pueda regular a gusto, incluso que se pueda hacer overclocking algo que ya open-wrt y dd-wrt ya lograron hace muchos años. Esta tarea es sumamente compleja ya que requiere conocimiento de desarrollo de aplicaciones y firmware muy específico para routers.




Desarrollo/Programas

Los programas que deberíamos desarrollar son el firmware principal que va a funcionar de forma similar a dd-wrt, open-wrt, etc, 




Codigo del programa:

import tkinter as tk
from tkinter import ttk, messagebox
import time

class RouterFlasher:
    def __init__(self, master):
        self.master = master
        master.title("Flasheador de Routers")
        master.geometry("400x300")

        self.router_models = {
            "Linksys WRT54G": {"DDWRT": True, "OpenWRT": True},
            "TP-Link Archer C7": {"DDWRT": True, "OpenWRT": True},
            "Netgear R7000": {"DDWRT": True, "OpenWRT": False},
            "Asus RT-AC68U": {"DDWRT": False, "OpenWRT": True},
            "D-Link DIR-885L": {"DDWRT": False, "OpenWRT": False}
        }

        self.create_widgets()

    def create_widgets(self):
        # Modelo de router
        ttk.Label(self.master, text="Seleccione el modelo de router:").pack(pady=10)
        self.router_var = tk.StringVar()
        self.router_combo = ttk.Combobox(self.master, textvariable=self.router_var)
        self.router_combo['values'] = list(self.router_models.keys())
        self.router_combo.pack(pady=5)
        self.router_combo.bind('<<ComboboxSelected>>', self.update_firmware_options)

        # Opciones de firmware
        self.firmware_var = tk.StringVar()
        self.firmware_frame = ttk.LabelFrame(self.master, text="Firmware compatible")
        self.firmware_frame.pack(pady=10, padx=10, fill="x")
        self.ddwrt_radio = ttk.Radiobutton(self.firmware_frame, text="DD-WRT", variable=self.firmware_var, value="DDWRT", state="disabled")
        self.ddwrt_radio.pack(side="left", padx=5)
        self.openwrt_radio = ttk.Radiobutton(self.firmware_frame, text="OpenWRT", variable=self.firmware_var, value="OpenWRT", state="disabled")
        self.openwrt_radio.pack(side="left", padx=5)

        # Botón de flasheo
        self.flash_button = ttk.Button(self.master, text="Flashear Router", command=self.flash_router, state="disabled")
        self.flash_button.pack(pady=20)

    def update_firmware_options(self, event):
        selected_router = self.router_var.get()
        if selected_router in self.router_models:
            compatibilities = self.router_models[selected_router]
            self.ddwrt_radio['state'] = "normal" if compatibilities["DDWRT"] else "disabled"
            self.openwrt_radio['state'] = "normal" if compatibilities["OpenWRT"] else "disabled"
            
            if compatibilities["DDWRT"] or compatibilities["OpenWRT"]:
                self.flash_button['state'] = "normal"
                if compatibilities["DDWRT"]:
                    self.firmware_var.set("DDWRT")
                elif compatibilities["OpenWRT"]:
                    self.firmware_var.set("OpenWRT")
            else:
                self.flash_button['state'] = "disabled"
                messagebox.showinfo("Incompatibilidad", f"El router {selected_router} no es compatible con DD-WRT ni OpenWRT.")
        else:
            self.ddwrt_radio['state'] = "disabled"
            self.openwrt_radio['state'] = "disabled"
            self.flash_button['state'] = "disabled"

    def flash_router(self):
        router = self.router_var.get()
        firmware = self.firmware_var.get()
        
        # Simulación de conexión al router
        messagebox.showinfo("Conexión", f"Conectando al router {router}...")
        time.sleep(1)  # Simula el tiempo de conexión
        
        # Simulación de flasheo
        messagebox.showinfo("Flasheo", f"Iniciando flasheo de {firmware} en {router}...")
        for i in range(5):
            time.sleep(1)  # Simula el tiempo de flasheo
            messagebox.showinfo("Progreso", f"Flasheo en progreso: {(i+1)*20}%")
        
        messagebox.showinfo("Éxito", f"Flasheo de {firmware} completado exitosamente en {router}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RouterFlasher(root)
    root.mainloop()

















Programa modificado:

from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import time
import os
import shutil
import subprocess
import telnetlib
import threading
import hashlib
import logging

class RouterFlasher:
    def __init__(self, master):
        self.master = master
        master.title("Flasheador de Routers Avanzado")
        master.geometry("600x500")

        # Configurar logging
        logging.basicConfig(filename='router_flasher.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        self.firmware_dir = "firmwares"
        if not os.path.exists(self.firmware_dir):
            os.makedirs(self.firmware_dir)

        self.router_models = {
            "TP-Link TL-WR840N v4": {
                "OpenWRT": "openwrt-23.05.4-ramips-mt76x8-tplink_tl-wr840n-v4-squashfs-tftp-recovery.bin",
                "MD5": "93f4f51c6ef1a4926ecc4aa7c904ee71",
                "IP": "192.168.0.1",
                "Username": "admin",
                "Password": "admin"
            },
            "TP-Link TL-WR1043ND v4": {
                "OpenWRT": "openwrt-23.05.4-ath79-generic-tplink_tl-wr1043nd-v4-squashfs-factory.bin",
                "MD5": "0c0a33d30596f203d2ca402a40c3b846",
                "IP": "192.168.0.1",
                "Username": "admin",
                "Password": "admin"
            },
            "TP-Link Archer C6 v3": {
                "OpenWRT": "openwrt-23.05.4-ramips-mt7621-tplink_archer-c6-v3-squashfs-factory.bin",
                "MD5": "0892e9c436554fc165feba6d12520381",
                "IP": "192.168.0.1",
                "Username": "admin",
                "Password": "admin"
            },
            "TP-Link TL-WR850N v2": {
                "OpenWRT": "openwrt-23.05.4-ramips-mt76x8-tplink_tl-wr850n-v2-squashfs-tftp-recovery.bin",
                "MD5": "68046139fc5f1a2b0b0364e6fe63bb7d",
                "IP": "192.168.0.1",
                "Username": "admin",
                "Password": "admin"
            },
            "TP-Link Archer C7 v5": {
                "OpenWRT": "openwrt-23.05.3-ath79-generic-tplink_archer-c7-v5-squashfs-factory.bin",
                "MD5": "14a5a8d37ed73099a029b387d897ef6d",
                "IP": "192.168.0.1",
                "Username": "admin",
                "Password": "admin"
            },
        }

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")

        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Seleccione el modelo de router:").grid(row=0, column=0, sticky="w", pady=5)
        self.router_var = tk.StringVar()
        self.router_combo = ttk.Combobox(main_frame, textvariable=self.router_var, width=30)
        self.router_combo['values'] = list(self.router_models.keys())
        self.router_combo.grid(row=0, column=1, pady=5)
        self.router_combo.bind('<<ComboboxSelected>>', self.update_firmware_options)

        ttk.Label(main_frame, text="Firmware:").grid(row=1, column=0, sticky="w", pady=5)
        self.firmware_var = tk.StringVar()
        self.firmware_combo = ttk.Combobox(main_frame, textvariable=self.firmware_var, width=30, state="disabled")
        self.firmware_combo.grid(row=1, column=1, pady=5)

        self.flash_button = ttk.Button(main_frame, text="Flashear Router", command=self.start_flashing, state="disabled")
        self.flash_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.progress = ttk.Progressbar(main_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=3, column=0, columnspan=2, pady=10)

        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)

        self.config_button = ttk.Button(main_frame, text="Configurar Red", command=self.configure_network, state="disabled")
        self.config_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.backup_button = ttk.Button(main_frame, text="Realizar Backup", command=self.backup_config)
        self.backup_button.grid(row=6, column=0, columnspan=2, pady=10)

    def update_firmware_options(self, event):
        selected_router = self.router_var.get()
        if selected_router in self.router_models:
            available_firmwares = ["OpenWRT", "Firmware personalizado"]
            self.firmware_combo['values'] = available_firmwares
            self.firmware_combo['state'] = "readonly"
            self.firmware_var.set(available_firmwares[0])
            self.flash_button['state'] = "normal"
        else:
            self.firmware_combo['state'] = "disabled"
            self.flash_button['state'] = "disabled"

    def start_flashing(self):
        router = self.router_var.get()
        firmware = self.firmware_var.get()
        
        if firmware == "Firmware personalizado":
            firmware_file = filedialog.askopenfilename(filetypes=[("Bin files", "*.bin")])
            if not firmware_file:
                return
        else:
            firmware_file = os.path.join(self.firmware_dir, self.router_models[router]["OpenWRT"])

        if not os.path.exists(firmware_file):
            messagebox.showerror("Error", f"Archivo de firmware no encontrado: {firmware_file}")
            return

        if firmware != "Firmware personalizado" and not self.verify_firmware_integrity(router, firmware_file):
            messagebox.showerror("Error", "La verificación de integridad del firmware ha fallado.")
            return

        router_ip = self.router_models[router]["IP"]
        username = self.router_models[router]["Username"]
        password = self.router_models[router]["Password"]

        threading.Thread(target=self.flash_router, args=(router, firmware_file, router_ip, username, password)).start()

    def verify_firmware_integrity(self, router, firmware_file):
        self.update_status("Verificando integridad del firmware...")
        self.update_progress(5)

        md5_hash = hashlib.md5()
        with open(firmware_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        calculated_md5 = md5_hash.hexdigest()

        expected_md5 = self.router_models[router]["MD5"]
        
        if calculated_md5 == expected_md5:
            self.update_status("Verificación de firmware exitosa.")
            self.update_progress(10)
            return True
        else:
            self.update_status("Fallo en la verificación del firmware.")
            self.update_progress(0)
            return False

    def flash_router(self, router, firmware_file, router_ip, username, password):
        max_attempts = 3
        attempt = 0

        while attempt < max_attempts:
            try:
                self.update_status(f"Conectando al router (Intento {attempt + 1})...")
                self.update_progress(10)

                tn = telnetlib.Telnet(router_ip, timeout=10)
                
                self.update_status("Iniciando sesión...")
                self.update_progress(30)

                tn.read_until(b"Login: ", timeout=5)
                tn.write(username.encode('ascii') + b"\n")
                tn.read_until(b"Password: ", timeout=5)
                tn.write(password.encode('ascii') + b"\n")

                response = tn.read_until(b"#", timeout=5)
                if b"#" not in response:
                    raise Exception("Login fallido")

                self.update_status("Iniciando proceso de flasheo...")
                self.update_progress(50)

                tn.write(b"sysupgrade -v " + firmware_file.encode('ascii') + b"\n")

                self.update_status("Flasheando router...")
                self.update_progress(70)

                response = tn.read_until(b"Upgrade completed", timeout=300)

                if b"Upgrade completed" in response:
                    self.update_status("Flasheo completado con éxito")
                    self.update_progress(100)
                    messagebox.showinfo("Éxito", f"Flasheo de {router} completado exitosamente.")
                    messagebox.showinfo("Instrucciones", "Por favor, reinicie su router para completar el proceso de actualización.")
                    self.config_button['state'] = "normal"
                    return
                else:
                    raise Exception("El flasheo no se completó correctamente")

            except Exception as e:
                attempt += 1
                if attempt < max_attempts:
                    retry = messagebox.askyesno("Error de conexión", 
                        f"No se pudo conectar al router. ¿Desea intentar con credenciales diferentes?\n\nError: {str(e)}")
                    if retry:
                        new_credentials = self.ask_credentials()
                        if new_credentials:
                            username, password = new_credentials
                        else:
                            break
                    else:
                        break
                else:
                    self.update_status(f"Error: {str(e)}")
                    messagebox.showerror("Error", f"Error durante el flasheo: {str(e)}")
            finally:
                try:
                    tn.close()
                except:
                    pass

        self.flash_button['state'] = "normal"

    def ask_credentials(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Credenciales")
        dialog.geometry("300x150")
        dialog.transient(self.master)
        dialog.grab_set()

        tk.Label(dialog, text="Ingrese el nombre de usuario:").pack(pady=5)
        username_entry = tk.Entry(dialog)
        username_entry.pack(pady=5)

        tk.Label(dialog, text="Ingrese la contraseña:").pack(pady=5)
        password_entry = tk.Entry(dialog, show="*")
        password_entry.pack(pady=5)

        result = [None, None]

        def on_ok():
            result[0] = username_entry.get()
            result[1] = password_entry.get()
            dialog.destroy()

        def on_cancel():
            dialog.destroy()

        tk.Button(dialog, text="OK", command=on_ok).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="Cancelar", command=on_cancel).pack(side=tk.RIGHT, padx=10, pady=10)

        self.master.wait_window(dialog)

        if result[0] and result[1]:
            return result
        else:
            return None

    def configure_network(self):
        new_ssid = simpledialog.askstring("Configuración", "Ingrese el nuevo nombre de la red WiFi (SSID):")
        new_password = simpledialog.askstring("Configuración", "Ingrese la nueva contraseña de WiFi:", show='*')
        new_admin_password = simpledialog.askstring("Configuración", "Ingrese la nueva contraseña de administrador:", show='*')

        if not all([new_ssid, new_password, new_admin_password]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        router = self.router_var.get()
        router_ip = self.router_models[router]["IP"]
        username = self.router_models[router]["Username"]
        password = self.router_models[router]["Password"]
        threading.Thread(target=self.apply_network_config, args=(router_ip, username, password, new_ssid, new_password, new_admin_password)).start()

    def apply_network_config(self, router_ip, username, password, new_ssid, new_password, new_admin_password):
        try:
            self.update_status("Aplicando nueva configuración de red...")
            self.update_progress(0)

            tn = telnetlib.Telnet(router_ip, timeout=10)
            
            self.update_status("Iniciando sesión...")
            self.update_progress(20)

            tn.read_until(b"Login: ", timeout=5)
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=5)
            tn.write(password.encode('ascii') + b"\n")

            self.update_status("Configurando WiFi...")
            self.update_progress(40)

            tn.write(f"uci set wireless.default_radio0.ssid='{new_ssid}'\n".encode('ascii'))
            tn.write(f"uci set wireless.default_radio0.key='{new_password}'\n".encode('ascii'))
            tn.write(b"uci commit wireless\n")
            tn.write(b"wifi reload\n")

            self.update_status("Configurando contraseña de administrador...")
            self.update_progress(60)

            tn.write(f"passwd\n{new_admin_password}\n{new_admin_password}\n".encode('ascii'))

            self.update_status("Aplicando cambios...")
            self.update_progress(80)

            tn.write(b"uci commit\n")
            tn.write(b"reboot\n")

            tn.close()

            self.update_status("Configuración completada. El router se está reiniciando.")
            self.update_progress(100)
            messagebox.showinfo("Éxito", "La configuración de red se ha aplicado correctamente. El router se está reiniciando.")

        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error durante la configuración de red: {str(e)}")
        finally:
            self.config_button['state'] = "normal"
    
    def backup_config(self):
        router = self.router_var.get()
        if not router:
            messagebox.showerror("Error", "Por favor, seleccione un modelo de router primero.")
            return

        router_ip = self.router_models[router]["IP"]
        username = self.router_models[router]["Username"]
        password = self.router_models[router]["Password"]

        try:
            self.update_status("Realizando backup de la configuración...")
            self.update_progress(0)

            tn = telnetlib.Telnet(router_ip, timeout=10)
            
            tn.read_until(b"Login: ", timeout=5)
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=5)
            tn.write(password.encode('ascii') + b"\n")

            tn.write(b"sysupgrade -b /tmp/backup.tar.gz\n")
            tn.read_until(b"#", timeout=30)

            self.update_progress(50)

            local_filename = filedialog.asksaveasfilename(defaultextension=".tar.gz",
                                                          filetypes=[("Gzip files", "*.tar.gz")])
            if not local_filename:
                tn.close()
                self.update_status("Backup cancelado.")
                return

            tn.write(b"cat /tmp/backup.tar.gz\n")
            backup_data = tn.read_until(b"#", timeout=30)

            with open(local_filename, 'wb') as f:
                f.write(backup_data)

            tn.close()

            self.update_status("Backup completado exitosamente.")
            self.update_progress(100)
            messagebox.showinfo("Éxito", f"Backup guardado en: {local_filename}")

        except Exception as e:
            logging.error(f"Error durante el backup: {str(e)}")
            self.update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error durante el backup: {str(e)}")
        finally:
            self.update_progress(0)

    def update_status(self, message):
        self.status_label.config(text=message)
        self.master.update_idletasks()
        logging.info(message)

    def update_progress(self, value):
        self.progress['value'] = value
        self.master.update_idletasks()

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Puedes cambiar "arc" por otros temas disponibles
    app = RouterFlasher(root)
    root.mainloop()

routers más comprados que sean compatibles con DD-Wrt y OpenWRT: 
TP-Link TL-WR840N (compatible con OpenWRT)
TP-Link Archer C60 (compatible con OpenWRT) 
TP-Link Archer C6 (compatible con OpenWRT)
TP-Link TL-WR850N (compatible con OpenWRT)
TP-Link Archer C7 (compatible con los 2)
Xiaomi Mi Router 4A(compatible con OpenWRT)

Cabe recalcar que este programa no funciona correctamente o dicho de una forma más realista este programa es basura, principalmente lo que está mal en este código es la falta de lógica, estructura y relaciones.









