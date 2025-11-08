from flask import Flask, redirect, request, render_template
import mysql.connector

app = Flask(__name__)

# ================= Compra de ingressos =================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compra", methods=["POST"])
def compra():
    filme = request.form.get("filme")
    quantidade = request.form.get("quantidade")

    if not filme or not quantidade:
        return "Erro: Preencha todos os campos da compra."

    dados = (filme, quantidade)

    conect = None
    cursor = None

    try:
        conect = mysql.connector.connect(
            host="localhost",
            database="cinema",
            user="root",
            password="pqpdesenha777"
        )
        cursor = conect.cursor()
        query = "INSERT INTO ingressos (filme, quantidade) VALUES (%s, %s)"
        cursor.execute(query, dados)
        conect.commit()

    except mysql.connector.Error as err:
        return f"Erro ao registrar compra: {err}"

    finally:
        if cursor:
            cursor.close()
        if conect:
            conect.close()

    return redirect("/cadastro")

# ================= Cadastro do cliente =================
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        cidade = request.form.get("cidade")

        if not nome or not telefone or not cidade:
            return "Erro: Preencha todos os campos obrigatórios."

        dados = (nome, cpf, telefone, cidade)

        conect = None
        cursor = None

        try:
            conect = mysql.connector.connect(
                host="localhost",
                database="cinema",
                user="root",
                password="pqpdesenha777"
            )
            cursor = conect.cursor()
            query = "INSERT INTO clientes (nome, cpf, telefone, cidade) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, dados)
            conect.commit()

        except mysql.connector.Error as err:
            return f"Erro ao cadastrar cliente: {err}"

        finally:
            if cursor:
                cursor.close()
            if conect:
                conect.close()

        return redirect("/sessoes")

    return render_template("cadastro_cliente.html")

# ================= Sessões =================
@app.route("/sessoes", methods=["GET", "POST"])
def sessoes():
    if request.method == "POST":
        horario = request.form.get("horario")
        sala = request.form.get("sala")

        if not horario or not sala:
            return "Erro: Preencha todos os campos da sessão."

        dados = (horario, sala)

        conect = None
        cursor = None

        try:
            conect = mysql.connector.connect(
                host="localhost",
                database="cinema",
                user="root",
                password="pqpdesenha777"
            )
            cursor = conect.cursor()
            query = "INSERT INTO sessoes (horario, sala) VALUES (%s, %s)"
            cursor.execute(query, dados)
            conect.commit()

        except mysql.connector.Error as err:
            return f"Erro ao salvar sessão: {err}"

        finally:
            if cursor:
                cursor.close()
            if conect:
                conect.close()

        return redirect("/")

    return render_template("sessoes.html")

if __name__ == "__main__":
    app.run(debug=True)
