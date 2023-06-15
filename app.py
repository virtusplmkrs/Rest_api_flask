from flask import Flask, jsonify, request
import json


app = Flask(__name__)

"""LISTA COM DICIONARIOS"""
desenvolvedores = [
    {'id':0, 'nome':'Alex', 'habilidades':['Python','Flask','Django',]},
    {'id':1,'nome':'Yuri', 'habilidades':['PHP','MySql','Django',]},
    {'id':2,'nome':'Silva', 'habilidades':['C#','Python', 'MySql',]},
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
# essa função busca, altera e exclui um objeto pelo id
def desenvolvedor(id):
    if request.method == 'GET':
        """Desenvolvedores recebe o id de acordo com a posição da lista"""
        # tratativa de error
        try:
            #desenvolvedor = desenvolvedores[id] # ou
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev de id {} not existe'.format(id)
            response = {'status': 404, 'message': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'message': mensagem}
            
        #return jsonify(desenvolvedor) # ou
        return jsonify(response)
        """ 
            para realizar a alteração com o put faça a seguinte alteração no postman
            body, raw, e altere de text para json e copie o conteúdo do get:
            {
                "habilidades": [
                    "PHP",
                    "MySql",
                    "Django"
                ],
                "nome": "Yuri"
            }
            Depois altere algun dado e execute novamente como put
            RESULTADO
            {
                "habilidades": [
                    "PHP",
                    "Java",
                    "Django"
                ],
                "nome": "Yuri"
            }
            .
        """
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        """poderia ser return jsonify({'status': 'success'})"""
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'success','mensagem': 'Removing the registered'})


# essa função lista e inclui um objeto, um registro.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_registro():
    """ inseri um registro """
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        '''para ser utilizado remova as linhas posicao = len e dados["id"]'''
        #return jsonify({'status': 'success', 'mensagem': 'Registro inserted'})
        return jsonify(desenvolvedores[posicao])
    
        """ lista registro """
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

    
if __name__ == '__main__':
    app.run(debug=True)

    