Приложение для регистрации пользователей:
Настроен workflow в GitHub Actions, 
который автоматически запускается при каждом коммите в ветку main.

Этапы workflow: 
1) сборка приложения, 
2) проверка качества кода (с помощью flake8), 
3) запуск автоматических тестов, 
4) автоматическое развертывание приложения на сервере 
при успешном прохождении предыдущих этапов.

Реализация логирования в приложении:
Внедрена система логирования с использованием модуля logging.
Настроены различные уровни логирования (DEBUG, INFO, CRITICAL).
Логи ошибок и критических событий сохраняются в app.log.
Реализуйте ротацию логов для предотвращения переполнения дискового пространства.
