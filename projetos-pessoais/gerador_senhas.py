import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória segura."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")
    tamanho_desejado = int(input("Digite o tamanho da senha desejada (ex: 12): "))
    nova_senha = gerar_senha(tamanho_desejado)
    print(f"Sua nova senha é: {nova_senha}")
