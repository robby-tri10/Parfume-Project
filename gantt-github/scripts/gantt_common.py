"""Fungsi bersama untuk membaca config.json dan tasks.csv."""
import csv
import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def fmt_date(d: date) -> str:
    return f"{d.day} {BULAN[d.month - 1]} {d.year}"


def load_config() -> dict:
    with open(ROOT / "config.json", encoding="utf-8") as f:
        cfg = json.load(f)
    cfg.setdefault("timezone", "Asia/Jakarta")
    cfg.setdefault("label_terlambat", "terlambat")
    return cfg


def get_today(cfg: dict) -> date:
    """Tanggal hari ini. Bisa ditimpa dengan env GANTT_TODAY=YYYY-MM-DD untuk uji coba."""
    override = os.environ.get("GANTT_TODAY", "").strip()
    if override:
        return date.fromisoformat(override)
    return datetime.now(ZoneInfo(cfg["timezone"])).date()


def load_tasks(cfg: dict, today: date) -> list:
    start0 = date.fromisoformat(cfg["start_date"])
    tasks = []
    with open(ROOT / "tasks.csv", encoding="utf-8", newline="") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            try:
                s, e = int(row["minggu_mulai"]), int(row["minggu_selesai"])
                prog = int(row["progres"] or 0)
                bobot = float(row["bobot"] or 0)
            except (ValueError, KeyError) as err:
                raise SystemExit(f"tasks.csv baris {n}: data tidak valid ({err})")
            if not (1 <= s <= e <= 16):
                raise SystemExit(f"tasks.csv baris {n}: minggu harus 1 sampai 16 dan mulai <= selesai")
            if not (0 <= prog <= 100):
                raise SystemExit(f"tasks.csv baris {n}: progres harus 0 sampai 100")
            t = {
                "id": row["id"].strip(),
                "tipe": row["tipe"].strip().lower(),
                "fase": row["fase"].strip(),
                "task": row["task"].strip(),
                "pic": row["pic"].strip(),
                "s": s, "e": e,
                "progres": prog,
                "bobot": bobot,
                "start": start0 + timedelta(days=7 * (s - 1)),
                "end": start0 + timedelta(days=7 * e - 1),  # akhir minggu selesai (Minggu)
            }
            t["selesai"] = prog >= 100
            t["terlambat"] = t["tipe"] == "task" and not t["selesai"] and today > t["end"]
            tasks.append(t)
    return tasks
