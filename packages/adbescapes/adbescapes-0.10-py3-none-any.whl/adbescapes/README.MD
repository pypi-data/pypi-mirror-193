### Makes strings compatible for "adb shell input text ..."


#### The string escape functions use numba under the hood - that means the first run is very slow (compile time)


##### pip install adbescapes

```python

from adbescapes import ADBInputEscaped

adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:5555"
adbk = ADBInputEscaped(adb_path=adb_path, deviceserial=deviceserial)
adbk.connect_to_device()
adbk.activate_debug()
adbk.escape_text_and_send(
    "'ąćęłń'\tóśźż\nĄĆĘŁŃÓŚŹŻ\n\"Junto à Estação de \nCarcavelos;\"" "äöüÄÖÜß",
    respect_german_letters=False,
    exit_keys="ctrl+x",
)

adbk.escape_text_and_send_with_delay(
    """

    "Müller\n&Ärger,ändern,\nKüche,Übung, Köchin, Öl\ngroß 

    """,
    delay=(0.01, 0.2),
    respect_german_letters=True,
    exit_keys="ctrl+x",
)



debug output:

input text \'aceln\'\ \ \ \ oszz
input keyevent 66
input text ACELNOSZZ
input keyevent 66
input text \"Junto\ a\ Estacao\ de\ 
input keyevent 66
input text Carcavelos\;\"aouAOUb
input keyevent 66
input keyevent 66
sleep 0.072
input text \ 
sleep 0.103
input text \ 
sleep 0.109
input text \ 
sleep 0.066
input text \ 
sleep 0.159
input text \"
sleep 0.134
input text M

....

```

![Result](https://github.com/hansalemaos/screenshots/raw/main/adboutput2.png)


![Debug](https://github.com/hansalemaos/screenshots/raw/main/adboutput1.png)

