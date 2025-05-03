
#*args y **kwars
# decoradores y generadores
# funciones anidadas
# inputs
# random
# estructuras de datos, manejo de lógica LIMPIA
from random import randint

abcedario='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

opciones={'Anime':['DEATH NOTE','DRAGON BALL','POKEMON','FULL METAL ALCHEMIST','JUJUTSU KAISEN','DANDADAN',
                   'FATE', 'ATTACK ON TITAN','NARUTO','EVANGELION','INUYASHA','DIGIMON','ONE PIECE','BLEACH','FRIEREN'],
          
          'Colores':['ROJO','AZUL','VERDE','AMARILLO','NARANJA','MORADO','BLANCO','NEGRO'],
          
          'Pokemon':["BULBASAUR", "IVYSAUR", "VENUSAUR", "CHARMANDER", "CHARMELEON", "CHARIZARD","SQUIRTLE", "WARTORTLE", "BLASTOISE", "CATERPIE", "METAPOD", "BUTTERFREE","WEEDLE", "KAKUNA", "BEEDRILL", "PIDGEY", "PIDGEOTTO", "PIDGEOT","RATTATA", "RATICATE", "SPEAROW", "FEAROW", "EKANS", "ARBOK","PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORAN", "NIDORINA","NIDOQUEEN", "NIDORAN", "NIDORINO", "NIDOKING", "CLEFAIRY", "CLEFABLE","VULPIX", "NINETALES", "JIGGLYPUFF", "WIGGLYTUFF", "ZUBAT", "GOLBAT","ODDISH", "GLOOM", "VILEPLUME", "PARAS", "PARASECT", "VENONAT","VENOMOTH", "DIGLETT", "DUGTRIO", "MEOWTH", "PERSIAN", "PSYDUCK","GOLDUCK", "MANKEY", "PRIMEAPE", "GROWLITHE", "ARCANINE", "POLIWAG","POLIWHIRL", "POLIWRATH", "ABRA", "KADABRA", "ALAKAZAM", "MACHOP","MACHOKE", "MACHAMP", "BELLSPROUT", "WEEPINBELL", "VICTREEBEL", "TENTACOOL","TENTACRUEL", "GEODUDE", "GRAVELER", "GOLEM", "PONYTA", "RAPIDASH","SLOWPOKE", "SLOWBRO", "MAGNEMITE", "MAGNETON", "FARFETCH’D", "DODUO","DODRIO", "SEEL", "DEWGONG", "GRIMER", "MUK", "SHELLDER","CLOYSTER", "GASTLY", "HAUNTER", "GENGAR", "ONIX", "DROWZEE","HYPNO", "KRABBY", "KINGLER", "VOLTORB", "ELECTRODE", "EXEGGCUTE","EXEGGUTOR", "CUBONE", "MAROWAK", "HITMONLEE", "HITMONCHAN", "LICKITUNG","KOFFING", "WEEZING", "RHYHORN", "RHYDON", "CHANSEY", "TANGELA","KANGASKHAN", "HORSEA", "SEADRA", "GOLDEEN", "SEAKING", "STARYU","STARMIE", "MR. MIME", "SCYTHER", "JYNX", "ELECTABUZZ", "MAGMAR","PINSIR", "TAUROS", "MAGIKARP", "GYARADOS", "LAPRAS", "DITTO","EEVEE", "VAPOREON", "JOLTEON", "FLAREON", "PORYGON", "OMANYTE","OMASTAR", "KABUTO", "KABUTOPS", "AERODACTYL", "SNORLAX", "ARTICUNO","ZAPDOS", "MOLTRES", "DRATINI", "DRAGONAIR", "DRAGONITE", "MEWTWO","MEW"]
          }

def mostrar_palabra(palabra, letras):
    resultado = ''
    for letra in palabra:
        if letra in letras or letra == ' ':
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()


salir=False

while salir==False:
    print('='*35)
    dificultad=int(input('Elija su dificultad:\n1. Facil\t2. Medio\n3. Dificil\t4. Salir\n-'))
    
    if dificultad== 1:
        
        vidas= 4
        lista_palabras=list(opciones.get('Colores'))
        salir=True
        categoria='Colores'
        
    elif dificultad== 2:
        vidas=6
        lista_palabras=list(opciones.get('Anime'))
        salir=True
        categoria='Anime'
        
    elif dificultad== 3:
        vidas=8
        lista_palabras=list(opciones.get('Pokemon'))
        salir=True
        categoria='Pokemon'
        
    elif dificultad== 4:
        break
    
    else:
        
        print('Opcion no valida, vuelva a intentar.')
        continue
    
def elegir_palabra(lista):
    return lista[randint(1,len(lista))]

palabra_elegida=(elegir_palabra(lista_palabras))

incorrectos =[]

letras = []

def jugar(palabra,letras,incorrectos,vidas):
    while vidas != 0:
        print('='*35)
        print(f'•Categoria: {categoria}')
        print(f'•Vidas: {vidas}')
        
        print(f'•Intentos fallidos: {' '.join(incorrectos)}')
        print('='*35)
        print('\n')
        
        if letras== '':
            print('_ '*(len(palabra_elegida)))
        
        intento=input('\n-Ingrese su intento:\n-').upper()
        
        if intento not in abcedario:
            print('Ingreso un caracter no valido, vuelva a intentar.\n')
            continue
        
        elif intento in abcedario and intento in palabra_elegida: 
            letras+=intento
            
        elif intento not in palabra_elegida:
            vidas= vidas-1
            incorrectos.append(intento)
            
        elif intento in incorrectos:
            print(f'Ya intento con esa letra.')
            continue
        
        adivinar= mostrar_palabra(palabra_elegida, letras)
        print(adivinar)
    
        
    # La funcion all recorre un itetable como una lista y devuelve verdadero si
    # (en este caso) todas la letras advinadas estan en la palabra

        if all(letra in letras or letra == ' ' for letra in palabra_elegida):
                print('='*45)
                print(f'\nCorrecto. La palabra secreta era: {palabra_elegida}')
                break
            
        elif vidas==0:
            
            print('Perdio, mejor suerte para la proxima.')
            
jugar(palabra_elegida, letras, incorrectos,vidas)
