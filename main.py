import json
from collections import defaultdict

def total_revenue(purchases_list):
    """Рассчитайте и верните общую выручку (цена * количество для всех записей)."""
    total = 0
    for purchase in purchases_list:
        total += purchase["price"] * purchase["quantity"]
    return total

def items_by_category(purchases_list):
    """Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории."""
    categories_map = defaultdict(set)
    for purchase in purchases_list:
        categories_map[purchase["category"]].add(purchase["item"])
    
    result_map = {category: sorted(list(items)) for category, items in categories_map.items()}
    return result_map

def expensive_purchases(purchases_list, min_price):
    """Выведите все покупки, где цена товара больше или равна min_price."""
    expensive_items = []
    for purchase in purchases_list:
        if purchase["price"] >= min_price:
            expensive_items.append(purchase)
    return expensive_items

def average_price_by_category(purchases_list):
    """Рассчитайте среднюю цену товаров по каждой категории."""
    category_prices_list = defaultdict(list)
    for purchase in purchases_list:
        category_prices_list[purchase["category"]].append(purchase["price"])

    avg_prices = {}
    for category, prices in category_prices_list.items():
        if prices:
            avg_prices[category] = round(sum(prices) / len(prices), 2)
    return avg_prices

def most_frequent_category(purchases_list):
    """Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity)."""
    category_quantities = defaultdict(int)
    for purchase in purchases_list:
        category_quantities[purchase["category"]] += purchase["quantity"]
    
    if not category_quantities:
        return None

    most_frequent = max(category_quantities, key=category_quantities.get)
    return most_frequent

	
# --- Функция для загрузки данных из файла ---
def load_purchases_from_file(file_path="./purchases.json"):
    """Загружает список покупок из JSON файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            purchases_data = json.load(f)
        # Простая валидация, что это список словарей
        if not isinstance(purchases_data, list):
            print(f"Ошибка: Данные в файле '{file_path}' не являются списком.")
            return []
        for item in purchases_data:
            if not isinstance(item, dict):
                print(f"Ошибка: Элемент в файле '{file_path}' не является словарем.")
                return []
        return purchases_data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return [] # Возвращаем пустой список, если файл не найден
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON из файла '{file_path}'. Проверьте формат файла.")
        return [] # Возвращаем пустой список при ошибке парсинга
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при чтении файла: {e}")
        return []

# --- Основной блок выполнения ---
if __name__ == "__main__":
    PURCHASES_FILE_PATH = "purchases.json"
    purchases = load_purchases_from_file(PURCHASES_FILE_PATH)

    if not purchases:
        print("Нет данных для анализа. Завершение работы.")
    else:
       # print(f"Анализ данных из файла: {PURCHASES_FILE_PATH}\n")

        # Анализ и вывод результатов
        print(f"Общая выручка: {total_revenue(purchases)}")

        items_cat = items_by_category(purchases)
        print(f"Товары по категориям: {items_cat}")

        min_p = 1.0
        exp_purchases = expensive_purchases(purchases, min_p)
        print(f"Покупки дороже {min_p}: {exp_purchases}")

        avg_price_cat = average_price_by_category(purchases)
        print(f"Средняя цена по категориям: {avg_price_cat}")

        most_freq_cat = most_frequent_category(purchases)
        print(f"Категория с наибольшим количеством проданных товаров: {most_freq_cat}")

