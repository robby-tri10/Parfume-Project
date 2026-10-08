#!/usr/bin/env python3
"""Memberi/mencabut label 'terlambat' pada GitHub Issue sesuai deadline di tasks.csv.

Cara mencocokkan: judul issue diawali ID task, contoh "[1.1] Membentuk tim dan membagi peran".

Pemakaian:
    python scripts/sync_issues.py              # sinkron label (butuh GITHUB_TOKEN dan GITHUB_REPOSITORY)
    python scripts/sync_issues.py --create     # sekaligus membuat issue untuk task yang belum punya issue
    python scripts/sync_issues.py --dry-run    # hanya mencetak apa yang akan dilakukan, tanpa API
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from gantt_common import fmt_date, get_today, load_config, load_tasks

API = "https://api.github.com"
ID_RE = re.compile(r"^\s*\[([^\]]+)\]")


def call(method, path, token, body=None, ok_404=False):
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(body).encode("utf-8") if body is not None else None,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "gantt-deadline-bot",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as err:
        if err.code == 404 and ok_404:
            return None
        detail = err.read().decode("utf-8", "replace")
        raise SystemExit(f"GitHub API {method} {path} gagal ({err.code}): {detail}")


def list_issues(repo, token):
    """Semua issue (open dan closed), tanpa pull request. Satu ID dipetakan ke satu issue."""
    found, page = {}, 1
    while True:
        batch = call("GET", f"/repos/{repo}/issues?state=all&per_page=100&page={page}", token)
        for it in batch:
            if "pull_request" in it:
                continue
            m = ID_RE.match(it["title"])
            if not m:
                continue
            tid = m.group(1).strip()
            # utamakan issue yang masih open bila ada judul ganda
            if tid not in found or (found[tid]["state"] != "open" and it["state"] == "open"):
                found[tid] = it
        if len(batch) < 100:
            return found
        page += 1


def ensure_label(repo, token, name):
    if call("GET", f"/repos/{repo}/labels/{urllib.parse.quote(name)}", token, ok_404=True) is None:
        call("POST", f"/repos/{repo}/labels", token, {
            "name": name, "color": "d73a4a",
            "description": "Task melewati deadline di tasks.csv"})
        print(f"Label '{name}' dibuat")


def issue_body(t):
    return (
        f"**Fase:** {t['fase']}\n"
        f"**PIC (peran):** {t['pic']}\n"
        f"**Jadwal:** Minggu {t['s']} sampai {t['e']} "
        f"({fmt_date(t['start'])} sampai {fmt_date(t['end'])})\n"
        f"**Deadline:** {fmt_date(t['end'])}\n"
        f"**Bobot nilai:** {t['bobot']:g}%\n\n"
        "Progres diperbarui di `tasks.csv`. Label `terlambat` dipasang dan dicabut otomatis."
    )


def main():
    args = set(sys.argv[1:])
    create = "--create" in args or os.environ.get("CREATE_ISSUES", "").lower() == "true"
    dry = "--dry-run" in args

    cfg = load_config()
    today = get_today(cfg)
    label = cfg["label_terlambat"]
    tasks = [t for t in load_tasks(cfg, today) if t["tipe"] == "task"]
    late = [t for t in tasks if t["terlambat"]]

    print(f"Hari ini {today}. Task terlambat: {len(late)} dari {len(tasks)}")
    for t in late:
        print(f"  [{t['id']}] {t['task']} (deadline {t['end']}, progres {t['progres']}%)")

    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if dry or not token or not repo:
        print("Mode dry-run atau token/repo tidak tersedia: tidak ada perubahan ke GitHub.")
        return

    ensure_label(repo, token, label)
    issues = list_issues(repo, token)

    if create:
        for t in tasks:
            if t["id"] in issues:
                continue
            new = call("POST", f"/repos/{repo}/issues", token, {
                "title": f"[{t['id']}] {t['task']}",
                "body": issue_body(t),
                "labels": [t["fase"].split(" - ")[0].lower().replace(" ", "-")],
            })
            issues[t["id"]] = new
            print(f"Issue dibuat: #{new['number']} [{t['id']}]")
            time.sleep(1.5)  # hindari secondary rate limit

    for t in tasks:
        iss = issues.get(t["id"])
        if not iss:
            continue
        names = {l["name"] for l in iss.get("labels", [])}
        should = t["terlambat"] and iss["state"] == "open"
        has = label in names
        num = iss["number"]
        if should and not has:
            call("POST", f"/repos/{repo}/issues/{num}/labels", token, {"labels": [label]})
            days = (today - t["end"]).days
            call("POST", f"/repos/{repo}/issues/{num}/comments", token, {
                "body": f"Task ini melewati deadline **{fmt_date(t['end'])}** ({days} hari) "
                        f"dan progresnya baru {t['progres']}%. Label `{label}` dipasang otomatis."})
            print(f"Label dipasang: #{num} [{t['id']}]")
        elif has and not should:
            call("DELETE", f"/repos/{repo}/issues/{num}/labels/{urllib.parse.quote(label)}", token, ok_404=True)
            print(f"Label dicabut: #{num} [{t['id']}]")


if __name__ == "__main__":
    main()
