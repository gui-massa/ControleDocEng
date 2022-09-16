from xml.dom.minidom import Document
from classes import Documento, Project, User, Pasta;

# Creating users
user1 = User("Guilherme Alves", "Grupo Coders", "Back-End Developer", "Root")
user2 = User("Pedro Tonto", "Grupo Coders", "Back-End Developer", "Root")
user3 = User("Francisca Cisca", "Grupo Coders", "Back-End Developer", "Root")
user4 = User("Mauricio Ricio", "Grupo Coders", "Back-End Developer", "Root")

print(user1._name, user1._user_number)
print(user2._name, user2._user_number)
print(user3._name, user3._user_number)
print(user4._name, user4._user_number)

# Creating Project
project1 = Project("Parque eólico Araraquara", "908765", "ARA")

# Creating Folders
pasta_1_tur = Pasta(project1, "Turbina", "TUR")
pasta_1_ger = Pasta(project1, "Gerador", "GER")
pasta_1_aut = Pasta(project1, "Automação", "AUT")

print(pasta_1_tur)
print(pasta_1_ger)
print(pasta_1_aut)

print(project1._pastas)

# Creating Documents
documento_1_TUR_0001 = Documento(pasta_1_tur)
documento_1_TUR_0002 = Documento(pasta_1_tur)
documento_1_TUR_0003 = Documento(pasta_1_tur)

documento_1_GER_0001 = Documento(pasta_1_ger)
documento_1_GER_0002 = Documento(pasta_1_ger)
documento_1_GER_0003 = Documento(pasta_1_ger)

documento_1_AUT_0001 = Documento(pasta_1_aut)
documento_1_AUT_0002 = Documento(pasta_1_aut)
documento_1_AUT_0003 = Documento(pasta_1_aut)

print(pasta_1_ger._documentos[1])