USE connectme;
SELECT 
    email,
    tipo,
    arquivo,
    texto,  
    data_hora
FROM postagem
WHERE email = 'abreubenicio@example.com'
ORDER BY data_hora;
