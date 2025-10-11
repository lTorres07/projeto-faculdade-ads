from flask import Flask, redirect, request, render_template
import mysql.connector

app = Flask(__name__)

# --- Página inicial: compra de ingressos ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Rota para processar a compra ---
@app.route("/compra", methods=["POST"])
def compra():
    filme = request.form.get("filme")
    quantidade = request.form.get("quantidade")

    try:
        conect = mysql.connector.connect(
            host="localhost",
            database="cinema",
            user="root",
            password="pqpdesenha777"
        )
        cursor = conect.cursor()
        query = "INSERT INTO ingressos (filme, quantidade) VALUES (%s, %s)"
        cursor.execute(query, (filme, quantidade))
        conect.commit()
        print(f"Ingresso salvo: {filme}, {quantidade}")
    except mysql.connector.Error as err:
        print(f"Erro ao salvar ingresso: {err}")
    finally:
        cursor.close()
        conect.close()

    # Redireciona para o cadastro do cliente
    return redirect("/cadastro")

# --- Rota para cadastro de clientes ---
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        cidade = request.form.get("cidade")

        # Debug: print dos dados recebidos
        print(f"Tentando salvar cliente: {nome}, {cpf}, {telefone}, {cidade}")

        try:
            conect = mysql.connector.connect(
                host="localhost",
                database="cinema",
                user="root",
                password="pqpdesenha777"
            )
            cursor = conect.cursor()
            query = "INSERT INTO clientes (nome, cpf, telefone, cidade) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome, cpf, telefone, cidade))
            conect.commit()
            print(f"Cliente salvo com sucesso: {nome}")
        except mysql.connector.Error as err:
            print(f"Erro ao salvar cliente: {err}")
            return f"Erro ao salvar cliente: {err}"
        finally:
            cursor.close()
            conect.close()

        # Mensagem de sucesso no navegador
        return f"Cliente {nome} cadastrado com sucesso! <br><a href='/'>Voltar à compra</a>"

    return render_template("cadastro_cliente.html")

if __name__ == "__main__":
    app.run(debug=True)
