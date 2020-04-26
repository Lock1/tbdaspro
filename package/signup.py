############################## Informasi Modul ##############################
## Modul signup
# Desainer
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Coder
# Kevin Domenico Tantiyo / 16519205 / 18 April 2020

# Tester
# Finna Alivia Nabila / 16519125 / 26 April 2020

######### Kamus #########
### Argumen yang direquest oleh fungsi
# user      : 2D Matrix of string
# N         : Integer

### Kamus Internal
# playerName        : String
# playerBornDay     : String
# playerHeight      : String
# playerUsername    : String
# playerPassword    : Strings
# playerRole        : Strings
# playerSaldo       : Strings
# playerGold        : Strings
# newPlayer         : Array of strings

### Kamus informasi yang direturn
# user      : 2D Matrix of string

###### Spesifikasi ######
# isUsernameValid   : (2D Matrix of strings, String, Integer) -> (Boolean)
# signUpUser        : (2D Matrix of strings, Integer) -> (2D Matrix of strings)
#############################################################################

############################### Algoritma ################################
from package.base import *

## Fungsi isUsernameValid
# Digunakan untuk mengecek apakah username sudah ada didatabase
# Jika sudah ada, return False
def isUsernameValid(user,username,N):
    isValid = True
    isValid = isExistOnDatabase(user,3,username,N,isValid)
    return isValid

def signUpUser(user,N=Nmax):
    # Penulisan interface dan input data
    print()
    playerName = input("Masukkan nama pemain: ")                                   # Nama
    playerBornDay = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")          # Tanggal Lahir
    playerHeight = input("Masukkan tinggi badan pemain (cm): ")                    # Tinggi
    playerUsername = input("Masukkan username pemain: ")                           # Username

    # Pengecekan username
    while not isUsernameValid(user,playerUsername,N):
        playerUsername = input("Username sudah digunakan, masukan username lain: ")

    # Penulisan interface lanjutan
    playerPassword = input("Masukkan password pemain: ")                           # Password

    # Setting informasi default untuk pemain baru
    playerPassword = hash(playerUsername,playerPassword)
    playerRole = "Pemain"                                       # Role
    playerSaldo = "0"                                           # Saldo
    playerGold = "0"                                            # Status Gold

    # Penulisan informasi baru
    newPlayer = [playerName, playerBornDay, playerHeight, playerUsername, playerPassword, playerRole, playerSaldo, playerGold]
    user = appendDatabase(user,newPlayer,N)
    print()
    print("Selamat menjadi pemain, {}. Selamat bermain.".format(playerName))

    print()
    return user

########################### End of function ##############################
