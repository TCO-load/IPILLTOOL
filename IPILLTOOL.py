import os
import subprocess
import socket
import psutil
import winreg
import colorama
from colorama import Fore, Style, init
import netifaces
import time

init(autoreset=True)

class NetworkManager:
    def __init__(self):
        self.color = Fore.LIGHTYELLOW_EX

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        banner = r"""
         $$$$$$\ $$$$$$$\  $$$$$$\ $$\       $$\       $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
        \_$$  _|$$  __$$\ \_$$  _|$$ |      $$ |      \__$$  __|$$  __$$\ $$  __$$\ $$ |      
          $$ |  $$ |  $$ |  $$ |  $$ |      $$ |         $$ |   $$ /  $$ |$$ /  $$ |$$ |      
          $$ |  $$$$$$$  |  $$ |  $$ |      $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
          $$ |  $$  ____/   $$ |  $$ |      $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
          $$ |  $$ |        $$ |  $$ |      $$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
        $$$$$$\ $$ |      $$$$$$\ $$$$$$$$\ $$$$$$$$\    $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
        \______|\__|      \______|\________|\________|   \__|    \______/  \______/ \________|
        """
        print(self.color + banner)

    def print_menu(self, title, options):
        self.clear_screen()
        self.print_banner()
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{title}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'=' * (len(title) + 4)}{Style.RESET_ALL}")
        for i, option in enumerate(options, 1):
            print(f"{Fore.GREEN}{i}.{Style.RESET_ALL} {option}")
        print(f"{Fore.YELLOW}{'=' * (len(title) + 4)}{Style.RESET_ALL}")

    def get_user_choice(self, max_choice):
        while True:
            try:
                choice = int(input(f"{Fore.CYAN}Choisissez une option (1-{max_choice}): {Style.RESET_ALL}"))
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    print(f"{Fore.RED}Choix invalide. Veuillez entrer un nombre entre 1 et {max_choice}.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrée invalide. Veuillez entrer un nombre.{Style.RESET_ALL}")

    def main_menu(self):
        options = [
            "Configuration réseau de base",
            "Diagnostics et analyses",
            "Sécurité réseau",
            "Configuration avancée",
            "Outils et utilitaires",
            "Quitter"
        ]
        while True:
            self.print_menu("Menu Principal", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.config_menu()
            elif choice == 2:
                self.diag_menu()
            elif choice == 3:
                self.security_menu()
            elif choice == 4:
                self.advanced_menu()
            elif choice == 5:
                self.tools_menu()
            elif choice == 6:
                print(f"{Fore.YELLOW}Au revoir!{Style.RESET_ALL}")
                break

    def config_menu(self):
        options = [
            "Voir les adresses IP",
            "Modifier une adresse IP",
            "Remettre en DHCP",
            "Configurer le proxy système",
            "Gérer les interfaces réseau",
            "Configurer IPv6",
            "Retour au menu principal"
        ]
        while True:
            self.print_menu("Configuration réseau de base", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.view_ip()
            elif choice == 2:
                self.modify_ip()
            elif choice == 3:
                self.set_dhcp()
            elif choice == 4:
                self.config_proxy()
            elif choice == 5:
                self.manage_interfaces()
            elif choice == 6:
                self.config_ipv6()
            elif choice == 7:
                break
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

    def diag_menu(self):
        options = [
            "Tester la connexion",
            "Afficher les statistiques réseau",
            "Analyser la bande passante",
            "Scanner les ports ouverts",
            "Analyser le trafic réseau",
            "Diagnostiquer et réparer le réseau",
            "Analyser les vulnérabilités réseau",
            "Retour au menu principal"
        ]
        while True:
            self.print_menu("Diagnostics et analyses", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.test_connection()
            elif choice == 2:
                self.show_network_stats()
            elif choice == 3:
                self.analyze_bandwidth()
            elif choice == 4:
                self.scan_ports()
            elif choice == 5:
                self.analyze_traffic()
            elif choice == 6:
                self.diagnose_repair_network()
            elif choice == 7:
                self.analyze_vulnerabilities()
            elif choice == 8:
                break
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

    def security_menu(self):
        options = [
            "Gérer les règles du pare-feu",
            "Configurer le pare-feu avancé",
            "Gérer les certificats de sécurité",
            "Configurer IPsec",
            "Configurer l'authentification 802.1X",
            "Gérer les paramètres de sécurité réseau avancés",
            "Configurer le contrôle parental réseau",
            "Retour au menu principal"
        ]
        while True:
            self.print_menu("Sécurité réseau", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.manage_firewall()
            elif choice == 2:
                self.config_adv_firewall()
            elif choice == 3:
                self.manage_certs()
            elif choice == 4:
                self.config_ipsec()
            elif choice == 5:
                self.config_8021x()
            elif choice == 6:
                self.advanced_net_security()
            elif choice == 7:
                self.config_parental_control()
            elif choice == 8:
                break
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

    def advanced_menu(self):
        options = [
            "Gérer les paramètres TCP/IP avancés",
            "Configurer la qualité de service (QoS)",
            "Gérer les connexions VPN",
            "Configurer le routage et l'accès distant",
            "Gérer les protocoles réseau",
            "Configurer les stratégies de groupe réseau",
            "Gérer les cartes réseau virtuelles",
            "Retour au menu principal"
        ]
        while True:
            self.print_menu("Configuration avancée", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.manage_tcpip()
            elif choice == 2:
                self.config_qos()
            elif choice == 3:
                self.manage_vpn()
            elif choice == 4:
                self.config_rras()
            elif choice == 5:
                self.manage_net_protocols()
            elif choice == 6:
                self.configure_net_gpo()
            elif choice == 7:
                self.manage_virtual_nics()
            elif choice == 8:
                break
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

    def tools_menu(self):
        options = [
            "Vider le cache DNS",
            "Afficher la table de routage",
            "Afficher les connexions actives",
            "Afficher l'historique des connexions Wi-Fi",
            "Afficher les mots de passe Wi-Fi",
            "Gérer les accès Wi-Fi invités",
            "Afficher et gérer les partages réseau",
            "Gérer les connexions RDP",
            "Retour au menu principal"
        ]
        while True:
            self.print_menu("Outils et utilitaires", options)
            choice = self.get_user_choice(len(options))
            if choice == 1:
                self.flush_dns()
            elif choice == 2:
                self.show_routing_table()
            elif choice == 3:
                self.show_active_connections()
            elif choice == 4:
                self.show_wifi_history()
            elif choice == 5:
                self.show_wifi_passwords()
            elif choice == 6:
                self.manage_guest_wifi()
            elif choice == 7:
                self.manage_shares()
            elif choice == 8:
                self.manage_rdp()
            elif choice == 9:
                break
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

    def view_ip(self):
        print(f"{Fore.CYAN}Adresses IP actuelles :{Style.RESET_ALL}")
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    print(f"{Fore.GREEN}{interface}: {Fore.YELLOW}{addr.address}{Style.RESET_ALL}")

    def modify_ip(self):
        interfaces = list(psutil.net_if_addrs().keys())
        print(f"{Fore.CYAN}Interfaces disponibles :{Style.RESET_ALL}")
        for i, interface in enumerate(interfaces, 1):
            print(f"{Fore.GREEN}{i}. {interface}{Style.RESET_ALL}")
        
        choice = self.get_user_choice(len(interfaces))
        interface = interfaces[choice - 1]
        
        new_ip = input(f"{Fore.CYAN}Nouvelle adresse IP : {Style.RESET_ALL}")
        new_mask = input(f"{Fore.CYAN}Nouveau masque de sous-réseau : {Style.RESET_ALL}")
        new_gateway = input(f"{Fore.CYAN}Nouvelle passerelle : {Style.RESET_ALL}")
        
        try:
            subprocess.run(["netsh", "interface", "ip", "set", "address", 
                            f"name={interface}", "static", new_ip, new_mask, new_gateway], 
                           check=True, capture_output=True)
            print(f"{Fore.GREEN}Adresse IP modifiée avec succès.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Erreur lors de la modification de l'adresse IP : {e.output.decode()}{Style.RESET_ALL}")

    def set_dhcp(self):
        interfaces = list(psutil.net_if_addrs().keys())
        print(f"{Fore.CYAN}Interfaces disponibles :{Style.RESET_ALL}")
        for i, interface in enumerate(interfaces, 1):
            print(f"{Fore.GREEN}{i}. {interface}{Style.RESET_ALL}")
        
        choice = self.get_user_choice(len(interfaces))
        interface = interfaces[choice - 1]
        
        try:
            subprocess.run(["netsh", "interface", "ip", "set", "address", 
                            f"name={interface}", "dhcp"], 
                           check=True, capture_output=True)
            print(f"{Fore.GREEN}Interface configurée en DHCP avec succès.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Erreur lors de la configuration en DHCP : {e.output.decode()}{Style.RESET_ALL}")

    def config_proxy(self):
        print(f"{Fore.YELLOW}Configuration du proxy :{Style.RESET_ALL}")
        proxy_enable = input(f"{Fore.CYAN}Activer le proxy ? (o/n) : {Style.RESET_ALL}").lower() == 'o'
        if proxy_enable:
            proxy_server = input(f"{Fore.CYAN}Adresse du serveur proxy : {Style.RESET_ALL}")
            proxy_port = input(f"{Fore.CYAN}Port du proxy : {Style.RESET_ALL}")
            
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, f"{proxy_server}:{proxy_port}")
            winreg.CloseKey(key)
            print(f"{Fore.GREEN}Proxy configuré avec succès.{Style.RESET_ALL}")
        else:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"{Fore.GREEN}Proxy désactivé.{Style.RESET_ALL}")

    def manage_interfaces(self):
        interfaces = list(psutil.net_if_addrs().keys())
        print(f"{Fore.CYAN}Interfaces réseau :{Style.RESET_ALL}")
        for i, interface in enumerate(interfaces, 1):
            print(f"{Fore.GREEN}{i}. {interface}{Style.RESET_ALL}")
        
        choice = self.get_user_choice(len(interfaces))
        interface = interfaces[choice - 1]
        
        print(f"{Fore.YELLOW}Actions disponibles :{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Activer l'interface{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Désactiver l'interface{Style.RESET_ALL}")
        action = self.get_user_choice(2)
        
        try:
            if action == 1:
                subprocess.run(["netsh", "interface", "set", "interface", interface, "enable"], check=True, capture_output=True)
                print(f"{Fore.GREEN}Interface {interface} activée avec succès.{Style.RESET_ALL}")
            else:
                subprocess.run(["netsh", "interface", "set", "interface", interface, "disable"], check=True, capture_output=True)
                print(f"{Fore.GREEN}Interface {interface} désactivée avec succès.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Erreur lors de la gestion de l'interface : {e.output.decode()}{Style.RESET_ALL}")

    def config_ipv6(self):
        interfaces = list(psutil.net_if_addrs().keys())
        print(f"{Fore.CYAN}Interfaces disponibles :{Style.RESET_ALL}")
        for i, interface in enumerate(interfaces, 1):
            print(f"{Fore.GREEN}{i}. {interface}{Style.RESET_ALL}")
        
        choice = self.get_user_choice(len(interfaces))
        interface = interfaces[choice - 1]
        
        print(f"{Fore.YELLOW}Actions disponibles :{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Activer IPv6{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Désactiver IPv6{Style.RESET_ALL}")
        action = self.get_user_choice(2)
        
        try:
            if action == 1:
                subprocess.run(["netsh", "interface", "ipv6", "set", "interface", interface, "enabled"], check=True, capture_output=True)
                print(f"{Fore.GREEN}IPv6 activé sur l'interface {interface}.{Style.RESET_ALL}")
            else:
                subprocess.run(["netsh", "interface", "ipv6", "set", "interface", interface, "disabled"], check=True, capture_output=True)
                print(f"{Fore.GREEN}IPv6 désactivé sur l'interface {interface}.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Erreur lors de la configuration IPv6 : {e.output.decode()}{Style.RESET_ALL}")

    def test_connection(self):
        host = input(f"{Fore.CYAN}Entrez l'adresse à tester (par défaut: google.com): {Style.RESET_ALL}") or "google.com"
        try:
            result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
            print(result.stdout)
            if "Perte" in result.stdout:
                loss = result.stdout.split("Perte")[1].split("%")[0].strip()
                if int(loss) == 0:
                    print(f"{Fore.GREEN}Connexion stable vers {host}.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}Connexion instable vers {host}. Perte de paquets: {loss}%{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Impossible de joindre {host}{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors du test de connexion{Style.RESET_ALL}")

    def show_network_stats(self):
        stats = psutil.net_io_counters(pernic=True)
        print(f"{Fore.CYAN}Statistiques réseau :{Style.RESET_ALL}")
        for interface, stat in stats.items():
            print(f"{Fore.GREEN}{interface}:{Style.RESET_ALL}")
            print(f"  Octets envoyés : {stat.bytes_sent}")
            print(f"  Octets reçus   : {stat.bytes_recv}")
            print(f"  Paquets envoyés: {stat.packets_sent}")
            print(f"  Paquets reçus  : {stat.packets_recv}")
            print(f"  Erreurs en envoi: {stat.errin}")
            print(f"  Erreurs en réception: {stat.errout}")
            print(f"  Paquets supprimés en envoi: {stat.dropin}")
            print(f"  Paquets supprimés en réception: {stat.dropout}")

    def analyze_bandwidth(self):
        print(f"{Fore.YELLOW}Analyse de la bande passante en cours...{Style.RESET_ALL}")
        start = psutil.net_io_counters()
        time.sleep(1)
        end = psutil.net_io_counters()
        
        bw_upload = (end.bytes_sent - start.bytes_sent) * 8 / 1000000
        bw_download = (end.bytes_recv - start.bytes_recv) * 8 / 1000000
        
        print(f"{Fore.GREEN}Bande passante montante  : {bw_upload:.2f} Mbps{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Bande passante descendante: {bw_download:.2f} Mbps{Style.RESET_ALL}")

    def scan_ports(self):
        target = input(f"{Fore.CYAN}Entrez l'adresse IP à scanner: {Style.RESET_ALL}")
        start_port = int(input(f"{Fore.CYAN}Port de début: {Style.RESET_ALL}"))
        end_port = int(input(f"{Fore.CYAN}Port de fin: {Style.RESET_ALL}"))

        print(f"{Fore.YELLOW}Scan des ports en cours...{Style.RESET_ALL}")
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Fore.GREEN}Port {port} est ouvert{Style.RESET_ALL}")
            sock.close()

    def analyze_traffic(self):
        print(f"{Fore.YELLOW}Analyse du trafic réseau en cours...{Style.RESET_ALL}")
        try:
            result = subprocess.run(["netstat", "-n"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'analyse du trafic réseau{Style.RESET_ALL}")

    def diagnose_repair_network(self):
        print(f"{Fore.YELLOW}Diagnostic et réparation du réseau en cours...{Style.RESET_ALL}")
        try:
            subprocess.run(["ipconfig", "/release"], check=True)
            subprocess.run(["ipconfig", "/renew"], check=True)
            subprocess.run(["ipconfig", "/flushdns"], check=True)
            subprocess.run(["netsh", "winsock", "reset"], check=True)
            print(f"{Fore.GREEN}Diagnostic et réparation terminés. Veuillez redémarrer votre ordinateur.{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors du diagnostic et de la réparation du réseau{Style.RESET_ALL}")

    def analyze_vulnerabilities(self):
        print(f"{Fore.YELLOW}Analyse des vulnérabilités réseau...{Style.RESET_ALL}")
        try:
            result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
            print(result.stdout)
            if "Activé" not in result.stdout:
                print(f"{Fore.RED}Attention : Le pare-feu Windows semble être désactivé.{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'analyse des vulnérabilités{Style.RESET_ALL}")

    def manage_firewall(self):
        print(f"{Fore.YELLOW}Gestion du pare-feu Windows{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Activer le pare-feu{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2. Désactiver le pare-feu{Style.RESET_ALL}")
        print(f"{Fore.GREEN}3. Afficher l'état du pare-feu{Style.RESET_ALL}")
        choice = self.get_user_choice(3)
        
        try:
            if choice == 1:
                subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"], check=True)
                print(f"{Fore.GREEN}Pare-feu activé.{Style.RESET_ALL}")
            elif choice == 2:
                subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "off"], check=True)
                print(f"{Fore.GREEN}Pare-feu désactivé.{Style.RESET_ALL}")
            else:
                result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
                print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de la gestion du pare-feu{Style.RESET_ALL}")

    def config_adv_firewall(self):
        print(f"{Fore.YELLOW}Configuration avancée du pare-feu non implémentée.{Style.RESET_ALL}")

    def manage_certs(self):
        print(f"{Fore.YELLOW}Gestion des certificats non implémentée.{Style.RESET_ALL}")

    def config_ipsec(self):
        print(f"{Fore.YELLOW}Configuration IPsec non implémentée.{Style.RESET_ALL}")

    def config_8021x(self):
        print(f"{Fore.YELLOW}Configuration 802.1X non implémentée.{Style.RESET_ALL}")

    def advanced_net_security(self):
        print(f"{Fore.YELLOW}Paramètres de sécurité réseau avancés non implémentés.{Style.RESET_ALL}")

    def config_parental_control(self):
        print(f"{Fore.YELLOW}Configuration du contrôle parental non implémentée.{Style.RESET_ALL}")

    def manage_tcpip(self):
        print(f"{Fore.YELLOW}Gestion des paramètres TCP/IP avancés non implémentée.{Style.RESET_ALL}")

    def config_qos(self):
        print(f"{Fore.YELLOW}Configuration de la QoS non implémentée.{Style.RESET_ALL}")

    def manage_vpn(self):
        print(f"{Fore.YELLOW}Gestion des connexions VPN non implémentée.{Style.RESET_ALL}")

    def config_rras(self):
        print(f"{Fore.YELLOW}Configuration du routage et accès distant non implémentée.{Style.RESET_ALL}")

    def manage_net_protocols(self):
        print(f"{Fore.YELLOW}Gestion des protocoles réseau non implémentée.{Style.RESET_ALL}")

    def configure_net_gpo(self):
        print(f"{Fore.YELLOW}Configuration des stratégies de groupe réseau non implémentée.{Style.RESET_ALL}")

    def manage_virtual_nics(self):
        print(f"{Fore.YELLOW}Gestion des cartes réseau virtuelles non implémentée.{Style.RESET_ALL}")

    def flush_dns(self):
        try:
            subprocess.run(["ipconfig", "/flushdns"], check=True, capture_output=True)
            print(f"{Fore.GREEN}Cache DNS vidé avec succès.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Erreur lors du vidage du cache DNS : {e.output.decode()}{Style.RESET_ALL}")

    def show_routing_table(self):
        try:
            result = subprocess.run(["route", "print"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'affichage de la table de routage{Style.RESET_ALL}")

    def show_active_connections(self):
        try:
            result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'affichage des connexions actives{Style.RESET_ALL}")

    def show_wifi_history(self):
        try:
            result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'affichage de l'historique Wi-Fi{Style.RESET_ALL}")

    def show_wifi_passwords(self):
        try:
            profiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:] for i in profiles if "Tous les profils utilisateurs" in i]
            for profile in profiles:
                try:
                    results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode('utf-8').split('\n')
                    results = [b.split(":")[1][1:] for b in results if "Contenu de la clé" in b]
                    try:
                        print(f"{Fore.GREEN}{profile} : {results[0]}{Style.RESET_ALL}")
                    except IndexError:
                        print(f"{Fore.YELLOW}{profile} : {Fore.RED}Impossible d'obtenir le mot de passe{Style.RESET_ALL}")
                except subprocess.CalledProcessError:
                    print(f"{Fore.YELLOW}{profile} : {Fore.RED}Erreur lors de l'obtention du mot de passe{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'obtention des profils Wi-Fi{Style.RESET_ALL}")

    def manage_guest_wifi(self):
        print(f"{Fore.YELLOW}Gestion des accès Wi-Fi invités non implémentée.{Style.RESET_ALL}")

    def manage_shares(self):
        try:
            result = subprocess.run(["net", "share"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Erreur lors de l'affichage des partages réseau{Style.RESET_ALL}")

    def manage_rdp(self):
        print(f"{Fore.YELLOW}Gestion des connexions RDP non implémentée.{Style.RESET_ALL}")

    def run_as_admin(self):
        import ctypes
        import sys

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit(0)

if __name__ == "__main__":
    manager = NetworkManager()
    manager.run_as_admin()  # Assurez-vous d'exécuter en tant qu'administrateur
    manager.main_menu()