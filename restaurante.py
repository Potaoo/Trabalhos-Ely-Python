import pymysql
from db_config import connect_db
from flask import jsonify
from flask import flash, request, Blueprint

restaurante_bp = Blueprint("restaurante", __name__)

@restaurante_bp.route("/restaurante")
def restaurante():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM restaurante")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@restaurante_bp.route("/restaurante/<id>")
def restaurantebyid(id):
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("""SELECT *
                          FROM restaurante
                          WHERE idrestaurante=%s""", (id))
        rows = cursor.fetchall()
        resp = jsonify(rows[0])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@restaurante_bp.route("/restaurante", methods=["POST"])
def restaurantenovo():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        restaurante = request.json
        nome = restaurante["nome"]
        telefone = restaurante["telefone"]
        endereco = restaurante["endereco"]
        tipo_cozinha = restaurante["tipo_cozinha"]
        avaliacao = restaurante["avaliacao"]

        cursor.execute("""INSERT INTO restaurante (nome, telefone, endereco, tipo_cozinha, avaliacao)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (nome, telefone, endereco, tipo_cozinha, avaliacao))
        conn.commit()
        resp = jsonify({"message": "inserido"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@restaurante_bp.route("/restaurante", methods=["PUT"])
def update_restaurante():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        restaurante = request.json
        idrestaurante = restaurante["idrestaurante"]
        nome = restaurante["nome"]
        telefone = restaurante["telefone"]
        endereco = restaurante["endereco"]
        tipo_cozinha = restaurante["tipo_cozinha"]
        avaliacao = restaurante["avaliacao"]

        cursor.execute("""UPDATE restaurante
                          SET nome= %s, telefone= %s, endereco= %s, tipo_cozinha= %s, avaliacao= %s
                          WHERE idrestaurante= %s""",
                       (nome, telefone, endereco, tipo_cozinha, avaliacao, idrestaurante))
        conn.commit()
        resp = jsonify({"message": "alterado"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@restaurante_bp.route("/restaurante/<id>", methods=["DELETE"])
def delete_restaurante(id):
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("""DELETE FROM restaurante
                          WHERE idrestaurante= %s""",
                       (id))
        conn.commit()
        resp = jsonify({"message": "excluido"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
