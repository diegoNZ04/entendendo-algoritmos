votaram = {}

def verifica_eleitor(nome):
	if votaram.get(nome):
		print("Mande embora!")
	else:
		votaram[nome] = True
		print("Deixe Votar!")
  
verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")