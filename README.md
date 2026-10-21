# music-shop
# Информационная система музыкального магазина

## 1. Назначение проекта

Данный проект представляет собой информационную систему для автоматизации работы музыкального магазина.

Система предназначена для хранения информации о музыкальных инструментах, поиска и управления товарами, оформления продаж и формирования чеков.

Проект разработан в рамках лабораторной работы по проектированию и разработке информационной системы.

---

## 2. Основные функциональные возможности

Система предоставляет следующие возможности:

- добавление музыкальных инструментов;
- поиск товара по артикулу;
- изменение информации о товаре;
- удаление товара;
- хранение информации о товарах в базе данных SQLite;
- работа со складом;
- работа с магазином;
- оформление продажи;
- формирование чека;
- указание способа оплаты;
- сохранение чека в формате `.xlsx`;
- управление товарами через графический интерфейс;
- автоматическое тестирование программных функций.

---

## 3. Предметная область

Основной объект системы — музыкальный инструмент.

В системе предусмотрены различные виды музыкальных инструментов:

- струнные;
- ударные;
- клавишные.

Также система содержит следующие основные сущности:

- музыкальный инструмент;
- склад;
- магазин;
- продавец;
- чек.

---

## 4. Архитектура проекта

Проект имеет модульную слоистую структуру.

```text
music-shop/
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── src/
│   └── music_shop/
│       ├── models/
│       │   ├── instrument.py
│       │   ├── string_instrument.py
│       │   ├── percussion_instrument.py
│       │   ├── keyboard_instrument.py
│       │   ├── warehouse.py
│       │   ├── store.py
│       │   ├── seller.py
│       │   └── receipt.py
│       │
│       ├── services/
│       │   ├── instrument_service.py
│       │   ├── product_service.py
│       │   ├── store_service.py
│       │   ├── warehouse_service.py
│       │   └── receipt_service.py
│       │
│       ├── database/
│       │   └── database.py
│       │
│       ├── repositories/
│       │   └── instrument_repository.py
│       │
│       └── ui/
│           └── main.py
│
├── tests/
|     ├── test_database.py
|     ├── test_instrument.py
|     ├── test_instrument_repository.py
|     ├── test_instrument_service.py
|     ├── test_keyboard_instrument.py
|     ├── test_percussion_instrument.py
|     ├── test_product_service.py
|     ├── test_receipt.py
|     ├── test_receipt_service.py
|     ├── test_seller.py
|     ├── test_store.py
|     ├── test_store_service.py
|     ├── test_string_instrument.py
|     ├── test_ui.py
|     ├── test_warehouse.py
|     └── test_warehouse_service.py
|
├── requirements.txt
├── README.md
├── LICENSE
├── music_shop.db
└── .gitignore
