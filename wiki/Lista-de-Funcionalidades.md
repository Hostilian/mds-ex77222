# Lista de Funcionalidades

**Proposta para discussão pelo grupo.** Cada funcionalidade tem um identificador único, uma descrição e os utilizadores com acesso.

- **E** — Explícito no pedido do cliente.
- **D** — Derivado para permitir o comportamento solicitado; validar a solução com o cliente.
- **P** — Proposta adicional; necessita de aprovação do cliente.

## Utilizadores referenciados

- **U01** — Participante da Universidade.
- **U02** — Participante externo à Universidade.
- **U03** — Organização do NEEI.
- **U04** — Responsável de torneio.
- **U05** — Visitante / espectador.

U04 aplica-se apenas a torneios atribuídos. U05 depende da aprovação de consulta pública. U01/U02 apenas consultam ou alteram os seus próprios dados privados. U03 acede a dados financeiros apenas quando autorizado dentro da organização.

| ID único | Funcionalidade | Descrição breve | Utilizadores com acesso | Origem |
| --- | --- | --- | --- | --- |
| F01 | Configurar o evento | Definir a edição da LAN Party, informações e parâmetros de inscrição. | U03 | D |
| F02 | Consultar informações do evento | Consultar as informações de inscrição e os torneios disponíveis. | U01, U02, U03, U04, U05 | P |
| F03 | Identificar o participante | Identificar a pessoa que se inscreve e recolher os dados necessários, incluindo a ligação à Universidade. | U01, U02 | D |
| F04 | Inscrever-se na LAN Party | Registar a inscrição de um participante no evento. | U01, U02 | E |
| F05 | Consultar a própria inscrição | Consultar o estado da sua inscrição no evento e, quando aplicável, do pagamento. | U01, U02 | D |
| F06 | Atualizar dados da própria inscrição | Corrigir dados de inscrição segundo os prazos e campos autorizados pela organização. | U01, U02 | P |
| F07 | Cancelar a própria inscrição | Solicitar o cancelamento da inscrição conforme a política do evento. | U01, U02 | P |
| F08 | Gerir inscrições no evento | Listar, pesquisar, consultar e atualizar o estado das inscrições pela organização. | U03 | E |
| F09 | Definir condições de pagamento | Configurar as condições e montantes eventualmente aplicáveis a participantes externos. | U03 | D |
| F10 | Iniciar um pagamento aplicável | Permitir ao participante externo iniciar o pagamento quando a sua inscrição o exigir. | U02 | E |
| F11 | Confirmar e reconciliar pagamentos | Registar uma confirmação fiável do pagamento e permitir a sua verificação pela organização. | U03 | D |
| F12 | Consultar pagamentos da organização | Consultar pagamentos associados às inscrições e identificar situações pendentes. | U03 | D |
| F13 | Configurar torneios | Criar os torneios da LAN Party e definir os parâmetros necessários às respetivas inscrições. | U03 | D |
| F14 | Consultar torneios | Consultar os torneios disponíveis e as respetivas condições de inscrição. | U01, U02, U03, U04, U05 | D |
| F15 | Inscrever-se num torneio | Registar a inscrição do participante num dos torneios da LAN Party. | U01, U02 | E |
| F16 | Consultar as próprias inscrições em torneios | Consultar o estado das inscrições do participante nos diversos torneios. | U01, U02 | D |
| F17 | Cancelar inscrição num torneio | Cancelar uma inscrição em torneio quando as regras o permitirem. | U01, U02 | P |
| F18 | Gerir inscrições nos torneios | Consultar e gerir as inscrições de cada torneio pela organização ou pelo responsável autorizado. | U03, U04 | E |
| F19 | Registar resultados de um torneio | Introduzir os resultados necessários à consulta durante e após o torneio. | U03, U04 | D |
| F20 | Consultar resultados em tempo real | Consultar os resultados publicados de cada torneio durante a sua realização. | U01, U02, U03, U04, U05 | E |
| F21 | Consultar resultados após o torneio | Consultar os resultados de um torneio depois de este terminar. | U01, U02, U03, U04, U05 | E |
| F22 | Corrigir resultados com histórico | Corrigir resultados publicados mantendo o motivo e a identificação do responsável. | U03, U04 | P |
| F23 | Atribuir responsáveis de torneio | Atribuir a uma pessoa a gestão de um ou mais torneios. | U03 | P |

## Critérios de revisão propostos

Ajudam a discutir o significado das funcionalidades; não representam critérios de aceitação já aprovados pelo cliente.

| ID | Critério a discutir |
| --- | --- |
| F01 | Os parâmetros definidos pela organização são usados nas inscrições da edição correta. |
| F02 | As informações mostradas correspondem à edição e aos torneios selecionados. |
| F03 | Cada inscrição fica associada a um participante identificado; conta própria e método de verificação ficam por confirmar. |
| F04 | Uma inscrição válida recebe um identificador e um estado e pode ser consultada posteriormente. |
| F05 | O participante consulta a sua inscrição, sem acesso às inscrições privadas de outras pessoas. |
| F06 | Só o titular pode alterar os campos e nos períodos permitidos pela política aprovada. |
| F07 | O estado muda para cancelado quando permitido; o efeito sobre pagamentos exige política de reembolso aprovada. |
| F08 | A organização consegue consultar e gerir inscrições identificadas, preservando a consistência dos estados. |
| F09 | Só são aplicadas cobranças segundo uma política aprovada; o pedido não fixa preço nem torna obrigatório cobrar todos os externos. |
| F10 | O pagamento fica associado à inscrição correta e ao montante aplicável; o método pode ser online ou manual, a confirmar. |
| F11 | Uma confirmação válida atualiza o estado financeiro; a repetição da mesma confirmação não duplica o pagamento. O participante inicia F10, mas não pode confirmar o próprio pagamento. |
| F12 | Apenas pessoas autorizadas pela organização consultam os dados financeiros necessários. |
| F13 | Cada torneio tem um identificador próprio e fica associado ao evento correto. |
| F14 | O utilizador consegue distinguir os torneios e consultar as condições aprovadas para cada um. |
| F15 | A inscrição fica associada ao participante e ao torneio corretos; regras de elegibilidade e equipas dependem de confirmação. |
| F16 | A lista mostra apenas as inscrições pertencentes ao participante autenticado ou identificado de forma segura. |
| F17 | O cancelamento respeita os prazos e as consequências definidos para esse torneio. |
| F18 | U04 só gere torneios atribuídos; U03 gere os torneios sob responsabilidade da organização. |
| F19 | Um resultado válido fica associado ao torneio correto e ao responsável pelo registo. |
| F20 | Os resultados apresentados refletem as atualizações publicadas; o atraso máximo aceitável deve ser acordado com o cliente. |
| F21 | O fim de um torneio não impede a consulta dos seus resultados. O período de retenção deve ser acordado. |
| F22 | Só o responsável autorizado corrige o resultado; a alteração conserva o valor anterior e o motivo. |
| F23 | As permissões de U04 ficam limitadas aos torneios atribuídos. |

[Lista de Utilizadores](Lista-de-Utilizadores) · [Questões para o Cliente](Questões-para-o-Cliente) · [Home](Home)
