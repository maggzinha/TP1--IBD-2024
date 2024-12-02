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
