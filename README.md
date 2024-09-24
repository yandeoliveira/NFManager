**NFManager**                                                                                           
Uma interface gráfica de usuário para gerenciar produtos e gerar notas fiscais.                                                    

**Descrição**                                    
Este aplicativo permite que os usuários adicionem, removam e gerenciem produtos, além de gerar uma nota fiscal com o custo total dos produtos. A GUI é construída usando Tkinter e utiliza um banco de dados SQLite para armazenar informações de produtos.

**Recursos**                                                          
Adicione produtos com nome, preço e quantidade;                                                                                                               
Remova produtos por ID;                                                                                                                                                                
Gere uma nota fiscal com o custo total dos produto;                                                                                                       
Interface de usuário amigável com botões e campos de texto.                                                                                                                                         

**Uso**                                                                               
1- Execute o aplicativo executando o arquivo `programa_final.exe`, da pasta `build` *(baixe a pasta zipada `FInal` em seu computador para acessar a pasta).*                                                         
2- Adicione produtos preenchendo os campos de nome, preço e quantidade e clicando no botão "Adicionar produto".     
3- Remova produtos inserindo o ID do produto e clicando no botão "Excluir produto".                            
4- Gere uma nota fiscal clicando no botão "Atualizar nota fiscal".                                                          
   *A nota fiscal será exibida no campo de texto abaixo.*

**Detalhes Técnicos**                                                                                                                                                          
- O aplicativo usa Tkinter para a GUI e SQLite para o banco de dados.                                                                              
- A classe NotaFiscal gerencia a conexão do banco de dados e os dados dos produtos.                                                                                  
- A classe NotaFiscalGUI cria a GUI e manipula a entrada do usuário.                                                                                                                                 

**Licença**                                                                                 
Este aplicativo é licenciado sob a Licença MIT. Veja o arquivo LICENSE para detalhes.

**Autor**                                                                                 
*[Yan de Oliveira]*



