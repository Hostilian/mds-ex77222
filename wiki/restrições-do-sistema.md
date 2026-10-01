# restrições do sistema

**Proposta inicial para discussão.** As restrições servem de base à identificação dos requisitos não funcionais. Incluem também contexto e regras de negócio, que devem ser separados dos critérios de qualidade na próxima análise.

- **E** — Explícito no pedido do cliente.
- **D** — Derivado para permitir o comportamento solicitado; validar a solução com o cliente.
- **P** — Proposta adicional; necessita de aprovação do cliente.

Uma restrição é uma condição que limita ou orienta a solução. O requisito de qualidade candidato e a forma de validação abaixo são propostas para transformar essa condição em algo verificável. Valores ainda desconhecidos devem ser acordados, sem inventar limites ou compromissos.

## R01 — Contexto da edição de 2026

**Origem:** E · **Categoria:** Contexto e prazo.

**Restrição:** O sistema destina-se à LAN Party organizada pelo NEEI em 2026. Datas de entrega e de realização não constam do pedido.

**Requisito candidato:** Planear disponibilidade antes do início das inscrições; acordar calendário de entrega e validação.

**Como validar:** Obter do cliente as datas do evento, abertura das inscrições e prazo de entrega.

## R02 — Volume esperado de inscrições

**Origem:** E · **Categoria:** Capacidade.

**Restrição:** São previstas cerca de 5000 inscrições no evento. Esta previsão não define um limite máximo nem 5000 utilizadores simultâneos.

**Requisito candidato:** Armazenar e gerir o volume esperado e avaliar picos de procura com dados do cliente.

**Como validar:** Testar operações representativas com cerca de 5000 inscrições; acordar margem e carga simultânea.

## R03 — Consulta de resultados em tempo real

**Origem:** E · **Categoria:** Desempenho e atualização.

**Restrição:** Os resultados de cada torneio devem poder ser consultados em tempo real.

**Requisito candidato:** Definir um limite mensurável entre publicação e apresentação de um resultado.

**Como validar:** Acordar o atraso máximo com o cliente e medi-lo sob a carga simultânea aprovada.

## R04 — Resultados disponíveis após os torneios

**Origem:** E · **Categoria:** Persistência e disponibilidade.

**Restrição:** A consulta dos resultados deve continuar após o fim de cada torneio.

**Requisito candidato:** Conservar resultados e garantir consulta durante um período acordado.

**Como validar:** Terminar um torneio e confirmar a consulta dos resultados; acordar retenção e disponibilidade.

## R05 — Pagamentos condicionais para externos

**Origem:** E · **Categoria:** Regra de negócio e integração.

**Restrição:** O pedido inclui possíveis pagamentos para pessoas externas à Universidade. Não fixa preço, método, isenções ou política de reembolso.

**Requisito candidato:** Permitir aplicar a política de pagamento acordada sem inventar valores ou condições.

**Como validar:** Obter tabela de condições e verificar cenários de pagamento aplicável e não aplicável.

## R06 — Separação entre evento e torneios

**Origem:** D · **Categoria:** Integridade dos dados.

**Restrição:** As inscrições no evento e nos diversos torneios são registos distintos, relacionados com o mesmo participante.

**Requisito candidato:** Preservar referências consistentes entre participantes, evento, torneios e inscrições.

**Como validar:** Verificar que uma inscrição de torneio referencia o participante e o torneio corretos; confirmar elegibilidade com o cliente.

## R07 — Acesso conforme o papel

**Origem:** D · **Categoria:** Segurança e autorização.

**Restrição:** A gestão de inscrições, pagamentos e resultados deve ficar limitada às pessoas autorizadas; cada participante deve aceder aos seus próprios dados privados.

**Requisito candidato:** Aplicar autorização em cada operação e impedir leitura ou alteração de dados de terceiros.

**Como validar:** Tentar consultar inscrição alheia, confirmar o próprio pagamento e alterar torneio não atribuído; verificar a recusa.

## R08 — Verificação da ligação à Universidade

**Origem:** D · **Categoria:** Identificação e interoperabilidade.

**Restrição:** É necessário distinguir participantes da Universidade e externos para aplicar condições de pagamento. O método de verificação é desconhecido.

**Requisito candidato:** Usar uma verificação fiável e adequada ao contexto, a acordar.

**Como validar:** Definir evidência aceite e testar classificação válida, inválida e em análise.

## R09 — Consistência das confirmações de pagamento

**Origem:** D · **Categoria:** Fiabilidade e integridade.

**Restrição:** Se houver pagamentos, uma confirmação repetida ou inválida não pode originar cobrança duplicada nem ativação indevida da inscrição.

**Requisito candidato:** Validar confirmações e tratar repetições de forma idempotente.

**Como validar:** Repetir uma confirmação e enviar outra inválida; confirmar um único pagamento válido e nenhum estado indevido.

## R10 — Alterações concorrentes

**Origem:** D · **Categoria:** Concorrência e integridade.

**Restrição:** Podem existir pedidos simultâneos de inscrição e atualização de resultados. A carga e as regras de lotação precisam de confirmação.

**Requisito candidato:** Evitar perda de atualizações e inconsistência dos dados; respeitar uma eventual lotação aprovada.

**Como validar:** Testar pedidos concorrentes e preservar os resultados corretos; não assumir uma lotação de 5000.

## R11 — Proteção dos dados recolhidos

**Origem:** D · **Categoria:** Privacidade.

**Restrição:** As inscrições envolvem dados de participantes e podem envolver informação financeira. Campos, retenção e requisitos aplicáveis devem ser definidos com o cliente.

**Requisito candidato:** Recolher apenas dados necessários, limitar acesso e definir retenção; confirmar os requisitos de proteção de dados aplicáveis.

**Como validar:** Rever os campos e permissões com o cliente e testar acesso indevido e o procedimento de retenção aprovado.

## R12 — Continuidade do serviço

**Origem:** P · **Categoria:** Recuperabilidade.

**Restrição:** A perda de dados de inscrições, pagamentos ou resultados pode prejudicar o evento; cópias de segurança e recuperação são propostas.

**Requisito candidato:** Definir frequência de cópias e objetivos de recuperação de dados e serviço.

**Como validar:** Acordar objetivos e executar uma restauração de teste com verificação dos registos.

## R13 — Dependências de serviços externos

**Origem:** P · **Categoria:** Interoperabilidade e disponibilidade.

**Restrição:** A utilização de um prestador de pagamentos ou identificação institucional pode criar dependências; nenhuma integração foi exigida pelo cliente.

**Requisito candidato:** Definir contratos de integração e comportamento perante falhas, se a integração for aprovada.

**Como validar:** Simular serviço indisponível e retoma, evitando confirmação indevida e duplicação de operações.

## R14 — Facilidade de utilização

**Origem:** P · **Categoria:** Usabilidade e acessibilidade.

**Restrição:** Os participantes e a organização podem ter níveis diferentes de experiência; interface simples e mensagens claras são propostas.

**Requisito candidato:** Definir tarefas de utilização e critérios de acessibilidade adequados ao público aprovado.

**Como validar:** Acordar perfis e critérios; observar inscrições e consulta de resultados em testes de utilização.

## R15 — Plataforma e ambiente de execução

**Origem:** P · **Categoria:** Implantação e portabilidade.

**Restrição:** O pedido não impõe aplicação web, linguagem, base de dados, Docker, serviços pagos ou GitHub Pages. O ambiente e a conectividade do evento estão por conhecer.

**Requisito candidato:** Selecionar a plataforma após conhecer dispositivos, alojamento, rede e suporte disponíveis.

**Como validar:** Confirmar o ambiente com o cliente e testar a solução nas plataformas aprovadas.

## R16 — Orçamento e recursos

**Origem:** E · **Categoria:** Custo e manutenção.

**Restrição:** O cliente pretende um orçamento, mas não forneceu teto financeiro, recursos disponíveis ou condições de manutenção.

**Requisito candidato:** Apresentar estimativa com pressupostos, custos recorrentes, dependências e âmbito acordado.

**Como validar:** Esclarecer recursos e âmbito antes de estimar; separar custo de desenvolvimento de operação e manutenção.

## R17 — Regras dos torneios

**Origem:** D · **Categoria:** Regras de negócio.

**Restrição:** Formato, inscrições individuais ou por equipas, lotação, desempates e conflito de horários não foram especificados.

**Requisito candidato:** Confirmar regras antes de modelar estruturas e validações de torneios.

**Como validar:** Recolher regras por torneio e verificar casos aceites e recusados segundo essas regras.

## R18 — Visibilidade dos resultados

**Origem:** D · **Categoria:** Autorização e privacidade.

**Restrição:** A consulta de resultados é exigida, mas a publicação para visitantes sem inscrição não foi especificada.

**Requisito candidato:** Acordar quais dados podem ser públicos e quais exigem acesso autorizado.

**Como validar:** Validar política com o cliente; testar visitante e participante para dados públicos e privados.

[Questões para o Cliente](Questões-para-o-Cliente) · [Rastreabilidade](Rastreabilidade) · [Home](Home)
