from flask import Blueprint, request, jsonify
from .logic import add, subtract, multiply, divide

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if num1 is None or num2 is None or operation is None:
        return jsonify({'error': 'Dados insuficientes fornecidos.'}), 400

    try:
        # Convertendo para float para lidar com números decimais
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            return jsonify({'error': 'Operação inválida.'}), 400

        return jsonify({'result': result}), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e: # Captura outros erros inesperados
        return jsonify({'error': 'Erro interno do servidor.'}), 500 