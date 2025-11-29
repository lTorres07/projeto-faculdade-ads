from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# -------------------
# Conexão com o Banco
# -------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pqpdesenha777",
        database="cinema"
    )

# -------------------
# ROTA 1: COMPRA
# -------------------
@app.route("/", methods=["GET", "POST"])
def compra():
    if request.method == "POST":
        filme = request.form["filme"]
        quantidade = int(request.form["quantidade"])

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO ingressos (filme, quantidade) VALUES (%s, %s)",
            (filme, quantidade)
        )

        conn.commit()
        novo_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return redirect(url_for("cliente", ingresso_id=novo_id))

    return render_template("index.html")

# -------------------
# ROTA 2: CLIENTE
# -------------------
@app.route("/cliente/<int:ingresso_id>", methods=["GET", "POST"])
def cliente(ingresso_id):
    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        cidade = request.form["cidade"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, cpf, telefone, cidade, ingresso_id) VALUES (%s, %s, %s, %s, %s)",
            (nome, cpf, telefone, cidade, ingresso_id)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("sessoes", ingresso_id=ingresso_id))

    return render_template("cadastro_cliente.html", ingresso_id=ingresso_id)

# -------------------
# ROTA 3: SESSÕES
# -------------------
@app.route("/sessoes/<int:ingresso_id>", methods=["GET", "POST"])
def sessoes(ingresso_id):
    if request.method == "POST":
        horario = request.form["horario"]
        sala = request.form["sala"]

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO sessoes (horario, sala, ingresso_id) VALUES (%s, %s, %s)",
            (horario, sala, ingresso_id)
        )

        conn.commit()
        sessao_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return redirect(url_for("pagamento", ingresso_id=ingresso_id, sessao_id=sessao_id))

    return render_template("sessoes.html", ingresso_id=ingresso_id)

# -------------------
# ROTA 4: PAGAMENTO
# -------------------
@app.route("/pagamento/<int:ingresso_id>/<int:sessao_id>", methods=["GET", "POST"])
def pagamento(ingresso_id, sessao_id):

    if request.method == "POST":
        tipo = request.form["tipo"]
        preco = 15 if tipo == "meia" else 30

        # Buscar quantidade do ingresso
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT quantidade FROM ingressos WHERE id = %s", (ingresso_id,))
        quantidade = cursor.fetchone()[0]

        valor_total = quantidade * preco

        # Inserir na tabela pagamento
        cursor.execute(
            "INSERT INTO pagamento (ingresso_id, tipo, valor_total) VALUES (%s, %s, %s)",
            (ingresso_id, tipo, valor_total)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("resumo", ingresso_id=ingresso_id, sessao_id=sessao_id))

    return render_template("pagamento.html", ingresso_id=ingresso_id, sessao_id=sessao_id)

# -------------------
# ROTA 5: RESUMO
# -------------------
@app.route("/resumo/<int:ingresso_id>/<int:sessao_id>")
def resumo(ingresso_id, sessao_id):

    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM ingressos WHERE id=%s", (ingresso_id,))
    ingresso = cursor.fetchone()

    cursor.execute("SELECT * FROM sessoes WHERE id=%s", (sessao_id,))
    sessao = cursor.fetchone()

    cursor.execute("SELECT * FROM pagamento WHERE ingresso_id=%s ORDER BY id DESC LIMIT 1", (ingresso_id,))
    pagamento_info = cursor.fetchone()  # pega o último pagamento registrado

    cursor.close()
    conn.close()

    return render_template("resumo.html", ingresso=ingresso, sessao=sessao, pagamento=pagamento_info)

# -------------------
# RUN
# -------------------
if __name__ == "__main__":
    app.run(debug=True)
