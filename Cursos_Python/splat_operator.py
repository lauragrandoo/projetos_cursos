dados_pessoais = ("Olívia", 24, "Médica")

print(f"Nome: {dados_pessoais[0]}, idade: {dados_pessoais[1]}, profissão: {dados_pessoais[2]}")
print("Nome: {}, idade: {}, profissão: {}".format(*dados_pessoais))

#Outro exemplo com o splat:
a = [1,2,3] 
b = [*a, 4,5,6] 
print(b) #[1,2,3,4,5,6]