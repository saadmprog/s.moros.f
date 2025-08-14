import os, getpass

r = "\033[31m"
w = "\033[37m"
p = "\033[35m"
y = "\033[33m"
g = "\033[32m"






def tool_logo():
    print(f"""
{p}╔════════════════════════════════════════════════════════════════════════════════════════╗
{p}║{y}     ███████╗   ███╗   ███╗ ██████╗ ██████╗  ██████╗ ███████╗   ███████╗   ██████╗      {p}║
{p}║{y}     ██╔════╝   ████╗ ████║██╔═══██╗██╔══██╗██╔═══██╗██╔════╝   ██╔════╝   ██╔══██╗     {p}║
{p}║{y}     ███████╗   ██╔████╔██║██║   ██║██████╔╝██║   ██║███████╗   █████╗     ██║  ██║     {p}║
{p}║{y}     ╚════██║   ██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║╚════██║   ██╔══╝     ██║  ██║     {p}║
{p}║{y}     ███████║██╗██║ ╚═╝ ██║╚██████╔╝██║  ██║╚██████╔╝███████║██╗███████╗██╗██████╔╝     {p}║
{p}║{y}     ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝╚═════╝      {p}║
{p}╠════════════════════════════════════════════════════════════════════════════════════════╣
{p}║{y} The best tool for encrypt and decrypt from moros encryption ~ this tool by @saadm.prog {p}║
{p}╚════════════════════════════════════════════════════════════════════════════════════════╝
\033[0m
""")
    
def help_menu():
    print(f"""
{p}╔═══════════════════════════════════════════════════════════════════════════╗
{p}║{y}                            Saad M. - S.MOROS.E.D                          {p}║
{p}║{y}        The best tool for encrypt and decrypt from moros encryption        {p}║
{p}║{y}    GitHub: @saadmprog {r}│{y} Telegram: @saadmprog {r}│{y} TryHackMe: @saadm.prog     {p}║
{p}╠═══════════════════════════════════════════════════════════════════════════╣
{p}║{g} Commands                       {p}│ {w}Description                              {p}║
{p}╟────────────────────────────────┼──────────────────────────────────────────╢
{p}║ {g}encrypt text                   {p}│ {w}Encrypt text in terminal                 {p}║
{p}║ {g}decrypt text                   {p}│ {w}Decrypt text in terminal                 {p}║
{p}║ {g}encrypt file                   {p}│ {w}Encrypt text file                        {p}║
{p}║ {g}decrypt file                   {p}│ {w}Decrypt text file                        {p}║
{p}║ {g}whoami                         {p}│ {w}Your user name                           {p}║
{p}║ {g}help                           {p}│ {w}View all available commands              {p}║
{p}║ {g}clear                          {p}│ {w}Clear the terminal screen                {p}║
{p}║ {g}exit                           {p}│ {w}Exit the tool and stop Tor               {p}║
{p}╚═══════════════════════════════════════════════════════════════════════════╝
\033[0m""")

MORSE_CODE_DICT = {
    'a': '.-',     'b': '-...',   'c': '-.-.',
    'd': '-..',    'e': '.',      'f': '..-.',
    'g': '--.',    'h': '....',   'i': '..',
    'j': '.---',   'k': '-.-',    'l': '.-..',
    'm': '--',     'n': '-.',     'o': '---',
    'p': '.--.',   'q': '--.-',   'r': '.-.',
    's': '...',    't': '-',      'u': '..-',
    'v': '...-',   'w': '.--',    'x': '-..-',
    'y': '-.--',   'z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ': '/',        
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    '#': '--..--..--..-',
}

MORSE_CODE_DICT_REVERSED = {value: key for key, value in MORSE_CODE_DICT.items()}

def encrypt_to_morse(text):
    encrypted = []
    for char in text.lower():
        if char in MORSE_CODE_DICT:
            encrypted.append(MORSE_CODE_DICT[char])
        else:
            encrypted.append('?') 
    return ' '.join(encrypted)

def decrypt_from_morse(morse_code):
    decrypted = []
    for code in morse_code.strip().split(' '):
        if code == '/':
            decrypted.append(' ')
        elif code in MORSE_CODE_DICT_REVERSED:
            decrypted.append(MORSE_CODE_DICT_REVERSED[code])
        else:
            decrypted.append('?') 
    return ''.join(decrypted)


if __name__ == "__main__":
    tool_logo()
    user = getpass.getuser()

    while True:

        command = input(f"{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{w} Command {r}:{w} ").lower()
    
        if command == "encrypt text":
            text = input(f"{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{w} Enter Original text {r}:{w} ")
            morse = encrypt_to_morse(text)
            print(f"\n{y}[{w}✓{y}] {w}  Encrypted text:{r}", morse)
            print(f"{y}[{w}✓{y}] {w}  Done{r} ...\n")

        elif command == "decrypt text":
            text = input(f"{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{w} Enter Encrypted text {r}:{w} ")
            decrypted = decrypt_from_morse(text)
            print(f"\n{y}[{w}✓{y}] {w}  Decrypt text: {r}", decrypted)
            print(f"{y}[{w}✓{y}] {w}  Done{r} ...\n")

        elif command == "decrypt file":
        
            filepath = input(f"{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{w} Enter the path to the text file {r}:{w} ").strip()
    
            if not os.path.exists(filepath):
                print(f"\n{y}[{w}✓{y}] {w}File does not exist. Please check the path {r}!")
                exit()
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
    
            decrypted = decrypt_from_morse(content)
            with open("decrypted_output.txt", "w", encoding="utf-8") as out_file:
                out_file.write(decrypted) 
            print(f"\n{y}[{w}✓{y}] {w}File Derypted. Output saved to 'decrypt_output.txt'{r}.\n")
        elif command == "encrypt file":
        
            filepath = input(f"{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{w} Enter the path to the text file {r}:{w} ").strip()
    
            if not os.path.exists(filepath):
                print(f"\n{y}[{w}✓{y}] {w}File does not exist. Please check the path {r}!")
                exit()
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
    
            morse = encrypt_to_morse(content)
            with open("encrypted_output.txt", "w", encoding="utf-8") as out_file:
                out_file.write(morse)
            print(f"\n{y}[{w}✓{y}] {w}File Encrypted. Output saved to 'encrypt_output.txt'{r}.\n")
    
        elif command == "help":
            help_menu()
        
        elif command == "logo":
            tool_logo()
        
        elif command == "clear":
            os.system("clear||cls")
        
        elif command == "whoami":
            print(f"\n{y}[{r}jajaja{y}]{w} I know who you are, you are {p}< {w}{user} {p}>{r} !\n")
        
        elif command == "exit":
            aysure = input(f"\n{p}[{y}s.moros.e.d{r}@{w}{user}{p}]{r}: {w}Are you sure {r}({w}y{r}/{w}n{r}) {r}:{w} ") 
            print("")
            if aysure.lower() == "y":
                print(f"{y}[{w}✓{y}] {w}Done{r} ...")
                break
        else:
            print(f"\n{y}[{w}✗{y}] {w}command not found try{r}:{y} help\n")
