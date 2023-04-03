# Name 1: IMG_RRRRMMDD_HHmmSSXXX(_HDR).<ext> if str[3] == "_" ?
# Name 2: IMGRRRRMMDDHHmmSS.<ext>
# Name 3: RRRRMMDD_HHmmSS.<ext>
# Name 4: IMG_PixelCam_Plus_RRRRMMDD_HHmmSS
# IMG or VID


# TO-DO
# - OBSLUGA NAME3
# - Sprawdzenie czy nie ma duplikatów w SORTED
# - Sprawdzanie czy rozszyfrowane dane są poprawne (tylko cyfry)
# - Przenosic wszystkie wyjątki do osobnego folderu

import os


path = input("Set patch where your files are: ") # Example: C:\Users\Me\Desktop\Photos
if path[len(path)-1] != "\\":
    path += "\\"

try:
    # Index files
    os.chdir(path)
    files = os.listdir()
    print("Files found: ", len(files))
    # Sort files, remove excessive files
    SkippedFiles = []
    files2remove = [] # Here You can add all files and dirs you want to remove from list. If you add something that is not in folder this will bring exception!
    for file in files:
        if file.find("trash") != -1:
            files2remove.append(file)
    for file in files2remove:
        files.remove(file)

    FileCount = 0 # Renamed files counter
    for file in files:
        '''if file.find("IMG") == -1 and file.find("VID") == -1: # To make sure that correct files are renamed
            continue
        if file.find("IMG") > 3 or file.find("VID") > 3: # To make sure that correct files are renamed
            continue'''
        if len(file) <= 16:
            continue
        if file[0:18] == "IMG_PixelCam_Plus_":
            # Name 4
            Type =      file[0:4]
            Year =      file[18:22]
            Month =     file[22:24]
            Day =       file[24:26]
            Hour =      file[27:29]
            Minutes =   file[29:31]
            Seconds =   file[31:33]
            ExtPoint =  file.find(".")
            Extra =     file[33:ExtPoint]
            Extension = file[ExtPoint+1:len(file)]
        elif file[3] == "_":
            # Name 1
            Type =      file[0:3]
            Year =      file[4:8]
            Month =     file[8:10]
            Day =       file[10:12]
            Hour =      file[13:15]
            Minutes =   file[15:17]
            Seconds =   file[17:19]
            IsHDR = file.find("HDR")
            if IsHDR != -1:
                Type += "_HDR"
            ExtPoint =  file.find(".")
            Extra =     file[19:ExtPoint]
            Extension = file[ExtPoint+1:len(file)]
        elif (not (file[0:3] == "IMG" or file[0:3] == "VID")) and (file[8] == "_"):
            # Name 3
            Type =      ""
            Year =      file[0:4]
            Month =     file[4:6]
            Day =       file[6:8]
            Hour =      file[9:11]
            Minutes =   file[11:13]
            Seconds =   file[13:15]
            ExtPoint =  file.find(".")
            Extra =     file[15:ExtPoint]
            Extension = file[ExtPoint+1:len(file)]
        elif (file[0:3] == "IMG" or file[0:3] == "VID"):
            # Name 2
            Type =      file[0:3]
            Year =      file[3:7]
            Month =     file[7:9]
            Day =       file[9:11]
            Hour =      file[11:13]
            Minutes =   file[13:15]
            Seconds =   file[15:17]
            ExtPoint =  file.find(".")
            Extra =     file[17:ExtPoint]
            Extension = file[ExtPoint+1:len(file)]
        else:
            continue
        
        spc1 = "_"
        spc2 = "-"
        NewName =   Year +spc2+ Month +spc2+ Day +spc1+ Hour +spc2+ Minutes +spc2+ Seconds +spc1+ Type +"."+Extension
        try:
            os.rename(file, NewName)
            #print(NewName)
        except FileExistsError:
            continue
        print(NewName)
        FileCount += 1

    print("Renamed files: ", FileCount)
except PermissionError:
    print("Permission denied")
except FileNotFoundError:
    print("File not found")
except NotADirectoryError:
    print("Path if not a directory")
except ValueError:
    print("There is probably wrong file name in \"files2remove\" list")
