from random import randint
from random import choice
puntaje=0
contador = 0
abcedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

opciones = {'Anime': ['DEATH NOTE','DRAGON BALL','POKEMON','FULL METAL ALCHEMIST','JUJUTSU KAISEN','DANDADAN','FATE', 'ATTACK ON TITAN','NARUTO','EVANGELION','INUYASHA','DIGIMON','ONE PIECE','BLEACH','FRIEREN','BLACK CLOVER','SOUL EATER','FIRE FORCE','FAIRY TAIL','ONE PUNCH MAN','MOB PSYCHO','BLUE LOCK','DR STONE','CHAINSAW MAN','DEMON SLAYER','HAIKYUU','NORAGAMI','HUNTER X HUNTER','INITIAL D','SPY X FAMILY'],
    
            'Colores': ['ROJO','AZUL','VERDE','AMARILLO','NARANJA','MORADO','BLANCO','NEGRO'],
    
            'Pokemon': ["BULBASAUR", "IVYSAUR", "VENUSAUR", "CHARMANDER", "CHARMELEON", "CHARIZARD","SQUIRTLE", "WARTORTLE", "BLASTOISE", "CATERPIE", "METAPOD", "BUTTERFREE","WEEDLE", "KAKUNA", "BEEDRILL", "PIDGEY", "PIDGEOTTO", "PIDGEOT","RATTATA", "RATICATE", "SPEAROW", "FEAROW", "EKANS", "ARBOK","PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORAN", "NIDORINA","NIDOQUEEN", "NIDORAN", "NIDORINO", "NIDOKING", "CLEFAIRY", "CLEFABLE","VULPIX", "NINETALES", "JIGGLYPUFF", "WIGGLYTUFF", "ZUBAT", "GOLBAT","ODDISH", "GLOOM", "VILEPLUME", "PARAS", "PARASECT", "VENONAT","VENOMOTH", "DIGLETT", "DUGTRIO", "MEOWTH", "PERSIAN", "PSYDUCK","GOLDUCK", "MANKEY", "PRIMEAPE", "GROWLITHE", "ARCANINE", "POLIWAG","POLIWHIRL", "POLIWRATH", "ABRA", "KADABRA", "ALAKAZAM", "MACHOP","MACHOKE", "MACHAMP", "BELLSPROUT", "WEEPINBELL", "VICTREEBEL", "TENTACOOL","TENTACRUEL", "GEODUDE", "GRAVELER", "GOLEM", "PONYTA", "RAPIDASH","SLOWPOKE", "SLOWBRO", "MAGNEMITE", "MAGNETON", "FARFETCH’D", "DODUO","DODRIO", "SEEL", "DEWGONG", "GRIMER", "MUK", "SHELLDER","CLOYSTER", "GASTLY", "HAUNTER", "GENGAR", "ONIX", "DROWZEE","HYPNO", "KRABBY", "KINGLER", "VOLTORB", "ELECTRODE", "EXEGGCUTE","EXEGGUTOR", "CUBONE", "MAROWAK", "HITMONLEE", "HITMONCHAN", "LICKITUNG","KOFFING", "WEEZING", "RHYHORN", "RHYDON", "CHANSEY", "TANGELA","KANGASKHAN", "HORSEA", "SEADRA", "GOLDEEN", "SEAKING", "STARYU","STARMIE", "MR. MIME", "SCYTHER", "JYNX", "ELECTABUZZ", "MAGMAR","PINSIR", "TAUROS", "MAGIKARP", "GYARADOS", "LAPRAS", "DITTO","EEVEE", "VAPOREON", "JOLTEON", "FLAREON", "PORYGON", "OMANYTE","OMASTAR", "KABUTO", "KABUTOPS", "AERODACTYL", "SNORLAX", "ARTICUNO","ZAPDOS", "MOLTRES", "DRATINI", "DRAGONAIR", "DRAGONITE", "MEWTWO","MEW"],
    
            'LOL': ["AATROX", "AHRI", "AKALI", "AKSHAN", "ALISTAR", "AMUMU", "ANIVIA", "ANNIE", "APHELIOS", "ASHE", "CAITLYN", "DARIUS", "EKKO", "EZREAL", "FIORA", "GNAR", "GAREN", "JINX", "JHIN", "KAI SA", "KATARINA", "LEE SIN", "LUX", "MORGANA", "NAMI", "RAKAN", "RENGAR", "SHACO", "SION", "SORAKA", "SYLAS", "TRYNDAMERE", "UDYR", "VAYNE", "VI", "YASUO", "ZED", "ZYRA"],
            
            'Peliculas': ['TITANIC', 'AVATAR', 'INCEPTION', 'GLADIATOR', 'JOKER','EL PADRINO', 'PULP FICTION', 'INTERSTELLAR', 'FORREST GUMP', 'MATRIX','EL SEÑOR DE LOS ANILLOS', 'LOS VENGADORES', 'IRON MAN', 'BATMAN BEGINS','EL CABALLERO DE LA NOCHE', 'TOY STORY', 'COCO', 'FROZEN', 'STAR WARS','JURASSIC PARK', 'LA LA LAND', 'DUNA', 'SPIDER-MAN', 'EL REY LEON'],
            
            'Videojuegos': ['MARIO', 'ZELDA', 'PACMAN', 'TETRIS', 'SONIC','METROID', 'DOOM', 'POKEMON', 'HALO', 'FIFA','MINECRAFT', 'FORTNITE', 'CALL OF DUTY', 'THE WITCHER','ANIMAL CROSSING', 'GRAND THEFT AUTO', 'RED DEAD REDEMPTION', 'STREET FIGHTER','LEAGUE OF LEGENDS', 'AMONG US', 'SKYRIM', 'OVERWATCH', 'FALLOUT']

} 


def inicio(contador,puntaje):
    print('=' * 45)
    if contador == 0:
        print('Bienvenido al juego de advina la palabra 🎮')
        elegir_dificultad(contador, puntaje)
    else:
        respuesta = input('\nDesea jugar otra vez? (si/no)\n').upper()
        if respuesta == 'SI':
            elegir_dificultad(contador, puntaje)
        elif respuesta == 'NO':
            print(f'\nJugo {contador} veces.')
            print(f'Hizo {puntaje} puntos')
            print('Gracias por jugar🎉\n')
        else:
            print('Solo ingrese "SI" o "NO".')
            inicio(contador,puntaje)
            
#agrego un decorador

def adivinar_palabra(func):
    def wrapper(*args, **kwargs):
        print('\nPreparando palabra...')
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper

#Convierto la funcion mostrar palabra en un generador

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

def elegir_dificultad(contador, puntaje):
    print('='*45)

    incorrectos = []
    letras = []

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
    elif dificultad == 5:
        print(f'\nJugo {contador} veces.')
        print(f'Hizo {puntaje} puntos')
        print('Gracias por jugar🎉\n')
        return
    else:
        print('Opcion no valida, vuelva a intentar.')
        elegir_dificultad()
        return
    
#Choice toma la lista con las categotias y elige una random

    categoria = choice(posibles_categorias)
    lista_palabras = list(opciones.get(categoria))
    palabra_elegida = elegir_palabra(lista_palabras)

    jugar(palabra_elegida, letras, incorrectos, vidas, categoria, contador,puntaje)

@adivinar_palabra
def jugar(palabra, letras, incorrectos, vidas, categoria, contador, puntaje):
    adivinar = mostrar_palabra(palabra, letras)

    while vidas != 0:
        print('=' * 45)
        print(f'• Categoría: {categoria}')
        print(' '.join('❤' * vidas))
        print(f'• Intentos fallidos: {' '.join(incorrectos)}')
        print('=' * 45)

        print(next(adivinar))

        intento = input('\n-Ingrese su intento:\n-').upper()

        if intento not in abcedario:
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
            contador += 1
            puntaje = puntaje + (len(letras)*vidas) - (len(incorrectos)) * contador
            
            print(puntaje)
            inicio(contador,puntaje)
            break

        elif vidas == 0:
            print('=' * 45)
            if categoria == 'LOL':
                print(f'Tranquilo, es culpa del jg🌿.\nLa palabra secreta era: {palabra}.')
            else:
                print(f'Perdiste. La palabra era: {palabra}.')
            contador += 1    
            puntaje = puntaje + (len(letras)) - (len(incorrectos)) * contador
            print(puntaje)
            inicio(contador,puntaje)

inicio(contador, puntaje)