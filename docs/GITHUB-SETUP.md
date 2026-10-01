# Configuração do GitHub / GitHub setup

## Prática 1

1. Use the intended existing account, currently `Hostilian`, unless the teacher asks for a different account.
2. In [email settings](https://github.com/settings/emails), add your University email and verify it through the verification email. Its status cannot be established from the connector's public profile email.
3. In [password and authentication settings](https://github.com/settings/security), enable two-factor authentication with your own authenticator, security key or another supported method. Save recovery codes privately. This step needs the account owner.
4. Use the University network as the teacher requests. At [GitHub Education](https://github.com/settings/education/benefits), follow the current application flow, choose the University and submit current student evidence if requested. Do not upload student ID or enrollment evidence to the repository.
5. Create **`mds-ex77222`** with **Private** visibility. The student identifier is taken from the provided University account context; confirm it against the student portal if necessary.
6. Add the exact username **`pedrosalgueiro`** through **Settings → Collaborators / Manage access**. Check that the selected account is the lecturer Pedro Salgueiro. Keep invitation state separate from accepted access.

If the repository is public: **Settings → General → Danger Zone → Change repository visibility → Private**. The connector cannot make that change.

## Prática 2 — grupo

- Form a group of 2 or 3 students and collect each member's GitHub username.
- The group project is created by one member only. Confirm whether the group should use this Practice 1 repository or another group member's existing project.
- Add every member as a collaborator with the agreed editing access. Record actual members and decisions in `docs/TEAM.md`.
- All members review and discuss the content. The prepared proposal is not evidence of completed group discussion.

## Native Wiki publication — browser method

Wiki files are kept in a separate Git repository from ordinary project files. They must be published to the actual **Wiki** tab to meet the Moodle instructions.

| Page title in GitHub | Prepared source file |
| --- | --- |
| Home | `wiki/Home.md` |
| Lista de Utilizadores | `wiki/Lista-de-Utilizadores.md` |
| Lista de Funcionalidades | `wiki/Lista-de-Funcionalidades.md` |
| restrições do sistema | `wiki/restrições-do-sistema.md` |
| Questões para o Cliente | `wiki/Questões-para-o-Cliente.md` |
| Rastreabilidade | `wiki/Rastreabilidade.md` |

Open the repository's **Wiki** tab, create the Home page, paste `wiki/Home.md`, and save. Add the remaining pages with the exact titles above. The final two pages are useful supporting material. Open every Home link afterward. If manually editing Wiki content, copy those changes back to `data/project.json` and regenerate to keep the source consistent.

For a private repository, the Wiki feature requires a compatible plan (GitHub Pro, Team or Enterprise). Check the current account benefits and repository settings. Do not make the required private repository public just to unlock its Wiki; ask the teacher how to proceed while Education verification is pending.

## Native Wiki publication — local Git method

After creating the first Wiki page in GitHub, use an authenticated Git installation:

```sh
git clone https://github.com/Hostilian/mds-ex77222.wiki.git
```

Copy only the reviewed files from this package's `wiki/` folder into that clone. Inspect the diff and keep any existing group content that should remain. Commit and push to the Wiki's existing default branch. Never put a password or token into a command URL. Use GitHub Desktop, SSH or a credential manager for authentication.

Files with hyphens map to Wiki titles containing spaces. The constraints filename preserves the required lower-case title and accents. The underscore files are GitHub's optional sidebar and footer.

## GitHub Pages

Pages is optional and absent from the supplied assessment instructions. This package generates an offline HTML reading page instead of publishing it. GitHub Pages sites are generally public even when the repository is private. Decide on public presentation only after the coursework privacy and group arrangements are settled.

## Upload the repository package

This package can be committed through GitHub Desktop or uploaded with the connected GitHub file tools. Include `data/`, `wiki/`, `docs/`, `scripts/`, `.github/`, `README.md` and `.gitignore`. The GitHub Actions workflow builds its own `build/` folder, so it does not need to be committed.

After a successful check on GitHub, download the `mds-documentation` artifact from that run and open `build/index.html`. Verify the native Wiki separately: a successful docs pipeline does not prove that the Wiki was published.

## Official references (checked 2026-10-01)

- [Apply for GitHub Education](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)
- [About wikis and supported plans](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
- [Adding/editing Wiki pages and cloning](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages)
- [GitHub Pages visibility](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
