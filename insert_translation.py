#!/usr/bin/env python3
#author     @Parnstermia
#Project
#brief  Simple script to insert new translation into our dictionary
#
fi = input("Enter the dictionary to modify  :\n------>")
fo = input("Enter the output dictionary     :\n------>")
with open(fi, 'r+') as fi:
    with open(fo, 'r+') as fo:
        continuar = True
        for line in fi:
            if "\t" not in line :
                if continuar:
                    translation = input("Insert translation for <" +
                                        line.strip("\n") + "> : ")
                if translation == '0':
                    continuar = False
                    print("Translation stopped, wait until file is written.")

                else:
                    if not translation == "":
                        line = line.strip("\n") + "\t" + translation + "\n"

                fo.write(line)

            else:
                fo.write(line)
    print(fo + " has been succesfully created.")
