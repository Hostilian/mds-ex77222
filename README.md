# NEEI LAN Party 2026

**INF13204L — Metodologias e Desenvolvimento de Software · Universidade de Évora**

Preparação das aulas práticas 1–3: configuração do GitHub, identificação de utilizadores e funcionalidades e restrições do sistema.

**Estado:** proposta inicial para revisão do grupo. A formação do grupo, aprovação do cliente e publicação na Wiki ainda precisam de ser concluídas. Não existe aplicação de gestão ou sistema de pagamentos implementado neste pacote.

## Ler primeiro

- [Guia rápido em inglês](docs/START-HERE-EN.md)
- [Configuração do GitHub e publicação na Wiki](docs/GITHUB-SETUP.md)
- [Checklist do enunciado](docs/ASSIGNMENT-CHECKLIST.md)
- [Equipa e decisões](docs/TEAM.md)

## Conteúdo da Wiki

Os ficheiros em `wiki/` são preparados para publicação na **Wiki nativa do GitHub**, que usa um repositório próprio. Guardá-los apenas na pasta `wiki/` do repositório principal não conclui o requisito do professor.

- [Home — pedido do cliente](wiki/Home.md)
- [Lista de Utilizadores](wiki/Lista-de-Utilizadores.md)
- [Lista de Funcionalidades](wiki/Lista-de-Funcionalidades.md)
- [restrições do sistema](wiki/restrições-do-sistema.md)
- [Questões para o Cliente](wiki/Questões-para-o-Cliente.md)
- [Rastreabilidade](wiki/Rastreabilidade.md)

## Atualizar e verificar

A fonte dos requisitos é `data/project.json`. Editar essa fonte e voltar a gerar a documentação:

```sh
python scripts/build_docs.py
python scripts/validate.py
```

Abrir `build/index.html` para uma leitura offline. A pipeline em `.github/workflows/docs.yml` verifica referências e permissões declaradas, confirma a correspondência entre os dados e a Wiki, gera a documentação e guarda um artefacto. Não publica um site nem utiliza credenciais de pagamento.

## Âmbito e incertezas

Cada item indica se é explícito no pedido (`E`), derivado (`D`) ou proposta adicional (`P`). As funções propostas e os utilizadores adicionais precisam de discussão. Cerca de 5000 inscrições não significa 5000 pessoas simultâneas ou uma lotação máxima. Pagamentos para externos são condicionais; o cliente não indicou preço nem método.

GitHub Pages não é necessário para estas tarefas. A apresentação offline acompanha a documentação. O repositório da prática 1 deve ser privado e chamar-se `mds-ex77222`, sujeito à confirmação do identificador de aluno. A Wiki do projeto de grupo pode usar o mesmo repositório se o professor aceitar, ou um repositório criado por um único membro do grupo.
