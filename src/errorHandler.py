testsNumber = int(input('Informe quantas avaliações o aluno realizou: '))
studentGrades = []


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


for x in range(testsNumber):
    try:
        grade = float(input('Digite a nota do aluno: '))
        if grade < 0 or grade > 10:
            raise InputError(
                'Nota não pode ser negativa nem maior que 10.')
        studentGrades.append(grade)
    except InputError as ex:
        print(ex)

print(studentGrades)
media = sum(studentGrades)/testsNumber
print('A média do aluno é de {} pontos'.format(media))
