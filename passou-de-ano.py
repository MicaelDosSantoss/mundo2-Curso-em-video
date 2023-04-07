import emoji

n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    r = emoji.emojize(":skull_and_crossbones:", language="alias")
    print(f'\033[1;31m REPROVADO! \033[m {r}')

elif media >= 5.0 and media < 7:
    r = emoji.emojize(":enraged_face:", language="alias")
    print(f'\033[1;33m RECUPERAÇÃO! \033[m {r}')

elif media >= 7.0:
    r = emoji.emojize(":star_struck:", language="alias")
    print(f'\033[1;32m APROVADO! \033[m {r}')