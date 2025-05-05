import random
import os
import pygame
import colorama
from colorama import *
import textwrap
import time


pygame.init()
pygame.mixer.init()
colorama.init()
os.system("cls")
print(colorama.Fore.GREEN)


pygame.mixer.music.load("Audio\Musica_ini.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
disparo_mark = pygame.mixer.Sound("Audio\PIS_MARK.mp3")
disparo_martin = pygame.mixer.Sound("Audio\PIS_MARTIN.mp3")
radio = pygame.mixer.Sound("Audio\Radio.mp3")
radio.set_volume(0.5)
bostezo = pygame.mixer.Sound("Audio\Boztezo.mp3")
bostezo.set_volume(0.5)
coche = pygame.mixer.Sound("Audio\Coche.mp3")
coche.set_volume(0.5)
gong = pygame.mixer.Sound("Audio\gong-014-69323.mp3")
gong.set_volume(0.5)
puerta = pygame.mixer.Sound("Audio\Toctoc.mp3")
puerta.set_volume(0.5)
bar = pygame.mixer.Sound("Audio\Bar.mp3")
bar.set_volume(0.5)
door = pygame.mixer.Sound("Audio\Cerrar puerta.mp3")
door.set_volume(0.5)
juicio = pygame.mixer.Sound("Audio\Juicio.mp3")
juicio.set_volume(0.5)

while True:
    
    print("""
╔════════════════════════╗
║░▀█▀░█▀█░▀█▀░█▀▀░▀█▀░█▀█║
║░░█░░█░█░░█░░█░░░░█░░█░█║
║░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀║
╚════════════════════════╝
    """)
    print("""
╔═════════════════════════════════════════════╗
║░▀█░░░░░░░▀▀█░█░█░█▀▀░█▀█░█▀▄                ║
║░░█░░░░░░░░░█░█░█░█░█░█▀█░█▀▄                ║
║░▀▀▀░▀░░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀░▀                ║
║░▀▀▄░░░░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░░█▀▀░█▀▀║
║░▄▀░░░░░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░░█▀▀░▀▀█║
║░▀▀▀░▀░░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀║
║░▀▀█░░░░░░█▀▀░█▀█░█░░░▀█▀░█▀▄                ║
║░░▀▄░░░░░░▀▀█░█▀█░█░░░░█░░█▀▄                ║
║░▀▀░░▀░░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀                ║
╚═════════════════════════════════════════════╝
""")
    selec_inicio = int(input("HOLA MUY WENAS"))
    
    if selec_inicio == 1:
        pygame.mixer.music.load("Audio\INICIO.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1) 
        os.system("cls")
        saludo1 = "TOY INVADIENDO TU PROYECTO :D\n\n"
        print("""
                                  _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      M   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      C   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      9   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                          
 """)
        for letra in saludo1:
          print(letra, end="", flush= True)
          time.sleep(0.05)
          
        comienzo1 = input("Si estás preparado para comenzar, pulsa ENTER: ")
        gong.play()
        for letra in comienzo1:
          print(letra, end="", flush= True)
          time.sleep(0.05)

        #Variables iniciales
        martin_vida = 4        
        mark_balas = 3
        martin_balas = 5
        mark_vida = 3

        os.system("cls")

        print(""" _______  _______ _________ _______  _______  _       
(  ____ \(  ____ )\__   __/(       )(  ____ \( (    /|
| (    \/| (    )|   ) (   | () () || (    \/|  \  ( |
| |      | (____)|   | |   | || || || (__    |   \ | |
| |      |     __)   | |   | |(_)| ||  __)   | (\ \) |
| |      | (\ (      | |   | |   | || (      | | \   |
| (____/\| ) \ \_____) (___| )   ( || (____/\| )  \  |
(_______/|/   \__/\_______/|/     \|(_______/|/    )_)
                                                      \n\n""")
        print(""" _______  _       
(  ____ \( (    /|
| (    \/|  \  ( |
| (__    |   \ | |
|  __)   | (\ \) |
| (      | | \   |
| (____/\| )  \  |
(_______/|/    )_)
                  \n\n """)
        print(""" _______  ______  _________ _______  ______            _______  _______  _______ 
(  ____ \(  __  \ \__   __/(       )(  ___ \ |\     /|(  ____ )(  ____ \(  ___  )
| (    \/| (  \  )   ) (   | () () || (   ) )| )   ( || (    )|| (    \/| (   ) |
| (__    | |   ) |   | |   | || || || (__/ / | |   | || (____)|| |      | |   | |
|  __)   | |   | |   | |   | |(_)| ||  __ (  | |   | ||     __)| | ____ | |   | |
| (      | |   ) |   | |   | |   | || (  \ \ | |   | || (\ (   | | \_  )| |   | |
| (____/\| (__/  )___) (___| )   ( || )___) )| (___) || ) \ \__| (___) || (___) |
(_______/(______/ \_______/|/     \||/ \___/ (_______)|/   \__/(_______)(_______)
                                                                                  \n""")

        input("Pulsa ENTER para comenzar: ")
        os.system("cls")
        radio.play()
        time.sleep(2)
        texto1= "Mark, despierta, código 212, asesinato en Bruntsfield, necesitan tu ayuda"
        for letra in texto1:
          print(letra, end="", flush= True)
          time.sleep(0.05)

        print("""

                                                                                          
                                          @@@@@@@@@@@@@@@@                                         
                                          @@@@@@@@@@@@@@@@                                         
                                          @@@@@@@@@@@@@@@@                                         
                                         @@@@@@@@@@@@@@@@@@                                         
                                         @@@@@@@@@@@@@@@@@@=                                        
                                        @@@@@@@@@@@@@@@@@@@%                                        
                                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                               
                                     *%@@@@@@@@@@@@@@@@@@@@@@@%+                                   
                                        @@@@@@@@@@@@@@@@@@@@                                        
                                        #@@@@@@@@@@@@@@@@@@:                                        
                                          @@@@@@@@@@@@@@@@:                                         
                                          *@@@@@@@@@@@@@@@                                          
                                          :@@@@@@@@@@@@@@+                                          
                                         -#+@@@@@@@@@@@@@-@                                         
                                        @@#.@@@@@@@@@@@+ @@@                                        
                                       @@@:.@@@@@@@@@@@* *@@@                                      
                                   @@@@@@@  *@@@@@@@@@@@  @@@@:@@                                  
                               -@@@+@@@@@@   .@@@@@@@#   :@@@@@-%@@@*                               
                          :@@@@@@=@@@@@@@                =@@@@@@-*@@@@@@-.                          
                        %@@@@@@@@-=*#@@@@@               %@@@@%#+.@@@@@@@@@%:                       
                     @:@@@@@@@@@@@@@@=%@@@@   @@@@@@@@   @@@%:@@@@@@@@@@@@@@@.                      
                     @@%@@@@@@@@@@@:@@@@@@@       @     .@@@@@@%.@@@@@@@@@@@@+                      
                     @@:@@@@@@@@@@=@@@@@@@@       @     %@@@@@@@%:@@@@@@@@@@%@                      
                     @@@-@@@@@@@@@@=@@@@@@@@     @@@   .@@@@@@@*=@@@@@@@@@@*@@                     
                     @@@:#@@@@@@@@@@-@@@@@@@     @@@   .@@@@@@-+@@@@@@@@@@%@@@                     
                     @@@@ @@@@@@@@@@@-@@@@@@@   -@@@.  @@@@@@.#@@@@@@@@@-@=@@@                     
                     @@@..+@@@@@@@@@@@-@@@@@@.  %@@@+ .@@@@@ %@@@@@@@@@%@.@@@@@                     
                    @@@@ .@@@@@@@@@@@@=#@@@@@@  @@@@@ =@@@@ %@@@@@@@@@@.:%@@@@@                    
                    @@@@@@ @@@@@@@@@@@@@=+@@@@ :@@@@@ @@@# @@@@@@@@@@+% :@@@@@@                    
                    @@@- :#%:%@@@@@@@@@@@*-@@@..@@@@+:@@= @@@@@@@@@+ @+.@@@-@@@                    
                   .@@@@*  -@ :@@@@@@@@%@@#.@@+ @@@@.#@. @@@@@@@@@  .@.%@.%@@@@@                    
                   :@@@@@% .@:  #@@@@@@@=@@% @@ #@@* @..@@@@@@@@=   #@  -@@@#=@@                    
                   :#######.##   .#######.### #:-##.= .########.    #= *. .*####:                   

""")               
        input()
        os.system("cls")
        bostezo.play()
        time.sleep(1.5)
        texto2 = "Mark se despierta..."  # Sonidos de bostezo
        for letra in texto2:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        coche.play()
        print(r"""
                               
    /  .       .      (<::::::>#####<::::::>)
   .      .     .  _/~~~~~~~~~~~~~~~~~~~~~~~~~\_   .       .   .   \
.(          . .  /~                             ~\ . .   .
  ( . .        .~                                 ~.      .         )
           ()\/_____                           _____\/()   .    .  ).
(         .-''      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-.  ...
.  . . .-~              __________________              ~-.  .    /
 .   ..`~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~'    . ) .
    . .| | | #### #### || | | | [] | | | || #### #### | | | .
   (   ;__\|___________|++++++++++++++++++|___________|/__;.   .
     .  (~~====___________________________________====~~~)
 ( .  .. \------____________[ POLICE ]___________-------/ ..  .     )
         .  |      ||         ~~~~~~~~       ||      |
             \_____/                          \_____/
""")
        texto3 = "Se viste a toda prisa, coge el tabaco y las llaves del coche y sale de casa"
        for letra in texto3:
          print(letra, end="", flush= True)
          time.sleep(0.05)  # Sonido de portazo
        input()
        os.system("cls")
        texto4 = "Llega a la escena del crimen"
        for letra in texto4:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto5 = "Forense - Te pondré al día con el caso"
        for letra in texto5:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto6 = " Forense - La víctima se llama Lily, de 21 años, se mudó a esta calle hace 3 semanas, ha aparecido muerta esta madrugada con signos de violencia\n\n"
        for letra in texto6:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        print("""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⢀⣠⣴⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣤⣾⣿⣿⣿⣿⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠻⠿⠿⢿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⠟⠋⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣴⣾⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠻⢿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠉⠙⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
          
          
          """)
        input()
        os.system("cls")
        texto7 = 'Mark - Parece que el asesino tuvo una mala noche...'
        for letra in texto7:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls") # Risas, sonido de mechero
        texto8 = "Forense - Sí, eso parece, hay restos de alcohol por la casa y hemos encontrado una llave que pertenece a alguna casa de esta zona del barrio"
        for letra in texto8:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        print("""\n\n                  

⣿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣷⣮⡛⣿⣿⣿
⣿⣿⣿⣿⣵⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣿⣿
⣿⣿⣿⣏⡻⣿⣿⣿⣿⣿⣿⣿⡇⢠⠀⠀⠠⣿⣝
⣿⣿⣿⣿⣿⣿⣿⣷⣬⣻⣿⣿⡇⢸⠀⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡻⡇⢸⠀⠀⠀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⠀⠀⠀⣿⣿
⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⠟⠃⠈⠀⠀⠀⠹⣿⣯⣿
⣿⣿⣿⡿⢿⣿⣿⣿⣿⡿⠁⠀⣠⠀⠀⠀⠀⠀⠈⢻⣿⣿
⣿⣿⣿⣿⣶⣝⠿⣿⣿⠁⠀⠠⡇⠀⠀⠀⠀⠀⠀⠀⣛⢿⡿⠛⠛⠛⠛⠛⠛⠓⠛⠛⠛⢳⣿⡿
⣿⣿⣿⣿⣿⣿⣷⣮⣛⠀⠀⠸⡃⠀⠀⠀⠀⠀⠀⠀⣾⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣝
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⣿⣿⣿⣿⣿⣿⡿⣫⣾⠀⠀⢰⡄⠀⠀⠀⠀⠀⠀⠀⣿⡅⠐⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏
⣿⣿⣿⣿⣿⣯⣾⣿⣿⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣽⣿⡀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿
⣿⣷⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⡀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿
⣿⣿⣿⣷⣍⡻⣿⣿⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⣀⣠⣾⡛
⣿⣿⣿⣿⣿⣿⣮⣝⢿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣷⣮⡻⢿⣿⣿⡿⣢⠀⠀⣾⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣶⣿⣿⣾⣿⠀⠀⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣻⣿⣿⣯⣝⠿⠀⠀⣿
⣿⣿⣿⣿⣿⣿⣧⣾⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣫⣿⣿⣿⣿⣿⣿⣿⠀⠀⢿
⣿⣿⣿⣿⣷⣿⣿⣿⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣷⣽
⣿⣿⣿⣯⡻⢿⣿⣿⣿⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣫⣿
⣿⣿⣿⣿⣿⣶⣝⠿⣿⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⢮⣙⢿⡟⠛⠉⠉⠀⠀⠀⠉⠉⠉⠛⢷⣬
⣿⣿⣿⣿⣿⣿⣿⣿⣮⣢⣄⣀⣁⣀⣀⣀⣀⣀⣤⣴⣿⣿⣷⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣤⣾
 """)
        input()
        os.system("cls")
        texto9 = "Forense - Hemos descartado la gran mayoría de casas y hemos acotado las opciones a 4"
        for letra in texto9:
          print(letra, end="", flush= True)
          time.sleep(0.05)


        ascii_art = textwrap.dedent("""\n
    ....           ....           ....           ....
    ||             ||             ||             ||
 /***l|\\       /***l|\\        /***l|\\        /***l|\\
/_______\\     /_______\\      /_______\\      /_______\\
|  .-.  |-----|  .-.  |----- |  .-.  |----- |  .-.  |------
|__|L|__| .--.|__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\\ //p__  `o-o'__\\  //p__`o-o'__\\  //p__`o-o'__\\  //p__`o-o'_
------------------------------------------------------------
------------------------------------------------------------
        """)

        print(ascii_art)
        input()
        os.system("cls")
        texto10 = "Mark - continúa..."
        for letra in texto10:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")

        print("{:<15} {:^15} {:>15}".format( "","SOSPECHOSOS",""))
        print("-"*50)
        print("    James: 54 años, moreno, 1.72m, casa nº3   ")
        print("    Mary: 38 años, rubia, 1.68m, casa nº4   ")
        print("    Jake: 20 años, moreno, 1.75m, casa nº5   ")
        print("    Martin: 67 años, castaño, 1.85m, casa nº6   ")
        print("-"*50)

        texto11 = "Mark - Genial, habrá que hacerles una visitilla, a ver si nos abren los ojos\n"
        for letra in texto11:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input("Pulsa ENTER para continuar: ")
        os.system("cls")
        texto12 = "Llega a la primera casa\n"
        for letra in texto12:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        print("""
              
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;
              """)
        input()
        input("Pulsa ENTER para llamar a la puerta del primer vecino: ")
        texto13 = "Llama a la puerta..."
        puerta.play()
        for letra in texto13:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto14 = "James - ¿Quién llama?"
        for letra in texto14:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto15 = "Mark - Detective Mark, es para hacerle unas preguntas"
        for letra in texto15:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto16 = "James - Buenos días detective, ¿En qué puedo ayudarle?"
        for letra in texto16:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto17 = "Mark - Hola, como ya sabe ha habido un pequeño incidente en la Nº 2, ¿Dónde estaba la anterior noche?"
        for letra in texto17:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto18 = "James - Estuve jugando al golf y después acabé en el bar del club bebiendo cerveza, tengo testigos que lo secundan"
        bar.play()
        for letra in texto18:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto19 = "Mark - Está bien, investigaremos tu coartada, no obstante, no salga de la ciudad por si volvemos a necesitar su ayuda"
        for letra in texto19:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto20 = "James  - Cómo usted mande detective"
        for letra in texto20:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto21 = "Mark - Buenos días caballero"
        door.play()
        for letra in texto21:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input()
        os.system("cls")
        texto22 = "Mark se dirije a la siguiente casa..."
        for letra in texto22:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        print("""\n\n



    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `"""   """`
     
     
     
     """)
        input()
        os.system("cls")
        texto23 = "Llamas a la segunda puerta y no abre nadie, al parecer la casa está abierta y la llave encontrada en la casa de la estudiante encaja con la cerradura\n"
        puerta.play()
        for letra in texto23:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input("Pulse ENTER para abrir la puerta: ")
        texto24 = "Parece que no hay nadie, pero, sobre la mesa de la entrada hay una nota escrita a mano"
        for letra in texto24:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        print("""
  ______________________________
 / \                             \.
|   |   From Mary to anyone      |.
 \_ |   who reads it:            |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |   ~~~~~~~~~~~~~~~~~~~~~~   |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/""")
        
        input("\nPulsa ENTER para leer nota: ")
        os.system("cls")

        texto25 = """\nSoy Mary, he estado muchos años aguantando este sentimiento\nel odio de un mundo vacío donde el único motor que mueve a la gente es el dinero\nhe perdido la empatía, la ganas de pertenecer a este engranaje,\nla vida es una carrera de fondo y yo estoy cansada de correr.\nSé quién ha asesinado a esa chica, y por qué lo hizo, ella representa la juventud y la ilusión, aquella que yo he perdido,e imagino que su asesino también\nEse día yo estaba en casa, sucedió la madrugada del viernes, escuché los gritos.\nDesde que supe lo que había pasado, pude reflejarme en aquella chica y sentí su paz no existiendo más en este mundo turbulento,\nla siguiente pista del crimen está en mi bolsillo derecho, en el puente de Forth\n"""
        for letra in texto25:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        input("Pulsa ENTER para continuar: ")
        os.system("cls")

        #Primera decisión
        texto26 = "Tienes dos opciones, elige sabiamente:\n"
        for letra in texto26:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        texto27 = "1. Ir al puente de Forth para seguir la pista de Mary\n"
        for letra in texto27:
          print(letra, end="", flush= True)
          time.sleep(0.05)
        texto28 = "2. Seguir investigando las casas\n"
        for letra in texto28:
          print(letra, end="", flush= True)
          time.sleep(0.05)


        while True: 
            seleccion = int(input("¿Qué camino quieres tomar (1, 2)?: "))
            #CAMINO 1
            if seleccion == 1:
                pygame.mixer.music.load("Audio/audio.mp3")
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
                os.system("cls")
                texto29 = "Vas al puente de Forth"
                for letra in texto29:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                print("""\n\n\n   ^^      ..                                       ..
            []                                       []
          .:[]:_          ^^                       ,:[]:.
        .: :[]: :-.                             ,-: :[]: :.
      .: : :[]: : :`._                       ,.': : :[]: : :.
    .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
_..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
_:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
!!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
            []                                       []
            []                                       []
            []                                       []
 ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
   ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
     ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -
     ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-
            ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-
                ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~""")
                input()
                texto30 = "Encuentras el cuerpo de Mary sin vida\n"
                for letra in texto30:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                input()
                texto31 = "Buscas la nota de la que hablaba Mary, y efectivamente ahi se encontraba\n"
                for letra in texto31:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                input("Pulsa ENTER para leer la nota ")
                texto32 = "\nEl asesino es un hombre mayor, de pelo castaño y gran estatura que vive en la casa nº6"
                for letra in texto32:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                input()
                os.system("cls")
                texto33 = "Mark - Joder...Se trata de Martin, el vecino de la casa nº6"
                for letra in texto33:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                input()
                os.system("cls")
                texto34 = "Te diriges a la casa de Martin y no responde nadie. Al volver a llamar, Martin dispara desde dentro"
                for letra in texto34:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)
                print("""\n\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⣀⣴⣾⣿⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣧⣤⣤⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠙⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡿⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠘⢿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣤⣟⣋⣀⣀⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠿⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ """)
                input()
                os.system("cls")
                texto35 = "¡Comienza el tiroteo!"
                for letra in texto35:
                  print(letra, end="", flush= True)
                  time.sleep(0.05)


                while mark_vida > 0 and martin_vida > 0:
                #Turno de Martin
                    
                    if martin_balas > 0:
                        print(f"\nVida de Martin:{martin_vida}, Balas de Martin {martin_balas}")
                        print("\nMartin abre fuego!")
                        disparo_martin.play()
                        if random.randint(1, 10) <= 6:  #60% de acierto
                            print("¡Martin te alcanzó")
                            input("ENTER para continuar ")
                            os.system("cls")
                            mark_vida -= 1
                        else:
                            print("¡Martin falla!")
                            disparo_martin.play()
                            input("ENTER para continuar ")
                            os.system("cls")
                        martin_balas -= 1
                    else:
                        print("Martin está sin balas y no puede disparar.")
                        input("ENTER para continuar ")
                        os.system("cls")

                    #Comporbar si Mark sigue vivo
                    if mark_vida <= 0:
                        print("\n¡Perdiste el enfrentamiento!")
                        break

                    #Turno de Mark
                    print(f"\nTu vida: {mark_vida}, Tus balas: {mark_balas}")
                    print("¿Qué quieres hacer?")
                    print("1. Disparar")
                    print("2. Llamar a los refuerzos")
                    accion = int(input("\n\nElige una acción (1 o 2): "))

                    if accion == 1:
                        if mark_balas > 0:
                            print("Disparas a Martin...")
                            disparo_mark.play()
                            if random.randint(1, 10) <= 7:  #70% de acierto
                                print("¡Acertaste! Martin pierde 2 de vida.")
                                input("ENTER para continuar ")
                                os.system("cls")
                                martin_vida -= 2
                            else:
                                print("¡Fallaste!")
                                disparo_mark.play()
                                input("ENTER para continuar ")
                                os.system("cls")
                            mark_balas -= 1
                        else:
                            print("¡No te quedan balas!")
                            input("ENTER para continuar ")
                            os.system("cls")
                    elif accion == 2:
                        print("Pides refuerzos... ¡Recibes una bala extra!")
                        input("ENTER para continuar ")
                        os.system("cls")
                        mark_balas += 1
                    else:
                        print("Acción no válida. Pierdes tu turno.")
                        input("ENTER para continuar ")
                        os.system("cls")

                    #Verificar si Martin sigue vivo
                    if martin_vida <= 0:
                        input("\n¡Has vencido! Martin ha sido neutralizado, Pulsa ENTER para continuar ")
                        os.system("cls")
                        
                        break

                # Resultado final
                if mark_vida > 0 and martin_vida <= 0:
                    pygame.mixer.music.load("Audio\FINAL BUENO.mp3")
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
                    texto36 = "Sobreviviste al enfrentamiento y resolviste el caso."
                    for letra in texto36:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input()
                    os.system("cls")
                    texto37 = "Eres transportado al hospital, donde te recuperas\n"
                    for letra in texto37:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto38 = "La policía descubre que Martin estaba obsesionado con Lily y planeó su asesinato\n"
                    for letra in texto38:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto39 = "Recibes una medalla por valentía y eres ascendido a Inspector Jefe\n"
                    for letra in texto39:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    print("""
                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢠⣾⣿⡿⣿⣿⣷⣾⣿⣿⢿⣿⣷⡄⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⠀⠀⠙⠛⠛⠋⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠉⠉⠉⠁⢀⣀⣤⣤⣤⣤⣤⣤⣀⣀⠈⠉⠉⠉⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣶⣿⣿⡿⠀⠀⣠⣴⣿⣿⣿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣶⣄⠀⠀⢿⣿⣷⣶⣦⣤⡀⠀⠀
⠀⠀⢾⣿⣿⠛⠋⠉⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⣀⣀⠀⠀⠀⠈⠛⢿⣿⣿⣦⠀⠉⠙⠛⣻⣿⡷⠀⠀
⠀⠀⠸⣿⣿⡄⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⢀⣾⣿⣿⣷⡀⠀⠀⠀⠀⠙⢿⣿⣷⡀⠀⢠⣿⣿⠇⠀⠀
⠀⣀⣴⣿⣿⠇⠀⣾⣿⡟⠀⠀⠀⠀⠀⢀⣾⣿⡟⢻⣿⣷⡀⠀⠀⠀⠀⠀⢿⣿⣷⡀⠸⣿⣿⣦⣀⠀
⣾⣿⣿⠟⠁⠀⢸⣿⣿⠀⢀⣶⣿⣿⣿⣿⣿⠟⠀⠀⠻⣿⣿⣿⣿⣿⣶⡀⠀⣿⣿⡇⠀⠈⠻⢿⣿⣷
⠻⣿⣿⣦⡀⠀⣿⣿⡇⠀⠘⣿⣿⣯⡉⠀⠀⠀⠀⠀⠀⠀⠀⢉⣽⣿⣿⠇⠀⢸⣿⣿⠀⢀⣴⣿⣿⠟
⠀⠈⣻⣿⣷⠀⢿⣿⣇⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠀⣸⣿⣿⠀⣾⣿⣿⠁⠀
⠀⣰⣿⣿⠃⠀⠸⣿⣿⡄⠀⠀⠀⢸⣿⣿⠂⠀⣀⣀⠀⠀⢿⣿⣇⠀⠀⠀⢀⣿⣿⡇⠀⠘⣿⣿⣦⠀
⠀⣿⣿⣧⣄⡀⠀⢻⣿⣷⡀⠀⠀⣿⣿⣧⣶⣿⣿⣿⣿⣶⣼⣿⣿⠀⠀⢀⣾⣿⡟⠀⢀⣠⣼⣿⣿⠀
⠀⠉⠛⠿⣿⣿⣷⠀⠻⣿⣿⣦⡀⠻⢿⣿⠿⠛⠉⠉⠛⠿⢿⡿⠟⢀⣴⣿⣿⠟⠀⣼⣿⣿⠿⠛⠉⠀
⠀⠀⠀⠀⢸⣿⣿⠇⠀⠈⠻⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⠟⠁⠀⠀⢿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣶⣶⣶⣤⡈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⣤⣶⣶⣶⣾⣿⡷⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠛⠛⣻⣿⣿⣧⠀⠀⢀⣀⣉⠉⠉⠉⠉⢉⣀⡀⠀⠀⣼⣿⣿⣿⠛⠛⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣶⣾⣿⣿⣿⣷⣄⢀⣾⣿⣿⣿⣷⣶⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⡏⠘⠛⠛⠛⠉⠈⠻⣿⣿⣿⣿⣿⠇⠉⠛⠛⠛⠋⢹⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⡏⠀⠀⠀⢀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡀⠀⠀⠀
⠀⠀⠀⣼⣿⡿⢀⣠⣴⣾⣿⣿⡆⠀⠀⠀⣾⣿⡟⢻⣿⣷⡀⠀⠀⢰⣿⣿⣷⣦⣄⡀⢿⣿⣧⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⠿⠛⠹⣿⣿⡆⠀⣸⣿⡿⠁⠈⢿⣿⣧⠀⢠⣿⣿⠏⠛⠿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠘⠿⠿⠛⠉⠀⠀⠀⠀⢹⣿⣿⣴⣿⣿⠃⠀⠀⠘⣿⣿⣦⣿⣿⠏⠀⠀⠀⠀⠉⠛⠻⠿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡏⠀⠀⠀⠀⢹⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    
                    """)
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto40 = "Fin de la historia, gracias por jugar."
                    for letra in texto40:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    print("""
╔════════════╗
║░█▀▀░▀█▀░█▀█║
║░█▀▀░░█░░█░█║
║░▀░░░▀▀▀░▀░▀║
╚════════════╝
""")
                    input("Pulsa ENTER para volver al inicio: ")
                    os.system("cls")
                        
                elif mark_vida <= 0:
                    pygame.mixer.music.load("Audio\FINAL MALO.mp3")
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
                    texto41 = "Martin ganó y escapó\n"
                    for letra in texto41:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto42 = "Te condecoraron con la medalla de valentía post-mortem\n"
                    for letra in texto42:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    print("""\n\n
              ⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢠⣾⣿⡿⣿⣿⣷⣾⣿⣿⢿⣿⣷⡄⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⠀⠀⠙⠛⠛⠋⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠉⠉⠉⠁⢀⣀⣤⣤⣤⣤⣤⣤⣀⣀⠈⠉⠉⠉⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣶⣿⣿⡿⠀⠀⣠⣴⣿⣿⣿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣶⣄⠀⠀⢿⣿⣷⣶⣦⣤⡀⠀⠀
⠀⠀⢾⣿⣿⠛⠋⠉⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⣀⣀⠀⠀⠀⠈⠛⢿⣿⣿⣦⠀⠉⠙⠛⣻⣿⡷⠀⠀
⠀⠀⠸⣿⣿⡄⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⢀⣾⣿⣿⣷⡀⠀⠀⠀⠀⠙⢿⣿⣷⡀⠀⢠⣿⣿⠇⠀⠀
⠀⣀⣴⣿⣿⠇⠀⣾⣿⡟⠀⠀⠀⠀⠀⢀⣾⣿⡟⢻⣿⣷⡀⠀⠀⠀⠀⠀⢿⣿⣷⡀⠸⣿⣿⣦⣀⠀
⣾⣿⣿⠟⠁⠀⢸⣿⣿⠀⢀⣶⣿⣿⣿⣿⣿⠟⠀⠀⠻⣿⣿⣿⣿⣿⣶⡀⠀⣿⣿⡇⠀⠈⠻⢿⣿⣷
⠻⣿⣿⣦⡀⠀⣿⣿⡇⠀⠘⣿⣿⣯⡉⠀⠀⠀⠀⠀⠀⠀⠀⢉⣽⣿⣿⠇⠀⢸⣿⣿⠀⢀⣴⣿⣿⠟
⠀⠈⣻⣿⣷⠀⢿⣿⣇⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠀⣸⣿⣿⠀⣾⣿⣿⠁⠀
⠀⣰⣿⣿⠃⠀⠸⣿⣿⡄⠀⠀⠀⢸⣿⣿⠂⠀⣀⣀⠀⠀⢿⣿⣇⠀⠀⠀⢀⣿⣿⡇⠀⠘⣿⣿⣦⠀
⠀⣿⣿⣧⣄⡀⠀⢻⣿⣷⡀⠀⠀⣿⣿⣧⣶⣿⣿⣿⣿⣶⣼⣿⣿⠀⠀⢀⣾⣿⡟⠀⢀⣠⣼⣿⣿⠀
⠀⠉⠛⠿⣿⣿⣷⠀⠻⣿⣿⣦⡀⠻⢿⣿⠿⠛⠉⠉⠛⠿⢿⡿⠟⢀⣴⣿⣿⠟⠀⣼⣿⣿⠿⠛⠉⠀
⠀⠀⠀⠀⢸⣿⣿⠇⠀⠈⠻⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⠟⠁⠀⠀⢿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣶⣶⣶⣤⡈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⣤⣶⣶⣶⣾⣿⡷⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠛⠛⣻⣿⣿⣧⠀⠀⢀⣀⣉⠉⠉⠉⠉⢉⣀⡀⠀⠀⣼⣿⣿⣿⠛⠛⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣶⣾⣿⣿⣿⣷⣄⢀⣾⣿⣿⣿⣷⣶⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⡏⠘⠛⠛⠛⠉⠈⠻⣿⣿⣿⣿⣿⠇⠉⠛⠛⠛⠋⢹⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⡏⠀⠀⠀⢀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡀⠀⠀⠀
⠀⠀⠀⣼⣿⡿⢀⣠⣴⣾⣿⣿⡆⠀⠀⠀⣾⣿⡟⢻⣿⣷⡀⠀⠀⢰⣿⣿⣷⣦⣄⡀⢿⣿⣧⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⠿⠛⠹⣿⣿⡆⠀⣸⣿⡿⠁⠈⢿⣿⣧⠀⢠⣿⣿⠏⠛⠿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠘⠿⠿⠛⠉⠀⠀⠀⠀⢹⣿⣿⣴⣿⣿⠃⠀⠀⠘⣿⣿⣦⣿⣿⠏⠀⠀⠀⠀⠉⠛⠻⠿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡏⠀⠀⠀⠀⢹⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto43 = "Tras una larga investigación, Martin fue interceptado y llevado a juicio dos meses después\n"
                    for letra in texto43:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input("ENTER para continuar ")
                    os.system("cls")
                    texto44 = "ahora está cumpliendo cadena perpetua en la Prisión Saughton de Edimburgo\n"
                    for letra in texto44:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                    input("ENTER para continuar ")
                    os.system("cls")
                    print("""

╔════════════╗
║░█▀▀░▀█▀░█▀█║
║░█▀▀░░█░░█░█║
║░▀░░░▀▀▀░▀░▀║
╚════════════╝

""")
                    input("Pulsa ENTER para finalizar la aventura y volver al Inicio ")
                    os.system("cls")
                break
            #CAMINO 02   
            elif seleccion == 2:
                texto45 = "Continúas tu investigación en las siguientes casas, pero parece que no responde nadie... curioso"
                for letra in texto45:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                input()
                os.system("cls")
                texto46 = "Mark - Tendré que continuar mi investigación en el Puente de Forth"
                for letra in texto46:
                      print(letra, end="", flush= True)
                      time.sleep(0.05)
                input()
                os.system("cls")
                input("Pulsa ENTER para ir al Puente,pero esta vez elige el primer camino (1): ")
                

            else:
                input("Pulsa un número correcto, pulsa ENTER para reintentar: ")
    
    elif selec_inicio == 2:
        os.system("cls")
        print("="*50)
        print()
        print("{:<15}{:^15}{:>15}".format ("", "CONTROLES", ""))
        print("-"*50)
        print("{:<15}{:^15}{:>15}".format (" ","ENTER"," "))
        print("-"*50)
        print("Pulsa la tecla ENTER para avanzar en el programa, excepto cuando el programa te indique otros controles")
        print("-"*50)
        print("{:<15}{:^15}{:>15}".format (" ","NÚMEROS"," "))
        print("-"*50)
        print("El programa te irá pidiendo que ingreses números en la terminal, cada número estará asignado a una decisión, elige un camino usando los números y pulsa ENTER cuando lo hayas escrito")
        print()
        print("="*50)
        input("Pulsa ENTER para volver al Menú: ")
        os.system("cls")

    elif selec_inicio == 3:
        break

    else:
        input("Selección incorrecta, pulsa ENTER para volver al menú: ")
    
input()