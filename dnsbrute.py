import dns.resolver

res = dns.resolver.Resolver()
#set wordlist
arquivo = open ("", "r")
subdominios = arquivo.read().splitlines()

#set target
alvo = ""

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + alvo
		resultado = res.resolve(sub_alvo, "A")
		for ip in resultado:
			print (sub_alvo, "->", ip)
	except:
		pass
