#!/usr/bin/env python3
"""Membuat GANTT.md (diagram Mermaid) dari tasks.csv dan menandai task yang terlambat.

Opsional: jika README.md memuat penanda
    <!-- GANTT:START -->  ...  <!-- GANTT:END -->
isi di antaranya ikut diperbarui.
"""
import re
from datetime import timedelta

from gantt_common import ROOT, fmt_date, get_today, load_config, load_tasks


def clean(text: str) -> str:
    """Mermaid gantt tidak suka karakter : ; # , di judul task."""
    text = text.replace(":", " -").replace(";", " ").replace("#", "").replace(",", " ")
    return re.sub(r"\s+", " ", text).strip()


def mermaid(tasks, today) -> str:
    lines = [
        "```mermaid",
        "gantt",
        "    dateFormat YYYY-MM-DD",
        "    axisFormat %d/%m",
        "    todayMarker stroke-width:3px,stroke:#d73a4a,opacity:0.7",
    ]
    section = None
    for t in tasks:
        if t["fase"] != section:
            section = t["fase"]
            lines.append(f"    section {clean(section)}")
        tid = "t" + re.sub(r"\W", "_", t["id"])
        start = t["start"]
        end_excl = t["end"] + timedelta(days=1)
        name = clean(t["task"])
        if t["tipe"] == "milestone":
            lines.append(f"    {name} :milestone, {tid}, {start}, 0d")
            continue
        if t["selesai"]:
            tag = "done, "
        elif t["terlambat"]:
            tag = "crit, "
        elif t["start"] <= today <= t["end"] or t["progres"] > 0:
            tag = "active, "
        else:
            tag = ""
        lines.append(f"    {name} :{tag}{tid}, {start}, {end_excl}")
    lines.append("```")
    return "\n".join(lines)


def summary(tasks, today) -> str:
    real = [t for t in tasks if t["tipe"] == "task"]
    total_w = sum(t["bobot"] for t in real)
    prog_w = sum(t["bobot"] * t["progres"] for t in real) / total_w if total_w else 0
    prog_avg = sum(t["progres"] for t in real) / len(real) if real else 0
    done = sum(t["selesai"] for t in real)
    late = [t for t in real if t["terlambat"]]
    out = [
        f"**Diperbarui:** {fmt_date(today)} (otomatis oleh GitHub Actions)",
        "",
        f"- Task selesai: **{done} dari {len(real)}**",
        f"- Progres rata-rata semua task: **{prog_avg:.0f}%**",
        f"- Progres tertimbang bobot nilai: **{prog_w:.0f}%**",
        f"- Task terlambat: **{len(late)}**",
    ]
    return "\n".join(out)


def late_table(tasks, today) -> str:
    late = [t for t in tasks if t["terlambat"]]
    if not late:
        return "Tidak ada task yang melewati deadline."
    rows = ["| ID | Task | PIC | Deadline | Terlambat | Progres |", "|---|---|---|---|---|---|"]
    for t in sorted(late, key=lambda x: x["end"]):
        days = (today - t["end"]).days
        task = t["task"].replace("|", "/")
        pic = t["pic"].replace("|", "/")
        rows.append(f"| {t['id']} | {task} | {pic} | {fmt_date(t['end'])} | {days} hari | {t['progres']}% |")
    return "\n".join(rows)


def main():
    cfg = load_config()
    today = get_today(cfg)
    tasks = load_tasks(cfg, today)

    block = "\n\n".join([
        summary(tasks, today),
        mermaid(tasks, today),
        "### Task terlambat\n\n" + late_table(tasks, today),
    ])

    (ROOT / "GANTT.md").write_text("# Gantt Chart Proyek\n\n" + block + "\n", encoding="utf-8")
    print(f"GANTT.md diperbarui ({len(tasks)} baris, hari ini {today})")

    readme = ROOT / "README.md"
    if readme.exists():
        txt = readme.read_text(encoding="utf-8")
        pat = re.compile(r"(<!-- GANTT:START -->)(.*?)(<!-- GANTT:END -->)", re.S)
        if pat.search(txt):
            new = pat.sub(lambda m: f"{m.group(1)}\n{block}\n{m.group(3)}", txt)
            if new != txt:
                readme.write_text(new, encoding="utf-8")
                print("README.md diperbarui")


if __name__ == "__main__":
    main()
