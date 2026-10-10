# =====================================================================

# SUAS RESPOSTAS

# =====================================================================

# Escreva cada consulta SQL entre as aspas triplas, assim:

#

#   Q1 = """

#   SELECT ...

#   FROM ...

#   """

#

# Depois salve o arquivo (Ctrl+S) e veja o resultado no painel.

# Mexa só no que está ENTRE as aspas triplas.

# =====================================================================



# ---------------------------------------------------------------------

# NÍVEL 1 - AQUECIMENTO

# ---------------------------------------------------------------------



# Q1. Clientes no Centro

# Colunas do resultado: ClientesNoCentro

Q1 = """

SELECT CLIENTES.BAIRRO,
COUNT (*) AS ClientesNoCentro
FROM Clientes
WHERE Bairro LIKE 'CENTRO'
GROUP BY CLIENTES.BAIRRO

"""



# Q2. Hambúrgueres acima de R$ 30

# Colunas do resultado: NomeProduto, Preco

Q2 = """

SELECT PRODUTOS.NomeProduto, PRODUTOS.Preco
FROM PRODUTOS
WHERE PRODUTOS.Preco > 30
GROUP BY PRODUTOS.NomeProduto, PRODUTOS.preco

"""



# Q3. Pedidos por status

# Colunas do resultado: Status, QuantidadePedidos

Q3 = """
SELECT PEDIDOS.Status,
COUNT (*) AS QuantidadePedidos
FROM PEDIDOS
WHERE PEDIDOS.Status LIKE 'ENTREGUE' or PEDIDOS.Status LIKE 'CANCELADO'
GROUP BY PEDIDOS.STATUS


"""



# Q4. Nota média e pedidos sem avaliação

# Colunas do resultado: PedidosEntregues, PedidosAvaliados, PedidosSemAvaliacao, NotaMedia

Q4 = """

SELECT
COUNT (*) AS PedidosEntregues,
COUNT (AVALIACAO) AS PedidosAvaliados,
COUNT(*) - COUNT (AVALIACAO) AS PedidosSemAvaliacao,
CAST(AVG (AVALIACAO) AS DECIMAL (4,2)) AS NotaMedia
FROM Pedidos
WHERE STATUS = 'ENTREGUE';

"""



# Q5. Delivery x Retirada por mês

# Colunas do resultado: Mes, TipoEntrega, QuantidadePedidos

Q5 = """

SELECT MONTH(DATAPEDIDO), PEDIDOS.TipoEntrega,
COUNT (*) AS QuantidadePedidos
FROM PEDIDOS
WHERE TipoEntrega LIKE 'DELIVERY' OR TipoEntrega LIKE 'RETIRADA'
GROUP BY MONTH(DATAPEDIDO), PEDIDOS.TIPOENTREGA
ORDER BY MONTH(DATAPEDIDO)


"""



# ---------------------------------------------------------------------

# NÍVEL 2 - CRUZANDO TABELAS

# ---------------------------------------------------------------------



# Q6. Pedidos de janeiro com cliente

# Colunas do resultado: IdPedido, DataPedido, Nome, Bairro, Status

Q6 = """
SELECT PEDIDOS.IdPedido, PEDIDOS.DataPedido, PEDIDOS.IdCliente, CLIENTES.Nome, Clientes.Bairro, Pedidos.Status
FROM PEDIDOS INNER JOIN CLIENTES ON PEDIDOS.IdCliente = Clientes.IdCliente
WHERE DataPedido BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY MONTH(DATAPEDIDO)


"""



# Q7. Entregas por entregador

# Colunas do resultado: Nome, Entregas

Q7 = """
SELECT entregadores.Nome,
COUNT (PEDIDOS.STATUS) AS Entregas
FROM PEDIDOS INNER JOIN ENTREGADORES ON PEDIDOS.IdEntregador = Entregadores.IdEntregador
WHERE STATUS = 'Entregue'
GROUP BY entregadores.Nome
ORDER BY Entregas DESC


"""



# Q8. Unidades e faturamento por produto

# Colunas do resultado: NomeProduto, UnidadesVendidas, Faturamento

Q8 = """
SELECT ItensPedido.IdProduto, ITENSPEDIDO.PrecoUnitario,
SUM (QUANTIDADE) AS UnidadesVendidas,
SUM (QUANTIDADE * PRECOUNITARIO) AS FATURAMENTO
FROM PEDIDOS INNER JOIN ITENSPEDIDO ON PEDIDOS.IdPedido = ItensPedido.IdPedido
WHERE STATUS = 'ENTREGUE'
GROUP BY IdProduto, PrecoUnitario
ORDER BY UnidadesVendidas DESC


"""



# Q9. Faturamento por categoria

# Colunas do resultado: Categoria, Faturamento

Q9 = """
SELECT Produtos.Categoria,
SUM (QUANTIDADE * PRECOUNITARIO) AS Faturamento
FROM PEDIDOS
INNER JOIN ITENSPEDIDO ON PEDIDOS.IdPedido = ItensPedido.IdPedido
INNER JOIN PRODUTOS ON ITENSPEDIDO.IDPRODUTO = PRODUTOS.IDPRODUTO
WHERE STATUS = 'ENTREGUE'
GROUP BY Categoria
ORDER BY Faturamento DESC


"""



# Q10. Bairros com 7+ pedidos entregues

# Colunas do resultado: Bairro, PedidosEntregues

Q10 = """



"""



# Q11. Preços praticados do X-Bacon

# Colunas do resultado: PrecoUnitario, Unidades, Faturamento

Q11 = """



"""



# ---------------------------------------------------------------------

# NÍVEL 3 - DESAFIO

# ---------------------------------------------------------------------



# Q12. Top 3 clientes (fidelidade)

# Colunas do resultado: Nome, Pedidos, TotalGasto

Q12 = """



"""



# Q13. Faturamento mês a mês

# Colunas do resultado: Mes, PedidosEntregues, Faturamento

Q13 = """



"""



# Q14. Entregador do trimestre

# Colunas do resultado: Nome, Entregas, NotaMedia

Q14 = """



"""



# Q15. Valor total dos pedidos de março

# Colunas do resultado: IdPedido, Nome, ValorProdutos, TaxaEntrega, ValorTotal

Q15 = """



"""



# Q16. Clientes sem nenhum pedido

# Colunas do resultado: Nome, Bairro, DataCadastro

Q16 = """



"""



# Q17. Produto que nunca foi vendido

# Colunas do resultado: NomeProduto, Categoria, Preco

Q17 = """



"""