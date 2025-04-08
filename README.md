# Validador de CPF

## Descrição do Projeto

Este projeto foi desenvolvido para validar um CPF (Cadastro de Pessoas Físicas) utilizando a linguagem de programação Python. A função principal do código é garantir que o CPF inserido seja válido de acordo com as regras de cálculo do CPF definidas pela Receita Federal do Brasil.

A validação do CPF é feita através do cálculo dos dois últimos dígitos verificadores. Caso esses dígitos coincidam com os calculados pelo programa, o CPF é considerado válido.

## Funcionalidades

- O usuário pode inserir um CPF com pontos e traços.
- O código remove a formatação do CPF automaticamente.
- O CPF é validado verificando os dois dígitos verificadores.
- O sistema informa se o CPF é válido ou inválido.

## Como Funciona

1. **Entrada de Dados**: O usuário insere o CPF no formato desejado com pontuação.
2. **Limpeza do CPF**: O programa remove os caracteres de formatação, como pontos e traços.
3. **Cálculo dos Dígitos Verificadores**: O algoritmo realiza os cálculos dos dois últimos dígitos do CPF utilizando multiplicação e módulo 11.
4. **Validação**: O CPF é validado comparando os dígitos verificadores calculados com os dois últimos números do CPF informado.
