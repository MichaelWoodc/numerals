"C:\Program Files\PsychoPy\python.exe" "numbers_ro_lastrun.py" 10 mandarin_path

works to launch the next one from powershell, need to fix code to do that from psychopy experiment

This works perfectly on windows to launch without it having a dependency on parent:
**subprocess**.Popen(
    [
r"C:\Program Files\PsychoPy\python.exe",
"numbers_ro_lastrun.py",
"10",
"mandarin_path"
    ],
cwd**=**r"C:\Users\micha\OneDrive - Georgia Southern University\numerals",
creationflags**=**0x00000008**|**0x00000200,
close_fds**=**True
)

import subprocess
import sys
import os

script_path = os.path.join(
    os.getcwd(),
    "numbers_ro_lastrun.py"
)

args = [
    sys.executable,   # uses current Python (important for cross-platform)
    script_path,
    str(number_trials),
    str(language)
]

if sys.platform == "win32":
    subprocess.Popen(
        args,
        cwd=os.getcwd(),
        creationflags=0x00000008 | 0x00000200,
        close_fds=True
    )
else:
    subprocess.Popen(
        args,
        cwd=os.getcwd(),
        start_new_session=True,
        close_fds=True
    )





## THIS WORKS PERFECTLY!


import subprocess
import platform

number_trials = correct + incorrect
language = expInfo['Language']

script_path = os.path.join(os.getcwd(), "numbers_ro_lastrun.py")

args = [
    sys.executable,
    script_path,
    str(number_trials),
    str(language)
]

system = platform.system()

# ------------------------

# WINDOWS

# ------------------------

if system == "Windows":
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200

    subprocess.Popen(
        args,
        cwd=os.getcwd(),
        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
        close_fds=True
    )

# ------------------------

# macOS / Linux

# ------------------------

else:
    subprocess.Popen(
        args,
        cwd=os.getcwd(),
        start_new_session=True,
        close_fds=True
    )
