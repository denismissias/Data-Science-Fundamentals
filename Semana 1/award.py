def which_prize(pontos):
    """
    Retorna a mensagem do prêmio adquirido, dado um número de pontos.

    pontos: int, pontuacao.
    """
    if pontos >= 0 and pontos <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif pontos >= 51 and pontos <= 150:
        return "Oh dear, no prize this time."
    elif pontos >= 151 and pontos <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    elif pontos >= 181 and pontos <= 200:
        return "Congratulations! You have won a penguin!"
print(which_prize(164))
