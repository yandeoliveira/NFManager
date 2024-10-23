# NFManager
Uma interface gráfica de usuário para gerenciar produtos e gerar notas fiscais.

## Descrição

Este aplicativo permite que os usuários adicionem, removam e gerenciem produtos, além de gerar uma nota fiscal com o custo total dos produtos. A GUI é construída usando Tkinter e utiliza um banco de dados SQLite para armazenar informações de produtos

## Funcionalidades

- **Adicionar Produtos**: Permite ao usuário adicionar produtos com nome, preço e quantidade.
- **Excluir Produtos**: Permite ao usuário excluir produtos da lista usando o ID do produto.
- **Imprimir Nota Fiscal**: Gera e exibe uma nota fiscal com a lista de produtos cadastrados e o total.

## Estrutura do Código

O código é dividido em duas classes principais:
```  
    NotaFiscal
```  
   Responsável pela lógica de negócios, incluindo a conexão com o banco de dados SQLite e operações de CRUD (Criar, Ler, Atualizar, Excluir) para os produtos.

```
   NotaFiscalGUI
```  
 Responsável pela interface gráfica do usuário, permitindo interação através de botões e campos de entrada.

## Requisitos

- Python 3.x
- Bibliotecas: `tkinter`, `sqlite3`

# Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

# Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.                                                                                                                                    

# Uso                                                                               
1- Execute o aplicativo executando o arquivo `programa_final.exe`, da pasta `build` *(baixe a pasta zipada `FInal` em seu computador para acessar a pasta).*                                                         
2- Adicione produtos preenchendo os campos de nome, preço e quantidade e clicando no botão "Adicionar produto".     
3- Remova produtos inserindo o `ID` do produto e clicando no botão "Excluir produto".                            
4- Gere uma nota fiscal clicando no botão "Atualizar nota fiscal".                                                          
      *A nota fiscal será exibida no campo de texto abaixo.*

#  Detalhes Técnicos                                                                                                                                                       
- O aplicativo usa `Tkinter` para a `GUI` e `SQLite` para o banco de dados.                                                                              
- A classe `NotaFiscal` gerencia a conexão do banco de dados e os dados dos produtos.                                                                                  
- A classe `NotaFiscalGUI` cria a `GUI` e manipula a entrada do usuário.                                                                                                                                 


(Arquivos de código e aplicativo em outra branch do repositório)
