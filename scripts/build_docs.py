#!/usr/bin/env python3
"""Build native GitHub Wiki sources and a self-contained offline reader."""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list[str]]) -> str:
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *["| " + " | ".join(cell(v) for v in row) + " |" for row in rows],
    ]) + "\n"


def legend(data: dict) -> str:
    return "\n".join(f"- **{key}** — {value}." for key, value in data["evidence"].items()) + "\n"


def wiki_pages(data: dict) -> dict[str, str]:
    names = {a["id"]: a["name"] for a in data["actors"]}
    navigation = (
        "- [Lista de Utilizadores](Lista-de-Utilizadores)\n"
        "- [Lista de Funcionalidades](Lista-de-Funcionalidades)\n"
        "- [restrições do sistema](restrições-do-sistema)\n"
        "- [Questões para o Cliente](Questões-para-o-Cliente)\n"
        "- [Rastreabilidade](Rastreabilidade)\n"
    )
    home = (
        f"# {data['title']}\n\n{data['course']}\n\n"
        f"**Estado:** {data['status']}. A discussão de grupo e a aprovação das propostas ainda não estão registadas.\n\n"
        "## Pedido do cliente\n\n" + data["client_request"] + "\n\n"
        "## Documentação\n\n" + navigation + "\n"
        "## Como ler esta proposta\n\n" + legend(data) + "\n"
        "As listas distinguem o que o cliente pediu e o que sugerimos esclarecer ou acrescentar. "
        "Os valores de desempenho, preços, prazos e tecnologias em aberto não são apresentados como decisões do cliente.\n\n"
        "## Trabalho do grupo\n\n"
        "Formar um grupo de 2 ou 3 alunos, escolher um único criador do projeto e adicionar todos os membros. "
        "Todos devem discutir, rever e registar as decisões relativas às listas. "
        "A configuração do email de aluno, Education e 2FA e o acesso do professor são passos separados da redação das páginas.\n\n"
        "Fonte: enunciados das aulas práticas 1–3 fornecidos pelo aluno em 2026-10-01. "
        "Não foi ainda registada uma aprovação do NEEI.\n"
    )
    users = "# Lista de Utilizadores\n\n**Proposta para discussão pelo grupo.**\n\n" + legend(data) + "\n"
    users += table(["ID", "Utilizador", "Descrição", "Origem"], [
        [a["id"], a["name"], a["description"], a["source"]] for a in data["actors"]
    ]) + "\n## Âmbito do acesso\n\n"
    users += "\n".join(f"- **{a['id']} — {a['name']}:** {a['scope']}" for a in data["actors"]) + "\n\n"
    users += "U01 e U02 são categorias do papel participante. A organização U03 é derivada do contexto de gestão; "
    users += "U04 e U05 são propostas, não novos perfis já exigidos pelo cliente. "
    users += "A pessoa responsável de torneio pode pertencer à organização e acumular papéis.\n\n"
    users += "## Sistemas externos possíveis\n\nNão são utilizadores humanos e não recebem permissões humanas na lista de funcionalidades.\n\n"
    users += table(["ID", "Sistema", "Descrição", "Origem"], [
        [s["id"], s["name"], s["description"], s["source"]] for s in data["external_systems"]
    ]) + "\n[Voltar à Home](Home)\n"
    funcs = "# Lista de Funcionalidades\n\n**Proposta para discussão pelo grupo.** Cada funcionalidade tem um identificador único, uma descrição e os utilizadores com acesso.\n\n"
    funcs += legend(data) + "\n## Utilizadores referenciados\n\n"
    funcs += "\n".join(f"- **{aid}** — {name}." for aid, name in names.items()) + "\n\n"
    funcs += "U04 aplica-se apenas a torneios atribuídos. U05 depende da aprovação de consulta pública. "
    funcs += "U01/U02 apenas consultam ou alteram os seus próprios dados privados. "
    funcs += "U03 acede a dados financeiros apenas quando autorizado dentro da organização.\n\n"
    funcs += table(["ID único", "Funcionalidade", "Descrição breve", "Utilizadores com acesso", "Origem"], [
        [f["id"], f["name"], f["description"], ", ".join(f["actors"]), f["source"]]
        for f in data["functions"]
    ]) + "\n## Critérios de revisão propostos\n\n"
    funcs += "Ajudam a discutir o significado das funcionalidades; não representam critérios de aceitação já aprovados pelo cliente.\n\n"
    funcs += table(["ID", "Critério a discutir"], [[f["id"], f["acceptance"]] for f in data["functions"]])
    funcs += "\n[Lista de Utilizadores](Lista-de-Utilizadores) · [Questões para o Cliente](Questões-para-o-Cliente) · [Home](Home)\n"
    restrictions = "# restrições do sistema\n\n**Proposta inicial para discussão.** As restrições servem de base à identificação dos requisitos não funcionais. "
    restrictions += "Incluem também contexto e regras de negócio, que devem ser separados dos critérios de qualidade na próxima análise.\n\n"
    restrictions += legend(data) + "\nUma restrição é uma condição que limita ou orienta a solução. "
    restrictions += "O requisito de qualidade candidato e a forma de validação abaixo são propostas para transformar essa condição em algo verificável. "
    restrictions += "Valores ainda desconhecidos devem ser acordados, sem inventar limites ou compromissos.\n\n"
    for r in data["constraints"]:
        restrictions += f"## {r['id']} — {r['name']}\n\n"
        restrictions += f"**Origem:** {r['source']} · **Categoria:** {r['category']}.\n\n"
        restrictions += f"**Restrição:** {r['description']}\n\n"
        restrictions += f"**Requisito candidato:** {r['nfr']}\n\n"
        restrictions += f"**Como validar:** {r['validation']}\n\n"
    restrictions += "[Questões para o Cliente](Questões-para-o-Cliente) · [Rastreabilidade](Rastreabilidade) · [Home](Home)\n"
    questions = "# Questões para o Cliente\n\nQuestões ainda sem resposta registada. Priorizar no grupo antes de pedir confirmação ao cliente/professor.\n\n"
    questions += table(["ID", "Questão", "Itens relacionados"], [
        [q["id"], q["question"], ", ".join(q["related"])] for q in data["questions"]
    ]) + "\n[Voltar à Home](Home)\n"
    trace = "# Rastreabilidade\n\nRelação entre o pedido do cliente, as funcionalidades e as restrições. "
    trace += "Itens derivados e propostos mantêm a origem identificada nas suas páginas.\n\n"
    trace += table(["Necessidade do cliente", "Funcionalidades", "Restrições"], [
        [t["client_need"], ", ".join(t["functions"]) or "Análise de custo e prazo; sem função autónoma", ", ".join(t["constraints"])]
        for t in data["traceability"]
    ]) + "\n## Fora do âmbito imediato destas práticas\n\n"
    trace += "A implementação da aplicação, o orçamento detalhado, pagamento real, tecnologia de atualização em tempo real "
    trace += "e implantação são decisões posteriores. Esta documentação não afirma que essas tarefas já foram executadas.\n\n[Voltar à Home](Home)\n"
    return {
        "Home.md": home,
        "Lista-de-Utilizadores.md": users,
        "Lista-de-Funcionalidades.md": funcs,
        "restrições-do-sistema.md": restrictions,
        "Questões-para-o-Cliente.md": questions,
        "Rastreabilidade.md": trace,
        "_Sidebar.md": "## LAN Party 2026\n\n[Home](Home)\n\n" + navigation,
        "_Footer.md": "INF13204L · NEEI LAN Party 2026 · Proposta inicial sujeita a discussão e validação.\n",
    }


CSS = """
:root{color-scheme:light;--ink:#122333;--muted:#50616e;--paper:#fff;--line:#d8e0e5;--accent:#00695c}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}
body{margin:0;font:17px/1.6 system-ui,-apple-system,sans-serif;color:var(--ink);background:#f1f5f5}
header,main,footer{max-width:1100px;margin:auto;padding:24px}header{padding-top:42px}
h1{font-size:clamp(27px,4vw,43px);line-height:1.15;max-width:900px;margin:12px 0 20px}
h2{font-size:27px;margin-top:0}h3{font-size:20px;line-height:1.35;margin:0 0 12px}
p{margin:10px 0 16px}a{color:var(--accent);text-underline-offset:3px}a:focus,input:focus,summary:focus{outline:3px solid #eead25;outline-offset:4px}
nav{position:sticky;top:0;background:#122333;z-index:2;padding:12px 20px;display:flex;justify-content:center;gap:10px 22px;flex-wrap:wrap}nav a{color:white;font-size:15px}
.tag{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);font-weight:750}
.notice{border-left:5px solid #ca7c15;padding:14px 18px;background:#fff8e8;border-radius:6px}
.stats,.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:15px;margin:22px 0}
.stat,.card,section{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:24px}
.stat strong{display:block;font-size:28px;line-height:1.2}.stat span,.muted{color:var(--muted)}
section{margin-bottom:26px}section .card{margin:16px 0;border-radius:10px;padding:20px}
.badges{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}.badge{font-size:13px;border-radius:99px;padding:3px 10px;background:#e6f4ef;color:#155847;font-weight:700}
.badge.P{background:#fff0d3;color:#704513}.badge.D{background:#eaf0fc;color:#264272}
.source{white-space:pre-line;max-width:85ch}input{width:100%;padding:13px;border:1px solid #8b9da8;border-radius:8px;font:inherit}
details{border-top:1px solid var(--line);padding-top:10px;margin-top:12px}summary{cursor:pointer;font-weight:650;color:var(--accent)}
.table-wrap{overflow:auto}table{width:100%;border-collapse:collapse;font-size:15px}th,td{text-align:left;vertical-align:top;border-bottom:1px solid var(--line);padding:10px}th{background:#edf5f2}
ol,ul{padding-left:23px}li{margin-bottom:8px}.hidden{display:none!important}footer{font-size:14px;color:var(--muted)}
@media(max-width:600px){header,main,footer{padding:18px}section{padding:18px}.stats{grid-template-columns:repeat(2,1fr)}nav{position:static}body{font-size:16px}}
@media print{nav,.search{display:none}body{background:white}section,.card{break-inside:avoid}details>*{display:block}.hidden{display:block!important}}
"""


def offline_html(data: dict) -> str:
    e = html.escape
    names = {a["id"]: a["name"] for a in data["actors"]}

    def badge(source: str) -> str:
        labels = {"E": "E · Explícito", "D": "D · Derivado", "P": "P · Proposta"}
        return f'<span class="badge {source}" title="{e(data["evidence"][source])}">{labels[source]}</span>'

    def card(title: str, source: str, content: str, extra: str = "") -> str:
        return f'<article class="card searchable"><div class="badges">{badge(source)}</div><h3>{e(title)}</h3><p>{e(content)}</p>{extra}</article>'

    users = "".join(card(f"{a['id']} · {a['name']}", a["source"], a["description"], f'<p><strong>Acesso:</strong> {e(a["scope"])}</p>') for a in data["actors"])
    funcs = "".join(card(f"{f['id']} · {f['name']}", f["source"], f["description"],
        '<p><strong>Quem pode usar:</strong> ' + e("; ".join(f"{aid} — {names[aid]}" for aid in f["actors"])) + '</p>'
        + '<details><summary>Critério de revisão</summary><p>' + e(f["acceptance"]) + '</p></details>') for f in data["functions"])
    constraints = "".join(card(f"{r['id']} · {r['name']}", r["source"], r["description"],
        f'<p class="muted">{e(r["category"])}</p><details><summary>Requisito candidato e validação</summary>'
        f'<p><strong>Requisito candidato:</strong> {e(r["nfr"])}</p><p><strong>Como validar:</strong> {e(r["validation"])}</p></details>') for r in data["constraints"])
    questions = "".join(f'<article class="card searchable"><h3>{e(q["id"])}</h3><p>{e(q["question"])}</p><p class="muted">{e(", ".join(q["related"]))}</p></article>' for q in data["questions"])
    trace = "".join(f'<tr><td>{e(t["client_need"])}</td><td>{e(", ".join(t["functions"])) or "Análise de custo/prazo"}</td><td>{e(", ".join(t["constraints"]))}</td></tr>' for t in data["traceability"])
    return f'''<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LAN Party 2026 · MDS</title><style>{CSS}</style></head><body>
<header><div class="tag">Universidade de Évora · INF13204L</div><h1>LAN Party 2026<br>Utilizadores, funcionalidades e restrições</h1>
<p class="muted">Leitor offline das aulas práticas 1–3 · proposta para discussão</p>
<div class="notice"><strong>Preparado para revisão.</strong> Esta página é uma proposta. A formação do grupo, Education, 2FA, acesso do professor e publicação na Wiki ainda têm de ser verificados.</div>
<div class="stats"><div class="stat"><strong>{len(data['actors'])}</strong><span>papéis de utilizador</span></div><div class="stat"><strong>{len(data['functions'])}</strong><span>funcionalidades</span></div><div class="stat"><strong>{len(data['constraints'])}</strong><span>restrições</span></div><div class="stat"><strong>~5 000</strong><span>inscrições previstas</span></div></div></header>
<nav aria-label="Secções"><a href="#brief">Pedido</a><a href="#guide">English guide</a><a href="#users">Utilizadores</a><a href="#functions">Funcionalidades</a><a href="#constraints">Restrições</a><a href="#questions">Questões</a></nav>
<main><section id="brief"><h2>Pedido do cliente</h2><p class="source">{e(data['client_request'])}</p><p class="notice"><strong>~5 000 inscrições ≠ 5 000 acessos simultâneos.</strong> Preço, método de pagamento, público dos resultados e atraso máximo continuam em aberto.</p></section>
<section id="guide" lang="en"><h2>What you need to do</h2><div class="grid"><div><h3>1 · GitHub setup</h3><p>University email, student approval, 2FA, private personal repo and lecturer access.</p></div><div><h3>2 · Users and functions</h3><p>Work in a group of 2–3. Publish the client request, user list and function list in the native Wiki.</p></div><div><h3>3 · Constraints</h3><p>Publish the page titled <strong>restrições do sistema</strong>. Explain each condition and the quality requirement it suggests.</p></div></div>
<p><strong>User:</strong> who uses the software. <strong>Function:</strong> what they can do. <strong>Constraint:</strong> a condition that shapes the solution.</p><p>This reader does not replace the native GitHub Wiki. These exercises ask for requirements analysis; the complete application and GitHub Pages are not required by the provided instructions.</p></section>
<section class="search"><label for="search"><strong>Pesquisar propostas / search</strong></label><input id="search" type="search" placeholder="Ex.: pagamento, F20, tempo real" aria-describedby="search-count"><p id="search-count" aria-live="polite" class="muted">Todos os itens visíveis.</p>
<p>{badge('E')} {badge('D')} {badge('P')}</p><p class="muted">D e P necessitam de revisão. Os critérios de validação são propostas; não são compromissos aprovados pelo cliente.</p></section>
<section id="users"><h2>Lista de Utilizadores</h2><p>U04 aplica-se aos torneios atribuídos; U05 depende da aprovação de consulta pública.</p>{users}</section>
<section id="functions"><h2>Lista de Funcionalidades</h2>{funcs}</section>
<section id="constraints"><h2>restrições do sistema</h2>{constraints}</section>
<section id="questions"><h2>Questões para o Cliente</h2>{questions}</section>
<section id="trace"><h2>Rastreabilidade</h2><div class="table-wrap"><table><thead><tr><th>Necessidade</th><th>Funcionalidades</th><th>Restrições</th></tr></thead><tbody>{trace}</tbody></table></div></section></main>
<footer>Fonte: enunciados Moodle fornecidos em 2026-10-01. Conteúdo gerado a partir de data/project.json. Funciona sem internet.</footer>
<script>const input=document.querySelector('#search');const cards=[...document.querySelectorAll('.searchable')];const normalize=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();input.addEventListener('input',()=>{{const q=normalize(input.value.trim());let n=0;for(const c of cards){{const show=normalize(c.textContent).includes(q);c.classList.toggle('hidden',!show);if(show)n++}}document.querySelector('#search-count').textContent=`${{n}} de ${{cards.length}} itens visíveis.`}});</script>
</body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if checked-in Wiki files differ from generated source")
    args = parser.parse_args()
    data = json.loads((ROOT / "data/project.json").read_text(encoding="utf-8"))
    pages = wiki_pages(data)
    if args.check:
        mismatches = [name for name, content in pages.items() if not (ROOT / "wiki" / name).is_file() or (ROOT / "wiki" / name).read_text(encoding="utf-8") != content]
        if mismatches:
            raise SystemExit("Wiki files out of sync: " + ", ".join(mismatches) + ". Run python scripts/build_docs.py")
        print(f"OK: {len(pages)} Wiki files match data/project.json")
        return
    (ROOT / "wiki").mkdir(exist_ok=True)
    (ROOT / "build").mkdir(exist_ok=True)
    for name, content in pages.items():
        (ROOT / "wiki" / name).write_text(content, encoding="utf-8")
    (ROOT / "build/index.html").write_text(offline_html(data), encoding="utf-8")
    print(f"Built {len(pages)} Wiki files and build/index.html")


if __name__ == "__main__":
    main()
