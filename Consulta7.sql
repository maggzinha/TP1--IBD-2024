'''
Consultas a serem implementadas: 
7 - Consulta de tendências: Listar o identificador dos 5 posts com mais interações nos últimos 7 dias.
'''

SELECT id_postagem, COUNT(*) AS total_interacoes
FROM Interage
WHERE data_hora >= DATE_SUB(NOW(), INTERVAL 7 DAY)
GROUP BY id_postagem
ORDER BY total_interacoes DESC
LIMIT 20;
