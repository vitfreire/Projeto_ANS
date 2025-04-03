SELECT 
    o.nome_fantasia,
    d.registro_ans,
    o.uf,
    SUM(d.valor) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE d.conta_contabil = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
  AND d.competencia >= DATE_SUB((SELECT MAX(competencia) FROM demonstracoes_contabeis), INTERVAL 1 YEAR)
GROUP BY d.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;
