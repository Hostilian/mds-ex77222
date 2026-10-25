# Checklist do enunciado

Os estados abaixo distinguem conteúdo preparado, publicação e ações humanas pendentes. Não são uma certificação automática de conclusão.

| Prática | Exigência | Preparação neste pacote | Conclusão real a verificar |
| --- | --- | --- | --- |
| 1 | Conta com email da Universidade | Guia de configuração | Email adicionado e verificado; professor aceita conta existente |
| 1 | Conta de estudante validada | Guia de candidatura | Aprovação da Education e benefícios ativos |
| 1 | Rede da Universidade | Instrução preservada | Candidatura feita no contexto pedido pelo professor |
| 1 | Two Factor Authentication | Guia, sem segredos | 2FA ativa na conta |
| 1 | Cartão ou prova de matrícula | Orientação; nenhum documento incluído | Evidência atual submetida quando pedida |
| 1 | Repositório privado `mds-ex77222` | Repositório `Hostilian/mds-ex77222` existe | **PENDENTE:** API GitHub confirmou visibilidade **PUBLIC** em 25/10/2026; alterar para Private depois de avaliar acesso à Wiki com plano GitHub adequado |
| 1 | Adicionar `pedrosalgueiro` | Utilizador exato identificado no enunciado | **VERIFICADO PARCIALMENTE 25/10/2026:** API devolve permissão `read`; como o repositório é atualmente PUBLIC, isto **não prova** convite aceite nem acesso após mudar para Private; confirmar em Settings → Collaborators |
| 2 | Grupo de 2 ou 3 | Registo vazio e roteiro de discussão | Membros reais confirmados |
| 2 | Um único criador do projeto | Guia de coordenação | Repositório acordado com o grupo |
| 2 | Conta com email de aluno validada | Mesmos passos da prática 1 | Conta/estado comprovados |
| 2 | Todos os membros adicionados | Guia de colaboradores | Acesso efetivo verificado para cada membro |
| 2 | Pedido do cliente na Home | `wiki/Home.md`, texto preservado | Home publicada na Wiki nativa |
| 2 | Link Lista de Utilizadores na Home | Preparado e verificado localmente | Link aberto na Wiki nativa |
| 2 | Link Lista de Funcionalidades na Home | Preparado e verificado localmente | Link aberto na Wiki nativa |
| 2 | Discutir utilizadores em grupo | Lista inicial com origem e âmbito | Discussão e revisão reais |
| 2 | Lista de utilizadores na Wiki | 5 papéis humanos; integrações separadas | Página publicada e aprovada pelo grupo |
| 2 | Discutir funcionalidades em grupo | 23 funções e perguntas | Discussão e revisão reais |
| 2 | IDs, descrição e utilizadores por função | F01–F23 e referências U01–U05 | Página publicada e acessos revistos |
| 3 | Página restrições do sistema | Título exato e 18 restrições preparadas | Página publicada na Wiki nativa |
| 3 | Base para requisitos não funcionais | Categoria, requisito candidato e validação por restrição | Propostas e critérios revistos; valores em aberto acordados |

## Auditoria de estado em 25/10/2026

Os estados acima representam apenas o que é verificável: **documentação preparada não equivale à publicação na Wiki**, e a API não mostrou grupo de 2–3 estudantes nem confirmação da avaliação pelo professor. GitHub Free permite Wiki em repositórios públicos; para uma Wiki privada pode ser necessário GitHub Pro/Education, Team ou equivalente (consultar https://docs.github.com/en/communities/documenting-your-project-with-wikis). Não publicar trabalhos académicos confidenciais para contornar esta limitação. Antes de alterar a visibilidade do repositório, confirmar as funcionalidades do plano e o requisito exato com a equipa/avaliação; uma mudança Public→Private pode desativar a Wiki se o plano não suportar Wiki privada.

## Verificação técnica

- `python scripts/build_docs.py` gera as páginas e o leitor offline.
- `python scripts/validate.py` verifica IDs, referências, papéis, rastreabilidade, links locais e correspondência entre a fonte e as páginas.
- A pipeline apenas automatiza essa verificação técnica. Não confirma Education, 2FA, formação do grupo, discussão nem publicação da Wiki.

## Fontes do enunciado

- [Prática 1](https://www.moodle.uevora.pt/2627/mod/assign/view.php?id=18885)
- [Prática 2](https://www.moodle.uevora.pt/2627/mod/assign/view.php?id=18879)
- [Prática 3](https://www.moodle.uevora.pt/2627/mod/assign/view.php?id=18877)

Texto fornecido pelo aluno em 2026-10-01. Os links Moodle podem exigir autenticação.
