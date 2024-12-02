'''
Consultas a serem implementadas: 
2 - Consulta de conexões de um usuário: Obter a lista de amigos de um determinado usuário. 
'''
USE connectme;
SELECT 
    ipu.nome,
    c.email_conexao AS 'lista de amigos'
FROM informacoes_perfil_usuario AS ipu
JOIN usuario AS u ON ipu.id = u.id_perfil_usuario
JOIN conecta AS c ON c.email_usuario = u.email  
WHERE ipu.id = 2;
