import pytest
from pytest import mark
from codigo.bytebank import Funcionario


class TestClass:
    @pytest.fixture()
    def funcionario_teste(self):
        return Funcionario('Teste')

    def test_retorna_o_atributo_nome(self, funcionario_teste):
        assert funcionario_teste.nome == 'Teste'

    def test_retorna_o_atributo_data_nascimento(self, funcionario_teste):
        data_nascimento = '11/09/2001'
        funcionario_teste.data_nascimento = data_nascimento
        assert funcionario_teste.data_nascimento == data_nascimento

    def test_retorna_o_atributo_salario(self, funcionario_teste):
        salario_atual = 1000
        funcionario_teste.salario = salario_atual
        assert funcionario_teste.salario == salario_atual

    def test_quando_idadde_recebe_13_03_2000_deve_retornar_23(self, funcionario_teste):
        entrada_data = '13/03/2000'
        entada_salario = 1111
        saida = 23

        funcionario_teste.data_nascimento = entrada_data
        funcionario_teste.salario = entada_salario
        resultado = funcionario_teste.idade()

        assert resultado == saida

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self, funcionario_teste):
        entrada_nome = 'Lucas Carvalho'
        saida = 'Carvalho'
        funcionario_teste.nome = entrada_nome
        resultado = funcionario_teste.sobrenome()

        assert saida == resultado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self, funcionario_teste):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        funcionario_teste.salario = entrada_salario
        funcionario_teste.nome = entrada_nome
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste._salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, funcionario_teste):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste.salario = entrada_salario
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000000_deve_retornar_exception(self, funcionario_teste):
        with pytest.raises(Exception):
            entrada_salario = 1000000000

            funcionario_teste.salario = entrada_salario
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
