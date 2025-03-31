import requests
import time
from colorama import init

# Initialiser colorama
init(autoreset=True)

# Texte ASCII avec dégradé de couleur
ascii_art = [
    "    _            __            __              ",
    "   (_)___       / /___  ____  / /____  ______           ",
    "  / / __ \\     / / __ \\/ __ \\/ //_/ / / / __ \\          ",
    " / / /_/ /    / / /_/ / /_/ / ,< / /_/ / /_/ /          ",
    "/_/ .___/    /_/\\____/\\____/_/|_|\\__,_/ .___/           ",
    " /_/                                 /_/                 "
]

def get_gradient_color(index, total):
    """Retourne un code couleur basé sur un dégradé d'orange à rouge."""
    red = 255
    green = int(165 * (1 - (index / total)))  # Orange à rouge
    return f"\033[38;2;{red};{green};0m"  # Code couleur ANSI

def print_ascii_with_gradient(ascii_art):
    """Affiche le texte ASCII avec un dégradé de couleur."""
    total_lines = len(ascii_art)
    for i, line in enumerate(ascii_art):
        color = get_gradient_color(i, total_lines)
        print(f"{color}{line}")

def get_ip_info(ip_address):
    """Récupère les informations sur l'adresse IP."""
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        data = response.json()
        if 'error' in data:
            return f"Erreur: {data['reason']}"
        return {
            "ip": data.get('ip'),
            "region": data.get('region'),
            "country": data.get('country'),
            "postal": data.get('postal'),
            "org": data.get('org'),
            "latitude": data.get('latitude'),
            "longitude": data.get('longitude'),
            "timezone": data.get('timezone'),
            "asn": data.get('asn'),
            "calling_code": data.get('calling_code'),
            "continent": data.get('continent_name'),
            "languages": data.get('languages'),
        }
    except Exception as e:
        return f"Erreur lors de la récupération des informations IP: {e}"

def loading_bar(duration):
    """Affiche une barre de chargement pendant la durée spécifiée en secondes."""
    bar_length = 30  # Longueur de la barre de chargement
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        bar = '#' * i + '-' * (bar_length - i)
        print(f"\r[{bar}] {percent:.0f}%", end="")
        time.sleep(duration / bar_length)
    print()  # Nouvelle ligne après la barre de chargement

def print_with_delay(text, delay=0.1):
    """Affiche le texte lettre par lettre avec un délai."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Nouvelle ligne après le texte

def main():
    # Affichage de l'ASCII art avec dégradé
    print_ascii_with_gradient(ascii_art)
    print("\n[Rejoignez notre serveur Discord] ici -----> [https://discord.com/invite/VnpqGPc9zM]")
    ip_address = input("[Entrez l'adresse IP publique ou] \n L Adresse IPv6 ou \n   L Adresse IPv6 temporaire \n     L IP que vous souhaitez consulter:")
    
    # Afficher la barre de chargement pendant 5 secondes
    print("\nChargement des informations, veuillez patienter...")
    loading_bar(1)
    
    ip_info = get_ip_info(ip_address)
    
    if isinstance(ip_info, dict):
        print("")
        print(f"\n91.169.57.129Informations pour l'adresse IP: {ip_info['ip']}")
        
       
        print("""
 ██████╗ ███████╗     █████╗ ██████╗      █████╗ ███████╗    ███████╗ ██╗    ███████╗ ██████╗ 
██╔═████╗╚════██║    ██╔══██╗╚════██╗    ██╔══██╗██╔════╝    ██╔════╝███║    ██╔════╝██╔════╝ 
██║██╔██║    ██╔╝    ╚█████╔╝ █████╔╝    ╚██████║███████╗    ███████╗╚██║    ███████╗███████╗ 
████╔╝██║   ██╔╝     ██╔══██╗██╔═══╝      ╚═══██║╚════██║    ╚════██║ ██║    ╚════██║██╔═══██╗
╚██████╔╝   ██║      ╚█████╔╝███████╗     █████╔╝███████║    ███████║ ██║    ███████║╚██████╔╝
 ╚═════╝    ╚═╝       ╚════╝ ╚══════╝     ╚════╝ ╚══════╝    ╚══════╝ ╚═╝    ╚══════╝ ╚═════╝ """)

        # Afficher chaque information lettre par lettre avec un délai de 1 seconde
        print_with_delay(f"Région: {ip_info['region']}", 0.030)
        print_with_delay(f"Pays: {ip_info['country']}", 0.019)
        print_with_delay(f"Code postal: {ip_info['postal']}", 0.019)
        print_with_delay(f"Fournisseur d'accès: {ip_info['org']}", 0.019)
        print_with_delay(f"Latitude: {ip_info['latitude']}, Longitude: {ip_info['longitude']}", 0.019)
        print_with_delay(f"Fuseau horaire: {ip_info['timezone']}", 0.019)
        print_with_delay(f"ASN: {ip_info['asn']}", 0.019)
        
        if ip_info.get('calling_code'):
            print_with_delay(f"Code d'appel: {ip_info['calling_code']}", 0.019)
        
        if ip_info.get('continent'):
            print_with_delay(f"Continent: {ip_info['continent']}", 0.019)
            
        if ip_info.get('languages'):
            primary_language = ip_info['languages'].split(',')[0] if ',' in ip_info['languages'] else ip_info['languages']
            print_with_delay(f"Langue: {primary_language.strip()}", 0.019)
    
        # Demande à l'utilisateur s'il a le numéro de la victime
        victim_number = input("\nAvez-vous le numéro de la victime ? (oui/non): ")
        if victim_number.lower() == "oui":
            victim_contact = input("Veuillez entrer le numéro de la victime: ")
            print_with_delay(f"Vous avez entré: {victim_contact}", 0.019)
        else:
            print_with_delay("Merci, aucune action supplémentaire requise.", 0.019)
    else:
        print(ip_info)

if __name__ == "__main__":
    main()
