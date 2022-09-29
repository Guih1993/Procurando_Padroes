#Strings e Padrões
gene1 = 'ATCTACGTGCTGGTAATGAAACTCCACGCACCCAAAGACACG'
gene2 = 'CTCGATATTGCAATTCGTGCTCTCCAACCTCAAA'
gene3 = 'AGAGAAACGTGATACCCAAGATGTAACTCGAC'
gene4 = 'ACCCGTTATGCAACTCTTTCACGTACACAGAGGGGAA'

padrao = 'TACGTCT'

#Funcão para definir a janela de procura
genes = [gene1, gene2, gene3, gene4]

def conta_diferencas(janela,padrao):
  diferencas = 0
  for base1,base2 in zip(janela, padrao):
    if base1 != base2:
      diferencas += 1

  return diferencas

#Função para realizar a busca do padrão na string
def procura_padrao(genes, padrao, d):
  tamanho_padrao = len(padrao)
  gene_id = 0

  for gene in genes:
    gene_id += 1
    tamanho_gene = len(gene)

    for pos in range(tamanho_gene - tamanho_padrao + 1):
      janela = gene[pos:pos+tamanho_padrao]
      diferencas = conta_diferencas (janela, padrao)
      if diferencas <= d:
        print(f"Gene {gene_id} -> {janela}")
        print(f"Padrão -> {padrao}")
        print(f"Diferenças -> {diferencas}")
        print(f"Localização no gene: {pos}-{pos+tamanho_padrao}\n")

#Imprimindo função
procura_padrao(genes, padrao, 3)