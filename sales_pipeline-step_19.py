# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SalesPipeline
def archive_lead(lead_id, reason=None):
    """Archive a completed or stale lead. Returns the archived record dict."""
    if lead_id not in LEADS:
        print(f"WARNING: Lead {lead_id} not found — skipping archive.")
        return None
    lead = dict(LEADS[lead_id])
    lead['archived'] = True
    lead['archive_date'] = datetime.now().isoformat()
    if reason is None:
        stage = LEAD_STAGES.get(lead.get('stage', 0), 'Unknown')
        reason = f"Auto-archived after reaching stage '{stage}'"
    lead['archive_reason'] = reason
    del LEADS[lead_id]
    ARCHIVED_LEADS.append(lead)
    print(f"Archived lead {lead_id} ({reason[:40]}...)")
    return lead

def list_archives():
    """Return a summary table of all archived leads."""
    if not ARCHIVED_LEADS:
        print("No archived records yet.")
        return []
    rows = [f"{i+1:>3} | {a['id']:>6} | {a.get('archive_date','?')[:10]} | {a.get('archive_reason','')}".split('|')]
    for a in ARCHIVED_LEADS:
        rows.append(f"{a['id']} | {a.get('archive_date','?')[:10]} | {a.get('archive_reason','')}")
    print("Archived leads:")
    return rows
