from flask import Flask, redirect, request, render_template
import mysql.connector

app = Flask(__name__)

# Rota principal - mostra o formulário
@app.route("/")
def home():
    return render_template("index.html")

# Rota para salvar a compra no banco
@app.route("/compra", methods=["POST"])
def compra():
    filme = request.form.get("filme")
    quantidade = request.form.get("quantidade")

    dados = (filme, quantidade)

    conect = None
    cursor = None

    try:
        conect = mysql.connector.connect(
            host="localhost",
            database="cinema",
            user="root",
            password="Pqpdesenha777"
        )
        cursor = conect.cursor()

        query = """
            INSERT INTO ingressos (filme, quantidade)
            VALUES (%s, %s)
        """
        cursor.execute(query, dados)
        conect.commit()

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conect is not None:
            conect.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
