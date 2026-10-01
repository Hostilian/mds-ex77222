#!/usr/bin/env python3
"""Validate requirements references, access declarations and local documentation links."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_docs import ROOT, wiki_pages


def validate(data: dict) -> list[str]:
    errors = []
    groups = {"actors": "U", "external_systems": "S", "functions": "F", "constraints": "R", "questions": "Q"}
    ids = {}
    for group, prefix in groups.items():
        items = data.get(group, [])
        if not items:
            errors.append(f"{group}: empty list")
        values = [item.get("id", "") for item in items]
        ids[group] = set(values)
        for item_id, count in Counter(values).items():
            if count > 1:
                errors.append(f"{group}: duplicate ID {item_id}")
            if not re.fullmatch(prefix + r"\d{2,}", item_id):
                errors.append(f"{group}: invalid ID {item_id!r}")
        for item in items:
            if group != "questions" and item.get("source") not in data["evidence"]:
                errors.append(f"{item.get('id')}: unknown evidence code")
            if group != "questions" and not item.get("description", "").strip():
                errors.append(f"{item.get('id')}: description missing")
    for function in data.get("functions", []):
        roles = function.get("actors", [])
        if not roles or len(roles) != len(set(roles)):
            errors.append(f"{function['id']}: access roles missing or duplicated")
        unknown = set(roles) - ids["actors"]
        if unknown:
            errors.append(f"{function['id']}: undefined human roles {sorted(unknown)}")
        if not function.get("acceptance", "").strip():
            errors.append(f"{function['id']}: review criterion missing")
    for actor in data.get("actors", []):
        if not actor.get("scope", "").strip():
            errors.append(f"{actor['id']}: access scope missing")
    for restriction in data.get("constraints", []):
        for field in ["category", "nfr", "validation"]:
            if not restriction.get(field, "").strip():
                errors.append(f"{restriction['id']}: {field} missing")
    for question in data.get("questions", []):
        if not question.get("question", "").strip():
            errors.append(f"{question['id']}: question missing")
        unknown = set(question.get("related", [])) - (ids["functions"] | ids["constraints"])
        if unknown:
            errors.append(f"{question['id']}: undefined references {sorted(unknown)}")
    traced = set()
    for trace in data.get("traceability", []):
        if not trace.get("client_need", "").strip():
            errors.append("Traceability: client need missing")
        for field in ["functions", "constraints"]:
            unknown = set(trace.get(field, [])) - ids[field]
            if unknown:
                errors.append(f"Traceability: undefined {field} {sorted(unknown)}")
        traced.update(trace.get("functions", []))
    for function in data.get("functions", []):
        if function["source"] == "E" and function["id"] not in traced:
            errors.append(f"{function['id']}: explicit client requirement has no traceability")
    return errors


def links_and_sync(data: dict) -> list[str]:
    errors = []
    expected = wiki_pages(data)
    for name, content in expected.items():
        path = ROOT / "wiki" / name
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            errors.append(f"Wiki source out of sync: {name}")
    paths = [ROOT / "README.md", *(ROOT / "docs").glob("*.md"), *(ROOT / "wiki").glob("*.md")]
    for path in paths:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\s)]+)\)", content):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            local = unquote(parts.path)
            resolved = path.parent / local
            if path.parent.name == "wiki" and not resolved.suffix:
                resolved = resolved.with_suffix(".md")
            if not resolved.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")
    home = expected["Home.md"]
    for label in ["Lista de Utilizadores", "Lista de Funcionalidades", "restrições do sistema"]:
        if f"[{label}]" not in home:
            errors.append(f"Home: assignment link missing: {label}")
    if data["client_request"] not in home:
        errors.append("Home: client request not preserved")
    if not expected["restrições-do-sistema.md"].startswith("# restrições do sistema\n"):
        errors.append("Constraint page: exact title missing")
    return errors


def main() -> None:
    try:
        data = json.loads((ROOT / "data/project.json").read_text(encoding="utf-8"))
        errors = validate(data) + links_and_sync(data)
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise SystemExit(f"Validation failed: {exc}") from exc
    if errors:
        print("Validation failed:\n" + "\n".join("- " + item for item in errors))
        sys.exit(1)
    print(f"OK: {len(data['actors'])} roles, {len(data['functions'])} functions, {len(data['constraints'])} constraints, "
          f"{len(data['questions'])} questions; IDs, access roles, traceability, local links and Wiki source match")


if __name__ == "__main__":
    main()
