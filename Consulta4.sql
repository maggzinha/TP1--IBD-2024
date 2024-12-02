'''
Consultas a serem implementadas: 
4 - Consulta de postagens em um grupo: Listar 20 as postagens mais recentes feitas em um grupo específico. 
'''
SELECT * 
FROM Postagem 
WHERE id_grupo = 1  -- Substitua '1' pelo ID do grupo desejado 
ORDER BY data_hora DESC;
