# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
image elucia1 = "sylvie2_surprised.png"
image ha1 = "maxresdefault [1].jpeg"
image spa = "spaceinvaders.jpeg"
image crai = "DSC_0029 [1].jpeg"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character("Elucia", color="0000CE")
define l = Character("Lushen", color="0000CE")
define estado = Character ("", color="0000CE")
define j = Character("Jerit", color="0000CE")

# The game starts here.
# - El juego comienza aquí.
label start:
    
    scene crai
    
    play music " Bone N Skin.mp3"
    
    scene  elucia1
    
    j"hey! que crees que estas haciendo?! lushen estas son horas de trabajo."
    
    l"Ahh. Estoy jugando Space invaders."
    
    l"pi pi pi pi piru piou. XD"
        
    j"... eso no es Space invaders."
    
    l"pi pi pi pi piru piou si lo es."
    
    j"lo que estas jugando es! "
    
    scene ha1
    
    j"Eso es lo de menos, si el jefe se da cuenta te va a dar una tunda!"
      
    l"Asi que crees que "
    
    
      
      
    return
