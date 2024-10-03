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