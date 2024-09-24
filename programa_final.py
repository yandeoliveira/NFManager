import tkinter as tk
import sqlite3


class NotaFiscal:
    def __init__(self):
        self.conn = sqlite3.connect('produtos.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_produto(self, nome, preco, quantidade):
        self.cursor.execute(
            'SELECT nome FROM produtos WHERE nome = ?', (nome,))
        if self.cursor.fetchone():
            raise ValueError(f"Produto '{nome}' já existe!")
        self.cursor.execute(
            'INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', (
                nome, preco, quantidade)
        )
        self.conn.commit()

    # ...

    def imprimir_nota_fiscal(self):
        self.cursor.execute('SELECT id, nome, preco, quantidade FROM produtos')
        produtos = self.cursor.fetchall()
        output = "ID\tNome do Produto:\t\t\tPreço:\tQuantidade:\n"
        total = 0
        for produto in produtos:
            if produto[3] is not None:
                output += f"{produto[0]}\t{produto[1]}\t\t\t{produto[2]:.2f}\t{produto[3]}\n"
                total += produto[2] * produto[3]
            else:
                output += f"{produto[0]}\t{produto[1]}\t\t\t{produto[2]:.2f}\t0\n"
        output += f"\nTOTAL: ......................................................\t\t\t{
            total:.2f}"
        return output

    def excluir_produto(self, produto_id):
        self.cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


class NotaFiscalGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nota Fiscal")
        self.geometry("530x580")
        self.configure(background="#6495ED")  # Adiciona um fundo branco
        self.create_widgets()
        self.nota_fiscal = NotaFiscal()

    def create_widgets(self):
        # Criar frame para adicionar produtos
        self.frame_adicionar = tk.Frame(
            self, bg="#f0f0f0", highlightbackground="#ccc", highlightthickness=1, borderwidth=2, relief="ridge")
        self.frame_adicionar.grid(column=0, row=0, padx=10, pady=10)

        self.label_nome = tk.Label(
            self.frame_adicionar, text="Nome do produto:", font=("Helvetica", 12), fg="#333")
        self.label_nome.grid(column=0, row=0, padx=5, pady=5)

        self.entry_nome = tk.Entry(self.frame_adicionar, width=30, font=(
            "Helvetica", 12), highlightthickness=1)
        self.entry_nome.grid(column=1, row=0, padx=5, pady=5)

        self.label_preco = tk.Label(
            self.frame_adicionar, text="Preço do produto:", font=("Helvetica", 12), fg="#333")
        self.label_preco.grid(column=0, row=1, padx=5, pady=5)

        self.entry_preco = tk.Entry(self.frame_adicionar, width=10, font=(
            "Helvetica", 12), highlightthickness=1)
        self.entry_preco.grid(column=1, row=1, padx=5, pady=5)

        # Adicionando quantidade dos produtos
        self.label_quantidade = tk.Label(
            self.frame_adicionar, text="Quantidade do produto:", font=("Helvetica", 12), fg="#333")
        self.label_quantidade.grid(column=0, row=2, padx=5, pady=5)

        self.entry_quantidade = tk.Entry(self.frame_adicionar, width=10, font=(
            "Helvetica", 12), highlightthickness=1)
        self.entry_quantidade.grid(column=1, row=2, padx=5, pady=5)

        self.button_adicionar = tk.Button(self.frame_adicionar, text="Adicionar produto", command=self.adicionar_produto,
                                          bg="#66CDAA", fg="white", font=("Helvetica", 12), highlightthickness=1)
        self.button_adicionar.grid(column=1, row=3, padx=5, pady=5)

        # Criar frame para imprimir nota fiscal
        self.frame_imprimir = tk.Frame(
            self, bg="#f0f0f0", highlightbackground="#ccc", highlightthickness=1)
        self.frame_imprimir.grid(column=0, row=1, padx=10, pady=10)

        self.button_imprimir = tk.Button(self.frame_imprimir, text="Atualizar nota fiscal", command=self.imprimir_nota_fiscal,
                                         bg="#2196F3", fg="white", font=("Helvetica", 12), highlightthickness=1)
        self.button_imprimir.grid(column=0, row=0, padx=5, pady=5)

        self.text_nota_fiscal = tk.Text(
            self.frame_imprimir, width=55, height=10, font=("Helvetica", 12))
        self.text_nota_fiscal.grid(column=0, row=1, padx=5, pady=5)

        # Criar frame para excluir produtos
        self.frame_excluir = tk.Frame(
            self, bg="#f0f0f0", highlightbackground="#ccc", highlightthickness=1)
        self.frame_excluir.grid(column=0, row=2, padx=10, pady=10)

        self.label_id = tk.Label(
            self.frame_excluir, text="ID do produto:", font=("Helvetica", 12), fg="#333")
        self.label_id.grid(column=0, row=0, padx=5, pady=5)

        self.entry_id = tk.Entry(self.frame_excluir, width=10, font=(
            "Helvetica", 12), highlightthickness=1)
        self.entry_id.grid(column=1, row=0, padx=5, pady=5)

        self.button_excluir = tk.Button(self.frame_excluir, text="Excluir produto", command=self.excluir_produto,
                                        bg="#FF0000", fg="white", font=("Helvetica", 12), highlightthickness=1)
        self.button_excluir.grid(column=1, row=1, padx=5, pady=5)

        # Criar frame para sair
        self.frame_sair = tk.Frame(
            self, bg="#f0f0f0", highlightbackground="#ccc", highlightthickness=1)
        self.frame_sair.grid(column=0, row=3, padx=10, pady=10)

        self.button_sair = tk.Button(self.frame_sair, text="Sair", command=self.destroy,
                                     bg="#FF9800", fg="white", font=("Helvetica", 12), highlightthickness=1)
        self.button_sair.grid(column=0, row=0, padx=5, pady=5)

        self.entry_nome.bind("<Return>", self.adicionar_produto_por_tecla)

        self.entry_preco.bind("<Return>", self.adicionar_produto_por_tecla)

    def adicionar_produto_por_tecla(self, _):
        self.adicionar_produto()

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        quantidade = int(self.entry_quantidade.get())
        self.nota_fiscal.adicionar_produto(nome, preco, quantidade)
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.atualizar_nota_fiscal()

    def atualizar_nota_fiscal(self):
        self.text_nota_fiscal.delete(1.0, tk.END)  # Limpa o Text widget
        table = self.nota_fiscal.imprimir_nota_fiscal()  # Obtem a tabela
        # Insere a tabela no Text widget
        self.text_nota_fiscal.insert(1.0, str(table))

    def excluir_produto(self):
        produto_id = int(self.entry_id.get())
        self.nota_fiscal.excluir_produto(produto_id)
        self.entry_id.delete(0, tk.END)
        self.atualizar_nota_fiscal()

    def imprimir_nota_fiscal(self):
        self.nota_fiscal.imprimir_nota_fiscal()  # Imprime no terminal
        table = self.nota_fiscal.imprimir_nota_fiscal()  # Obtem a tabela
        self.text_nota_fiscal.delete(1.0, tk.END)  # Limpa o Text widget
        # Insere a tabela no Text widget
        self.text_nota_fiscal.insert(1.0, str(table))


if __name__ == "__main__":
    gui = NotaFiscalGUI()
    gui.mainloop()
