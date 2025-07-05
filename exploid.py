import time
import random


def hellotextsoft():
    print("███████ ██   ██ ██████  ██       ██████  ██ ██████  ")
    print("██       ██ ██  ██   ██ ██      ██    ██ ██ ██   ██ ")
    print("█████     ███   ██████  ██      ██    ██ ██ ██   ██ ")
    print("██       ██ ██  ██      ██      ██    ██ ██ ██   ██ ")
    print("███████ ██   ██ ██      ███████  ██████  ██ ██████ ")
    print("     by los1st https://github.com/los1st/   ")
    print("")
    time.sleep(1)
    print("")

def softhelp():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃    snos      ┃    ddos    ┃       hack      ┃numberinfo/ni ┃")
    print("┃-acc/-account ┃-ip         ┃-tg              ┃siteinfo/si   ┃")
    print("┃-bot          ┃-p -ip      ┃-vk              ┃nickinfo/ni   ┃")
    print("┃-ch/-channel  ┃            ┃-disc/-discord   ┃ip            ┃")
    print("┃              ┃portscan/ps ┃-inst/-instagram ┃whois         ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

softhelp()

def comm_snosacc():
    print("╭─                                                     ─╮")
    print(" supported: telegram(tg), instagram(inst), vkontakte(vk) ")
    print("╰─                                                     ─╯")
    snacc = input("Social-network of account: ")
    if snacc == "tg":
        usname = input("Telegram user(@example): ")
        if usname.startswith("@"):
            time.sleep(0.8)
            dec = input("You sure?(1, 0): ")
            if dec == "1":
                sn = random.randint(15, 35)
                time.sleep(4)
                print(f"{sn} reports send in {usname}")
            elif dec == "0":
                print("! canceled")
                print(f"luck to {usname}")
            else:
                print("! error")
        else:
            print("! Invalid user")
    elif snacc == "vk":
        print("vk")
    elif snacc == "inst":
        print("inst")
    else:
        print(f"! {snacc} not supported")

comm_snosacc()
input()

soft_comms = {
    "snos -acc": comm_snosacc,
    "snos -account": comm_snosacc,
    "snos -bot": comm_snosbot,
    "snos -ch": comm_snoschannel,
    "snos -channel": comm_snoschannel,
    "ddos -ip": comm_ddos,
    "ddos -p -ip": comm_ddos_prem,
    "hack -tg": comm_htg,
    "hack -vk": comm_hvk,
    "hack -disc": comm_hdisc,
    "hack -discord": comm_hdisc,
    "hack -inst": comm_hinst,
    "hack -instagram": comm_hinst,
    "whois": comm_whois,
    "portscan": comm_portscan,
    "ps": comm_portscan,
}
