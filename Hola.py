
meme_dict = {
            "CHE": "Es como decir amigo pero en Argentina",
           "CHAMUYO": "Alguien que intenta impresionar, convencer o seducir",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("PALABRA NO RECONOCIDA")
