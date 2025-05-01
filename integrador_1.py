
#*args y **kwars
# decoradores y generadores
# funciones anidadas
# inputs
# random
# estructuras de datos, manejo de lógica LIMPIA
from random import randint

opciones={'Anime':['DEATH NOTE','DRAGON BALL','POKEMON','FULL METAL ALCHEMIST','JUJUTSU KAISEN','DANDADAN',
                   'FATE', 'ATTACK ON TITAN','NARUTO','EVANGELION','INUYASHA','DIGIMON','ONE PIECE','BLEACH','FRIEREN'],
          
          'Colores':['ROJO','AZUL','VERDE','AMARILLO','NARANJA','MORADO','BLANCO','NEGRO'],
          
          'Pokemon':["BULBASAUR", "IVYSAUR", "VENUSAUR", "CHARMANDER", "CHARMELEON", "CHARIZARD","SQUIRTLE", "WARTORTLE", "BLASTOISE", "CATERPIE", "METAPOD", "BUTTERFREE","WEEDLE", "KAKUNA", "BEEDRILL", "PIDGEY", "PIDGEOTTO", "PIDGEOT","RATTATA", "RATICATE", "SPEAROW", "FEAROW", "EKANS", "ARBOK","PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORAN", "NIDORINA","NIDOQUEEN", "NIDORAN", "NIDORINO", "NIDOKING", "CLEFAIRY", "CLEFABLE","VULPIX", "NINETALES", "JIGGLYPUFF", "WIGGLYTUFF", "ZUBAT", "GOLBAT","ODDISH", "GLOOM", "VILEPLUME", "PARAS", "PARASECT", "VENONAT","VENOMOTH", "DIGLETT", "DUGTRIO", "MEOWTH", "PERSIAN", "PSYDUCK","GOLDUCK", "MANKEY", "PRIMEAPE", "GROWLITHE", "ARCANINE", "POLIWAG","POLIWHIRL", "POLIWRATH", "ABRA", "KADABRA", "ALAKAZAM", "MACHOP","MACHOKE", "MACHAMP", "BELLSPROUT", "WEEPINBELL", "VICTREEBEL", "TENTACOOL","TENTACRUEL", "GEODUDE", "GRAVELER", "GOLEM", "PONYTA", "RAPIDASH","SLOWPOKE", "SLOWBRO", "MAGNEMITE", "MAGNETON", "FARFETCH’D", "DODUO","DODRIO", "SEEL", "DEWGONG", "GRIMER", "MUK", "SHELLDER","CLOYSTER", "GASTLY", "HAUNTER", "GENGAR", "ONIX", "DROWZEE","HYPNO", "KRABBY", "KINGLER", "VOLTORB", "ELECTRODE", "EXEGGCUTE","EXEGGUTOR", "CUBONE", "MAROWAK", "HITMONLEE", "HITMONCHAN", "LICKITUNG","KOFFING", "WEEZING", "RHYHORN", "RHYDON", "CHANSEY", "TANGELA","KANGASKHAN", "HORSEA", "SEADRA", "GOLDEEN", "SEAKING", "STARYU","STARMIE", "MR. MIME", "SCYTHER", "JYNX", "ELECTABUZZ", "MAGMAR","PINSIR", "TAUROS", "MAGIKARP", "GYARADOS", "LAPRAS", "DITTO","EEVEE", "VAPOREON", "JOLTEON", "FLAREON", "PORYGON", "OMANYTE","OMASTAR", "KABUTO", "KABUTOPS", "AERODACTYL", "SNORLAX", "ARTICUNO","ZAPDOS", "MOLTRES", "DRATINI", "DRAGONAIR", "DRAGONITE", "MEWTWO","MEW"]
          }

dificultad=int(input('Elija su dificultad:\n1. Facil\t2. Medio\t3. Dificil\t4. Salir\n-'))

salir=False

while salir==False:
    if dificultad== 1:
        vidas= 4
        lista_palabras=list(opciones.get('Colores'))
        salir=True
    elif dificultad== 2:
        vidas=6
        lista_palabras=list(opciones.get('Anime'))
        salir=True
    elif dificultad== 3:
        vidas=8
        lista_palabras=list(opciones.get('Pokemon'))
        salir=True
    elif dificultad== 4:
        break
    else:
        continue
    
palabra_elegida=lista_palabras[randint(1,len(lista_palabras))]

print(' '.join(palabra_elegida))