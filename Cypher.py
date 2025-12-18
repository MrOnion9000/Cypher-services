# Hi skid
# Made by MrOnion9000

# DO NOT CHANGE ANYTHING IF YOU DONT KNOW WHAT YOURE DOING!!

# DO NOT CHANGE ANYTHING IF YOU DONT KNOW WHAT YOURE DOING!!

# DO NOT CHANGE ANYTHING IF YOU DONT KNOW WHAT YOURE DOING!!

# DO NOT CHANGE ANYTHING IF YOU DONT KNOW WHAT YOURE DOING!!

#    XX             XX      XX         XX
#      XX         XX         XX      XX
#       XX      XX             XX  XX 
#         XX  XX                 XX
#           XX                 XX  XX
#         XX  XX              XX     XX
#        XX     XX          XX         XX
#      XX         XX      XX            XX
#     XX            XX  XX                XX
#
#        
#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# I AM NOT HELD ACCOUNTABLE FOR ANY MISUSE OF MY PROJECT

# I AM NOT HELD ACCOUNTABLE FOR ANY MISUSE OF MY PROJECT

# I AM NOT HELD ACCOUNTABLE FOR ANY MISUSE OF MY PROJECT

# I AM NOT HELD ACCOUNTABLE FOR ANY MISUSE OF MY PROJECT

# MORE FEATURES COMING SOON!
# join discord.gg/wzGM9qtjVj if you have any ideas or want help troubleshooting!

import os, sys, time, random, subprocess, threading, ctypes, requests, base64, zlib


# UAC(User Account Control)
def ensure_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit()

ensure_admin()
# -----
# title
# -----
os.system("title Cypher Services")
GREEN = "\033[32m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# 
# code fall bit
# 
def falling_code(duration=2.5, width=80, density=0.02):
    end = time.time() + duration
    while time.time() < end:
        line = ''.join(random.choice("01{}[]()<>;:.,-+*/\\|^%$#@!~") if random.random() < density else " " for _ in range(width))
        print(GREEN + line + RESET)
        time.sleep(0.03)
# -----------
# menu screen
# ------------
def header():
    clear()
    print(GREEN + """
      █████   ██   ██  ██████   ██   ██ ██████  ██████ 
     ██        ██ ██   ██   ██  ██   ██ ██      ██   ██
     ██         ███    ██████   ███████ ██████  ██████ 
     ██          █     ██       ██   ██ ██      ██   ██
      █████      █     ██       ██   ██ ██████  ██   ██

    """ + RESET)
    print(GREEN + "         Cypher services - MrOnion9000 \n" + RESET)
    print("-" * 70)
# ------------
# ip looker
# ------------
def get_ip_geo(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=8); r.raise_for_status()
    except Exception as e:
        print("Network error:", e); return
    d = r.json()
    if d.get("status") != "success":
        print("Failed:", d.get("message")); return
    for k in ("query","country","regionName","city","lat","lon","isp","timezone"):
        print(f"{k}: {d.get(k)}")
    print("Note: results are approximate.")

# =========================
#   COORDINATE CONVERTER
# =========================

def decimal_to_dms(value):
    degrees = int(value)
    minutes_float = abs(value - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    return degrees, minutes, seconds

def format_dms(lat, lon):
    lat_deg, lat_min, lat_sec = decimal_to_dms(lat)
    lon_deg, lon_min, lon_sec = decimal_to_dms(lon)

    lat_dir = "N" if lat >= 0 else "S"
    lon_dir = "E" if lon >= 0 else "W"

    lat_str = f"{abs(lat_deg)}°{lat_min}'{lat_sec:.2f}\" {lat_dir}"
    lon_str = f"{abs(lon_deg)}°{lon_min}'{lon_sec:.2f}\" {lon_dir}"

    return lat_str, lon_str

def to_google_maps(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"

def coord_converter():
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))
    except:
        print("Invalid format. Use lat and long from the ip looker.")
        input("Enter to continue...")
        return

    print("\nDecimal coordinates:")
    print(lat, lon)

    lat_dms, lon_dms = format_dms(lat, lon)

    print("\nDMS coordinates:")
    print(lat_dms)
    print(lon_dms)

    print("\nGoogle Maps link:")
    print(to_google_maps(lat, lon))

    input("\nPress Enter to continue...")

# --------------------
# wifi sniffer (local)
# --------------------
def wifi_sniffer():
    if os.name != "nt":
        print("Wifi sniffer only runs on Windows."); input("Enter..."); return
    try:
        out = subprocess.check_output("netsh wlan show profile", shell=True, text=True, encoding="utf-8", errors="ignore"); print(out)
    except Exception as e:
        print("Error:", e); input("Enter..."); return
    wifi = input("Enter EXACT Wi-Fi profile name: ").strip()
    if not wifi: return
    try:
        det = subprocess.check_output(f'netsh wlan show profile name="{wifi}" key=clear', shell=True, text=True, encoding="utf-8", errors="ignore")
        print(det)
    except Exception as e:
        print("Error:", e)
    input("Enter to continue...")
# -----------------
# Part of ip looker
# -----------------
def ip_looker():
    ip = input("Enter IP: ").strip()
    if not ip: return
    get_ip_geo(ip)
    input("Enter to continue...")

# -----------------------------
#   defender enabler
# -----------------------------

def disable_defender():
    choice = input("Do you wish to disable Windows Defender? (yes/no): ").lower()
    if choice == "yes":
        cmd = r'PowerShell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"'
        subprocess.run(cmd, shell=True)
        print("Windows Defender realtime protection DISABLED.")
    else:
        print("Cancelled.")
    input("Enter to continue...")

# ---------------
# defender disabler
# ---------------
def enable_defender():
    choice = input("Do you wish to enable Windows Defender? (yes/no): ").lower()
    if choice == "yes":
        cmd = r'PowerShell -Command "Set-MpPreference -DisableRealtimeMonitoring $false"'
        subprocess.run(cmd, shell=True)
        print("Windows Defender realtime protection ENABLED.")
    else:
        print("Cancelled.")
    input("Enter to continue...")
# -------
# ro grabber
# --------
def ro_grabber():
    print("Check out Ro-Ip-Grabber.txt for more becuase its super sophistcated...")
    input("Enter to continue...")
# ---------------
# code obfuscator
# ----------------
def py_obfuscator():
    print("Paste your Python code.")
    print("Type END(all caps) on a new line when finished.\n")

    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    source = "\n".join(lines)
    encoded = base64.b64encode(zlib.compress(source.encode("utf-8"))).decode("ascii")

    print("\n--- OBFUSCATED CODE ---\n")
    print(f"import base64,zlib;exec(zlib.decompress(base64.b64decode({encoded!r})).decode('utf-8'))")
    input("Press enter to continue")


# -----------------------------
# menu layout 
# -----------------------------

def menu():
    while True:
        clear()
        falling_code(duration=1.5)
        header()
        print(GREEN + "[1] IP Looker   [2] Wifi Sniffer   [3] Disable Defender" + RESET)
        print(GREEN + "[4] Enable Defender   [5] Coordinate converter"  + RESET)
        print(GREEN + "[6] Python code obfuscator   [7] Ro-Grabber-IP    [8] Exit  " + RESET)

        choice = input("Select> ").strip().lower()

        if choice in ("8","exit"):
            break
        elif choice == "1": ip_looker()
        elif choice == "2": wifi_sniffer()
        elif choice == "3": disable_defender()
        elif choice == "4": enable_defender()
        elif choice == "5": coord_converter()
        elif choice == "6": py_obfuscator()
        elif choice == "7": ro_grabber ()
        else:
            print("Invalid input, try again"); time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        pass
    finally:
        try: input("\nPress Enter to exit...")
        except: pass
        sys.exit(0)
