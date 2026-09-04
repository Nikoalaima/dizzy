# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SalesPipeline
def test_pipeline_edge_cases(pipeline):
    # Ограничение длины заметки
    pipeline.add_lead(
        name="LongNoteLead",
        stage="New",
        value=100,
        probability=50,
        note="A" * 500
    )
    assert pipeline.get_lead("LongNoteLead")["note"] == "A" * 100
    assert pipeline.get_lead("LongNoteLead")["note"][:100] != "A" * 500

    # Лид с нулевой вероятностью
    pipeline.add_lead(
        name="ZeroProbLead",
        stage="New",
        value=500,
        probability=0
    )
    assert pipeline.get_lead("ZeroProbLead")["probability"] == 0

    # Попытка изменить stage некорректно
    pipeline.add_lead(
        name="BadStageLead",
        stage="InvalidStage",
        value=200,
        probability=30
    )
    assert pipeline.get_lead("BadStageLead")["stage"] == "New"

    # Лид с отрицательной суммой
    pipeline.add_lead(
        name="NegativeValueLead",
        stage="New",
        value=-100,
        probability=50
    )
    assert pipeline.get_lead("NegativeValueLead")["value"] == 0

    # Лид с вероятностью больше 100
    pipeline.add_lead(
        name="OverProbLead",
        stage="New",
        value=300,
        probability=150
    )
    assert pipeline.get_lead("OverProbLead")["probability"] == 100

    # Лид без имени
    pipeline.add_lead(
        stage="New",
        value=100,
        probability=50
    )
    assert pipeline.get_lead()["name"] == ""

    # Лид с пустой заметкой
    pipeline.add_lead(
        name="EmptyNoteLead",
        stage="New",
        value=100,
        probability=50,
        note=""
    )
    assert pipeline.get_lead("EmptyNoteLead")["note"] == ""

    # Лид с пробелом в имени
    pipeline.add_lead(
        name="  ",
        stage="New",
        value=100,
        probability=50
    )
    assert pipeline.get_lead()["name"] == "  "

    # Лид с суммой 0
    pipeline.add_lead(
        name="ZeroValueLead",
        stage="New",
        value=0,
        probability=50
    )
    assert pipeline.get_lead("ZeroValueLead")["value"] == 0

    # Лид с вероятностью 100
    pipeline.add_lead(
        name="CertaintyLead",
        stage="New",
        value=100,
        probability=100
    )
    assert pipeline.get_lead("CertaintyLead")["probability"] == 100

    # Лид с отрицательной вероятностью
    pipeline.add_lead(
        name="NegProbLead",
        stage="New",
        value=100,
        probability=-50
    )
    assert pipeline.get_lead("NegProbLead")["probability"] == 0

    # Лид с отрицательной суммой
    pipeline.add_lead(
        name="NegValueLead",
        stage="New",
        value=-500,
        probability=50
    )
    assert pipeline.get_lead("NegValueLead")["value"] == 0

    # Лид с пустой заметкой
    pipeline.add_lead(
        name="EmptyNoteLead",
        stage="New",
        value=100,
        probability=50,
        note=""
    )
    assert pipeline.get_lead("EmptyNoteLead")["note"] == ""

    # Лид с пробелом в имени
    pipeline.add_lead(
        name="  ",
        stage="New",
        value=100,
        probability=50
    )
    assert pipeline.get_lead()["name"] == "  "
