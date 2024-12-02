'''
Consultas a serem implementadas: 
8 - Consulta de análise de engajamento: Dado um post de um usuário, fazer a contagem de quantos usuários interagiram com ele nos últimos 7 dias. 
'''
SELECT 
    p.id AS 'id post',
    p.email AS 'usuario postagem', 
    i.email_usuario AS 'interagiu postagem'
FROM 
    interage i
JOIN 
    postagem p ON i.id_postagem = p.id
WHERE 
    p.id = 10;
