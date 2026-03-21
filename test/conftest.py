import pytest

# Переменная для хранения имени текущего файла, чтобы не дублировать заголовки
last_file = None

def pytest_runtest_logreport(report):
    global last_file
    
    # Нас интересует только этап 'call' (выполнение самого теста)
    if report.when == 'call':
        # Извлекаем путь к файлу и название теста
        file_path = report.nodeid.split("::")[0]
        test_name = report.nodeid.split("::")[-1]
        
        # Если мы перешли к новому файлу, печатаем его название
        if file_path != last_file:
            print(f"\n\n📂 [FILE]: {file_path}")
            print("-" * 40)
            last_file = file_path
        
        # Определяем статус для наглядности
        status = "✅ PASSED" if report.passed else "❌ FAILED"
        if report.skipped:
            status = "⚠️ SKIPPED"

        # Печатаем результат конкретной функции теста
        print(f"  test: {test_name} -> {status}")

        # Если тест упал, можно вывести краткий лог ошибки прямо здесь
        if report.failed:
            print(f"    Error: {report.longreprtext.splitlines()[-1]}")

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Финальное общее сообщение после всех групп"""
    terminalreporter.ensure_newline()
    terminalreporter.section("ЗАВЕРШЕНИЕ ТЕСТИРОВАНИЯ", sep="=")
    if exitstatus == 0:
        print("🚀 Все группы тестов успешно пройдены!")
    else:
        print("🔍 Проверьте отчеты выше, есть ошибки в функциях.")