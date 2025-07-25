from AppKit import NSWorkspace
import time
import subprocess

def log(logger, msg):
    if logger:
        logger(msg)
    else:
        print(msg)

def focus(logger=None):
    log(logger, "Trying to focus app...")
    app_name = "java"
    ws = NSWorkspace.sharedWorkspace()
    apps = ws.runningApplications()
    for app in apps:
        if app.localizedName() == app_name:
            app.activateWithOptions_(1 << 1)
            time.sleep(0.5)
            log(logger, "App found but not focused, trying to click...")
            subprocess.run([
                "osascript", "-e",
                'tell application "System Events" to tell process "java" to set frontmost to true'
            ])
            subprocess.run([
                "osascript", "-e",
                'tell application "System Events" to click at {800, 300}'
            ])
            return True
    log(logger, "PokeMMO app not found.")
    return False
