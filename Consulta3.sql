'''Consultas a serem implementadas: 
3 - Consulta de postagens de um usuário: Recuperar todas as postagens feitas por um usuário específico, ordenadas por data de publicação (as mais recentes primeiro). 
'''
USE connectme;
SELECT 
    email,
    tipo,
    arquivo,
    texto,  
    data_hora
FROM postagem
WHERE email = 'amanda48@example.org'
ORDER BY data_hora;
