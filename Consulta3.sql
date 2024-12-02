'''Consultas a serem implementadas: 
3 - Consulta de postagens de um usuário: Recuperar todas as postagens feitas por um usuário específico, ordenadas por data de publicação (as mais recentes primeiro). 
'''
SELECT 
	tipo, 
    arquivo, 
    texto, 
    data_hora
FROM Postagem
WHERE email = 'viananina@exemple.org'
ORDER BY data_hora;
