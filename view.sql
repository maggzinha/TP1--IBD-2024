CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `connectme`.`informacoes_perfil_usuario` AS
    SELECT 
        `pu`.`id` AS `id`,
        `pu`.`nome` AS `nome`,
        `pu`.`foto` AS `foto`,
        `pu`.`data_nascimento` AS `data_nascimento`,
        `pu`.`endereco` AS `endereco`,
        `pu`.`biografia` AS `biografia`,
        (SELECT 
                COUNT(0)
            FROM
                `connectme`.`conecta`
            WHERE
                (`connectme`.`conecta`.`email_usuario` = `connectme`.`usuario`.`email`)) AS `quantidade_amigo`
    FROM
        (`connectme`.`perfil_usuario` `pu`
        JOIN `connectme`.`usuario` ON ((`connectme`.`usuario`.`id_perfil_usuario` = `pu`.`id`)))
