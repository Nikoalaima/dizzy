# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: SalesPipeline
import argparse

def main():
    parser = argparse.ArgumentParser(description="SalesPipeline CLI")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a lead")
    p_add.add_argument("name")
    p_add.add_argument("--stage", default="New")
    p_add.add_argument("--amount", type=float, default=0.0)
    p_add.add_argument("--probability", type=int, default=10)
    p_add.add_argument("--note", default="")

    p_view = sub.add_parser("view", help="View all leads")

    p_export = sub.add_parser("export", help="Export to CSV")

    args = parser.parse_args()
    if args.command == "add":
        add_lead(args.name, args.stage, args.amount, args.probability, args.note)
    elif args.command == "view":
        view_leads()
    elif args.command == "export":
        export_leads()
