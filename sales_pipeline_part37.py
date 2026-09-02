# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SalesPipeline
import unittest

class TestSalesPipeline(unittest.TestCase):
    def test_lead_creation(self):
        from salespipeline import SalesPipeline
        sp = SalesPipeline()
        sp.add_lead("Test Corp", "John", 100000, 0.5)
        leads = sp.get_leads()
        self.assertEqual(len(leads), 1)
        self.assertEqual(leads[0]["name"], "Test Corp")
        self.assertEqual(leads[0]["contact"], "John")
        self.assertEqual(leads[0]["amount"], 100000)
        self.assertEqual(leads[0]["probability"], 0.5)

    def test_add_stage(self):
        from salespipeline import SalesPipeline
        sp = SalesPipeline()
        sp.add_stage("Prospecting", 0.1)
        stages = sp.get_stages()
        self.assertEqual(len(stages), 1)
        self.assertEqual(stages[0]["name"], "Prospecting")
        self.assertEqual(stages[0]["probability"], 0.1)

    def test_add_note(self):
        from salespipeline import SalesPipeline
        sp = SalesPipeline()
        sp.add_note("Test Corp", "Initial contact made")
        notes = sp.get_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["lead_name"], "Test Corp")
        self.assertEqual(notes[0]["content"], "Initial contact made")

    def test_pipeline_report(self):
        from salespipeline import SalesPipeline
        sp = SalesPipeline()
        sp.add_lead("A", "a", 50000, 0.2)
        sp.add_lead("B", "b", 75000, 0.3)
        sp.add_lead("C", "c", 120000, 0.5)
        report = sp.get_report()
        self.assertIn("Total Leads", report)
        self.assertIn("Total Amount", report)
        self.assertIn("Total Probability", report)
        self.assertIn("Expected Revenue", report)
        self.assertEqual(report["Total Leads"], 3)
        self.assertEqual(report["Total Amount"], 245000)
        self.assertEqual(report["Total Probability"], 1.0)
        self.assertEqual(report["Expected Revenue"], 122500)

if __name__ == "__main__":
    unittest.main()
