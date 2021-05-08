# Parking Lot

 Проект позволяет вести учёт паркоместа на парковке

## Установка и запуск

Для установки и запуска требуется только интерпритатор Python 3

Запускается файл main.py

## Документация

После запуска программы предлагается запустить тестовую парковку с заданными значениями
Если нажать 1 то будет предложено вручную ввести параметры парковки, а именно:
 - Название парковки
 - Количество мест для Мотоциклов
 - Количество мест для Автомобилей
 - Количество мест для Автобусов
После отобразится меню выбора действий,
 -	Отобразить наличие свободных мест по каждому из типов
 -	Отобразить схему ячеек парковки (заняты или свободны в виде матрицы)
 -	Отобразить количество транспортных средств каждого вида, которые находятся на парковке
 -	Добавить транспорт на парковку
    * Необходимо будет выбрать какой транспорт добавить
   	   - Мотоцикл
   	   - Автомобиль
   	   - Автобус
 -	Убрать транспорт с парковки
    *	Необходимо будет выбрать какой транспорт добавить
          - Мотоцикл
   	      - Автомобиль
   	      - Автобус
   
## Пример для работы с программой

1.	Запустить
2.	Выбрать тестовую парковку введя «0»
3.	Выбрать пункт добавления транспорта введя «4»
4.	Выбрать Автомобиль введя «2»
  -	Отобразит что добавило 1 автомобиль
5.	Нажать Enter для продолжения
6.	Ещё раз пройти пункты 3, 4, 5
7.	Так же выполнить пункт 3, 4 
  -	Будет отображено сообщение что нет мест на парковке для автомобиля
8.	Нажать Enter для продолжения
9.	Выбрать пункт «2» для отображения схемы парковки
  -	Будет отображено где заняты места на парковке буквой «А»
10.	Нажать Enter для продолжения
11.	Выбрать пункт удаления транспорта с парковки введя «5»
12.	Выбрать вид транспорта автомобиль введя «2»
  -	Отобразит что удалило 1 автомобиль
13.	Нажать Enter для продолжения
14.	Выбрать пункт «2» для отображения схемы парковки
  -	Будет отображено где заняты места на парковке буквой «А»
  -	Видно что убрало машину с более приоритетного места
15.	Нажать Enter для продолжения
16.	Ввести «0» для завершения программы
