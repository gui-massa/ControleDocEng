
class User:

    def __init__(self, name, company, role, access_level):
        self._name = name
        self._user_number = User.new_user()
        self._company = company
        self._role = role
        self._access_level = access_level

    def __str__(self):
        return self._name + str(self._user_number)

    def new_user():
        global new_user_number
        if "new_user_number" not in globals():
            new_user_number = 0
        new_user_number += 1
        return new_user_number


class Project:

    def __init__(self, name, id_number, sigla) -> None:
        self._name = name 
        self._id_number = id_number
        self._sigla = sigla
        self._pastas = []

    def __str__(self):
        return self._sigla

class Pasta:

    def __init__(self, project, nome_pasta, sigla_pasta) -> None:
        self._nome_pasta = nome_pasta
        self._sigla_pasta = sigla_pasta
        self._project = project
        self._documentos = []
        project._pastas.append(self)

    def __str__(self):
        return self._sigla_pasta


class Documento:

    def __init__(self, Pasta): 
        self._pasta = Pasta
        self._number = str(Documento.new_document()).zfill(4)
        
        Pasta._documentos.append(self)

    def __str__(self) -> str:
        return str(self._pasta._project) + "-" + str(self._pasta) + "-" + str(self._number).zfill(4)
        # str(self._number)

    def new_document():
        global new_document_number
        if "new_document_number" not in globals():
            new_document_number = 0
        new_document_number += 1
        return new_document_number