from datetime import datetime

# Obter a data e hora atual
agora = datetime.now()

# Formatar a data e hora
formato = agora.strftime("%d/%m/%Y %H:%M:%S")

print("Data e hora atual:", formato)
