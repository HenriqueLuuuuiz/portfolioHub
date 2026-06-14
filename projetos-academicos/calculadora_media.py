def calcular_media(nota1, nota2):
    """Calcula a média semestral do aluno e verifica se foi aprovado."""
    media = (nota1 + nota2) / 2
    return media

if __name__ == "__main__":
    print("--- Calculadora de Média do CEUB ---")
    n1 = float(input("Digite a nota da N1: "))
    n2 = float(input("Digite a nota da N2: "))
    
    media_final = calcular_media(n1, n2)
    
    print(f"\nMédia Final: {media_final:.2f}")
    if media_final >= 5.0: # Supondo que a média para passar seja 5
        print("Status: APROVADO! 🎉")
    else:
        print("Status: REPROVADO. Estude mais! 📚")
