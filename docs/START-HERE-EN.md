# Start here — Practices 1, 2 and 3

## What the teacher wants

| Practice | Deliverable | What you need to understand |
| --- | --- | --- |
| 1 | University email on GitHub, student verification, 2FA, a private `mds-ex77222` repo, and collaborator `pedrosalgueiro` | Set up the place where your work is shared. |
| 2 | A group of 2–3, one project creator, all members added, and native Wiki pages for the client request, users and functions | Who uses the software, and what can each person do? |
| 3 | Native Wiki page called **restrições do sistema** | What limits or quality conditions must the software respect? |

The Moodle instructions say no online assignment submission is required. That does not remove the GitHub/Wiki work or the teacher's review.

## The project in one minute

NEEI wants software for a **2026 LAN Party** with **about 5,000 expected event registrations**. It should manage event registrations, possible payments for people outside the University, registrations in multiple tournaments, and tournament results during and after each tournament.

These are requirements-analysis tasks. You are not yet required by these three instructions to implement the full app, charge people, estimate a made-up price or deploy GitHub Pages.

## Read these four things

1. `wiki/Home.md`: the exact client request and page links.
2. `wiki/Lista-de-Utilizadores.md`: who uses the system.
3. `wiki/Lista-de-Funcionalidades.md`: unique function IDs, short descriptions and access roles.
4. `wiki/restrições-do-sistema.md`: constraints, their sources and how to turn them into quality requirements.

**E** = explicit in the brief. **D** = inferred to support the brief; discuss with the client. **P** = extra proposal, still awaiting approval.

## Five points you can explain in class

- A **user** is a person interacting with the software, such as a participant or organiser.
- A **function** is an action: registering for a tournament, recording a result, or checking results.
- A **constraint** is a condition or limitation: expected registration volume, who may access private data, or how promptly results must update.
- **5,000 expected registrations** is not a hard capacity limit and does not mean 5,000 simultaneous users.
- **Possible payments for external participants** does not mean every external participant must pay, or that University participants are guaranteed free entry. Ask about the policy.

## Useful Portuguese sentences

**Sou estudante Erasmus e ainda estou a aprender português.**

I am an Erasmus student and I am still learning Portuguese.

**Ainda não tenho grupo. Posso juntar-me a um grupo de dois alunos?**

I do not have a group yet. Can I join a group of two students?

**Preparei uma proposta de utilizadores, funcionalidades e restrições para discutirmos.**

I prepared a proposal for users, functions and constraints for us to discuss.

**Os resultados devem ser públicos ou apenas visíveis para os participantes?**

Should results be public or only visible to participants?

**Qual é o atraso máximo aceitável para os resultados em tempo real?**

What is the maximum acceptable delay for live results?

## Still needs real action

- Form or join a group of **2–3 students**. Do not claim that group discussion has happened until it has.
- Add your University email to the existing GitHub account and verify it. Ask the teacher whether this satisfies the instruction to register with the University email; do not create a second account automatically.
- Enable 2FA yourself and save recovery codes securely. Never commit them.
- Apply for GitHub Education using current student evidence and the University network as instructed. Application submitted and application approved are different states.
- Make the Practice 1 repository **private** and add `pedrosalgueiro` as a collaborator. An invitation must be accepted to provide active access.
- Agree which repository is the single group project. If a group member already created one, use that project rather than creating duplicate group projects.
- Publish the prepared pages in the **native Wiki** and verify its links. Files in the ordinary repository are backups/source, not the native Wiki itself.
- Discuss the proposed roles, functions and constraints with your teammates and revise them.

## Pipeline

Run `python scripts/build_docs.py` then `python scripts/validate.py`. The GitHub Actions workflow runs these checks, builds an offline reading page, and packages the Wiki as an artifact. No Docker or paid services are needed for this documentation-only work.
