from random import randint
from random import choice



# Defino una lista con todos los caracteres validos para comparar mas adelante
ABCEDARIO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Creo un diccionario con cada categoria y sus opciones
opciones = {'Anime': ['DEATH NOTE','DRAGON BALL','POKEMON','FULL METAL ALCHEMIST','JUJUTSU KAISEN','DANDADAN','FATE', 'ATTACK ON TITAN','NARUTO','EVANGELION','INUYASHA','DIGIMON','ONE PIECE','BLEACH','FRIEREN','BLACK CLOVER','SOUL EATER','FIRE FORCE','FAIRY TAIL','ONE PUNCH MAN','MOB PSYCHO','BLUE LOCK','DR STONE','CHAINSAW MAN','DEMON SLAYER','HAIKYUU','NORAGAMI','HUNTER X HUNTER','INITIAL D','SPY X FAMILY'],
    
            'Colores': ['ROJO','AZUL','VERDE','AMARILLO','NARANJA','MORADO','BLANCO','NEGRO'],
    
            'Pokemon': ["BULBASAUR", "IVYSAUR", "VENUSAUR", "CHARMANDER", "CHARMELEON", "CHARIZARD","SQUIRTLE", "WARTORTLE", "BLASTOISE", "CATERPIE", "METAPOD", "BUTTERFREE","WEEDLE", "KAKUNA", "BEEDRILL", "PIDGEY", "PIDGEOTTO", "PIDGEOT","RATTATA", "RATICATE", "SPEAROW", "FEAROW", "EKANS", "ARBOK","PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORAN F", "NIDORINA","NIDOQUEEN", "NIDORAN M", "NIDORINO", "NIDOKING", "CLEFAIRY", "CLEFABLE","VULPIX", "NINETALES", "JIGGLYPUFF", "WIGGLYTUFF", "ZUBAT", "GOLBAT","ODDISH", "GLOOM", "VILEPLUME", "PARAS", "PARASECT", "VENONAT","VENOMOTH", "DIGLETT", "DUGTRIO", "MEOWTH", "PERSIAN", "PSYDUCK","GOLDUCK", "MANKEY", "PRIMEAPE", "GROWLITHE", "ARCANINE", "POLIWAG","POLIWHIRL", "POLIWRATH", "ABRA", "KADABRA", "ALAKAZAM", "MACHOP","MACHOKE", "MACHAMP", "BELLSPROUT", "WEEPINBELL", "VICTREEBEL", "TENTACOOL","TENTACRUEL", "GEODUDE", "GRAVELER", "GOLEM", "PONYTA", "RAPIDASH","SLOWPOKE", "SLOWBRO", "MAGNEMITE", "MAGNETON", "FARFETCHD", "DODUO","DODRIO", "SEEL", "DEWGONG", "GRIMER", "MUK", "SHELLDER","CLOYSTER", "GASTLY", "HAUNTER", "GENGAR", "ONIX", "DROWZEE","HYPNO", "KRABBY", "KINGLER", "VOLTORB", "ELECTRODE", "EXEGGCUTE","EXEGGUTOR", "CUBONE", "MAROWAK", "HITMONLEE", "HITMONCHAN", "LICKITUNG","KOFFING", "WEEZING", "RHYHORN", "RHYDON", "CHANSEY", "TANGELA","KANGASKHAN", "HORSEA", "SEADRA", "GOLDEEN", "SEAKING", "STARYU","STARMIE", "MR MIME", "SCYTHER", "JYNX", "ELECTABUZZ", "MAGMAR","PINSIR", "TAUROS", "MAGIKARP", "GYARADOS", "LAPRAS", "DITTO","EEVEE", "VAPOREON", "JOLTEON", "FLAREON", "PORYGON", "OMANYTE","OMASTAR", "KABUTO", "KABUTOPS", "AERODACTYL", "SNORLAX", "ARTICUNO","ZAPDOS", "MOLTRES", "DRATINI", "DRAGONAIR", "DRAGONITE", "MEWTWO","MEW"],
    
            'LOL': ["AATROX", "AHRI", "AKALI", "AKSHAN", "ALISTAR", "AMUMU", "ANIVIA", "ANNIE", "APHELIOS", "ASHE", "CAITLYN", "DARIUS", "EKKO", "EZREAL", "FIORA", "GNAR", "GAREN", "JINX", "JHIN", "KAI SA", "KATARINA", "LEE SIN", "LUX", "MORGANA", "NAMI", "RAKAN", "RENGAR", "SHACO", "SION", "SORAKA", "SYLAS", "TRYNDAMERE", "UDYR", "VAYNE", "VI", "YASUO", "ZED", "ZYRA"],
            
            'Peliculas': ['TITANIC', 'AVATAR', 'INCEPTION', 'GLADIATOR', 'JOKER','EL PADRINO', 'PULP FICTION', 'INTERSTELLAR', 'FORREST GUMP', 'MATRIX','EL SEÑOR DE LOS ANILLOS', 'LOS VENGADORES', 'IRON MAN', 'BATMAN BEGINS','EL CABALLERO DE LA NOCHE', 'TOY STORY', 'COCO', 'FROZEN', 'STAR WARS','JURASSIC PARK', 'LA LA LAND', 'DUNA', 'SPIDER MAN', 'EL REY LEON'],
            
            'Videojuegos': ['MARIO', 'ZELDA', 'PACMAN', 'TETRIS', 'SONIC','METROID', 'DOOM', 'POKEMON', 'HALO', 'FIFA','MINECRAFT', 'FORTNITE', 'CALL OF DUTY', 'THE WITCHER','ANIMAL CROSSING', 'GRAND THEFT AUTO', 'RED DEAD REDEMPTION', 'STREET FIGHTER','LEAGUE OF LEGENDS', 'AMONG US', 'SKYRIM', 'OVERWATCH', 'FALLOUT']
} 
# Defino una funcion para empezar y volver a jugar, ademas de mostrar las veces que jugo y el puntaje acumulado
def inicio():
    
# Inicio las variables de puntaje y un contador para saber cuantas veces jugo el usuario en o
    puntaje = 0
    contador = 0
    
    print('=' * 45)
    print('Bienvenido al juego de advina la palabra 🎮')

    while True:
        resultado = elegir_dificultad(contador, puntaje)
        if resultado is None:
            break
        contador, puntaje = resultado

        respuesta = input('\n¿Desea jugar otra vez? (si/no):\n- ').strip().upper()
        while respuesta not in ['SI', 'NO']:
            respuesta = input('Por favor, ingrese "SI" o "NO":\n- ').strip().upper()

        if respuesta == 'NO':
            print(f'\nJugó {contador} veces.')
            print(f'Hizo {puntaje} puntos.')
            print('¡Gracias por jugar! 🎉')
            print('=' * 45)
            break
            
# Uso un decorador 

def adivinar_palabra(func):
    def wrapper(*args, **kwargs):
        print('\nPreparando palabra...')
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

# Uso un generador para mostrar ir actualizando la en pantalla segun las letras que ingrese el usuario

def mostrar_palabra(palabra, letras):
    while True:
        resultado = ''
        for letra in palabra:
            if letra in letras or letra == ' ':
                resultado += letra + ' '
            else:
                resultado += '_ '
        yield resultado.strip()
        
        
def elegir_palabra(lista):
    return lista[randint(0, len(lista)-1)]

# Le pide al usuario que elija la dificultad y dependiendo de ello define la cantidad de vidas y las posibles categorias
def elegir_dificultad(contador, puntaje):
    
    print('='*45)

    dificultad = int(input('Elija su dificultad:\n1. Facil\t2. Medio\t3. Dificil\n4. Ranked\t5. Salir\n-'))

    if dificultad == 1:
        vidas = 6
        posibles_categorias = ['Colores','Peliculas']
        
    elif dificultad == 2:
        vidas = 5
        posibles_categorias = ['Anime','Videojuegos','Peliculas']
        
    elif dificultad == 3:
        vidas = 4
        posibles_categorias = [ 'Pokemon', 'Anime','LOL']
        
    elif dificultad == 4:
        vidas = 3
        posibles_categorias = ['Colores', 'Pokemon', 'Anime','LOL','Peliculas','Videojuegos']
        
# Si decide salir, muestra las veces que jugo y su puntaje
    elif dificultad == 5:
        
        print(f'\nJugo {contador} veces')
        print(f'Hizo {puntaje} puntos')
        print('Gracias por jugar🎉\n')
        print('='*45)
        return
    else:
# Si ingresa algo que no este en las opciones se repite
        print('Opcion no valida, vuelva a intentar.')
        return elegir_dificultad(contador, puntaje)
    
#Choice toma la lista con las categorias y elige una al azar

    categoria = choice(posibles_categorias)
    lista_palabras = list(opciones.get(categoria))
    
# Tomando la lista de categorias, la funcion elegir_palabra devuelve una
    palabra_elegida = elegir_palabra(lista_palabras)

# Llama a jugar y le da todos los datos necesarios
    return jugar(palabra_elegida, vidas, categoria, contador,puntaje)

@adivinar_palabra
def jugar(palabra, vidas, categoria, contador, puntaje):

# Define una lista para los errores y otra para las letras que si son correctas
    incorrectos = []
    letras = []
    
# Llamo al generador y le doy la palabra secreta y las palabras correctas
    adivinar = mostrar_palabra(palabra, letras)
# Muestro los datos importates en pantalla y
# le pido al jugador que ponga que letra cree que esta en la palabra secreta

    while vidas != 0:
        print('=' * 45)
        print(f'• Categoría: {categoria}')
        print(' '.join('❤' * vidas))
        print(f'• Intentos fallidos: {' '.join(incorrectos)}')
        print('=' * 45)
        print(next(adivinar))

        intento = input('\n-Ingrese su intento:\n-').upper()
    
    
# Con un if, comparo si la letra que ingreso el jugador es valida,
# si ya la habia ingresado antes, si esta en la palabra o si no esta lo añade a una lista     
        if intento not in ABCEDARIO:
            print('-Por favor ingrese un caracter válido.\n')
            continue

        if intento in letras or intento in incorrectos:
            print(f'-Ya intentó con esa letra.')
            continue

        if intento in palabra:
            letras += intento
        else:
            vidas -= 1
            incorrectos.append(intento)
            
# La funcion all recorre un itetable como una lista y devuelve verdadero si
# (en este caso) todas la letras ingresadas estan en la palabra secreta

        if all(letra in letras or letra == ' ' for letra in palabra):
            print('=' * 45)
            print(f'\n🎊 Correcto, La palabra era: {palabra} 🎊\n')
            
# Suma un 1 al contador y hace el calculo del puntaje

            contador += 1
            puntaje += (len(palabra) * vidas) - (len(incorrectos))
        
            print('='*45)
            
            return contador,puntaje
        
# En caso de quedarse sin vidas, escribe un mensaje personalizado,
# suma 1 al contador y tambien hace el calculo del puntaje

        elif vidas == 0:
            print('=' * 45)
            
            if categoria == 'LOL':
                print(f'Tranquilo, es culpa del jg🌿.\nLa palabra secreta era: {palabra}.')
            else:
                print(f'Perdiste. La palabra era: {palabra}.')
                
            contador += 1    
            puntaje += (len(letras)) - (len(incorrectos))
            
            print('='*45)
            
            return contador,puntaje

inicio()