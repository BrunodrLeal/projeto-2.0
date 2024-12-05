# hello_git.py
print("Hello, Git!")

# calculator.py
def calculator():
    print("Bem-vindo à Calculadora!")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A soma de {num1} + {num2} é {num1 + num2}")

if __name__ == "__main__":
    calculator()
# random_numbers.py
import random

def generate_random_numbers():
    print("Gerando 5 números aleatórios entre 1 e 100:")
    for _ in range(5):
        print(random.randint(1, 100))

if __name__ == "__main__":
    generate_random_numbers()
# file_operations.py
def write_file():
    with open("sample.txt", "w") as file:
        file.write("Este é um arquivo de teste.\nCriado para aprender Python com Git.")

def read_file():
    with open("sample.txt", "r") as file:
        content = file.read()
        print("Conteúdo do arquivo:")
        print(content)

if __name__ == "__main__":
    write_file()
    read_file()
# file_operations.py
def write_file():
    with open("sample.txt", "w") as file:
        file.write("Este é um arquivo de teste.\nCriado para aprender Python com Git.")

def read_file():
    with open("sample.txt", "r") as file:
        content = file.read()
        print("Conteúdo do arquivo:")
        print(content)

if __name__ == "__main__":
    write_file()
    read_file()

# cpf_validator.py
def validate_cpf(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        print(f"O CPF {cpf} é válido.")
    else:
        print(f"O CPF {cpf} é inválido.")

if __name__ == "__main__":
    cpf = input("Digite um CPF (somente números): ")
    validate_cpf(cpf)
# guessing_game.py
import random

def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("Adivinhe o número secreto (entre 1 e 10):")
    while attempts > 0:
        guess = int(input("Seu palpite: "))
        if guess == secret_number:
            print("Parabéns! Você acertou!")
            break
        else:
            attempts -= 1
            print(f"Errado! Você tem {attempts} tentativas restantes.")
    if attempts == 0:
        print(f"Game Over! O número secreto era {secret_number}.")

if __name__ == "__main__":
    guessing_game()
# simple_plot.py
import matplotlib.pyplot as plt

def simple_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.plot(x, y, marker="o")
    plt.title("Gráfico Simples")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simple_plot()
