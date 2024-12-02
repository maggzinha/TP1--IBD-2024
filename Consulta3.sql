USE connectme;
SELECT 
    email,
    tipo,
    arquivo,
    texto,  
    data_hora
FROM postagem
WHERE email = 'acardoso@example.net'
ORDER BY data_hora;
