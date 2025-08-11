11/08

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
len(assistiram)
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

for usuario in set(assistiram):
  print(usuario)
usuarios_data_science ^ usuarios_machine_learning

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
set(meu_texto.split())
 aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}
type(aparicoes)

