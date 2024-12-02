'''
Consultas a serem implementadas: 
5 - Consulta de mensagens privadas: Listar as 10 mensagens privadas mais recentes trocadas entre 2 usuários dados como entrada.  
'''
SELECT 
    c.email_usuario,
    m.conteudo
FROM chat c
JOIN mensagem m ON c.id_mensagem = m.id
ORDER BY c.data_hora_mensagem;
