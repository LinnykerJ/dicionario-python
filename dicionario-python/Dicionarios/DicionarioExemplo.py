usuarios = { }
print (usuarios)

usuarios = {
    "joao" : ["João Linnyker", "12/01/2022", "Recep_01"],
    "guilherme" : ["Guilherme Carvalho", "10/01/2022", "Raiox_03"]
}
print (usuarios)

usuarios["rayane"] = ["Rayane Guimaraes", "09/01/2022", "Raiox_01"]
print (usuarios)

print("####----####")
print(usuarios.get("joao"))