import pandas as pd
import os

def load_game_data(file_name="games_full.csv"):
    """
    Загружает данные из CSV-файла.

    Args:
        file_name (str): Имя CSV-файла с данными.

    Returns:
        pd.DataFrame: Загруженные данные в виде DataFrame, или None в случае ошибки.
    """
    # Определяем базовую директорию текущего скрипта
    script_dir = os.path.dirname(__file__)
    #  Project_GameDataAnalysis/data/

    data_path = os.path.join(script_dir, "data", file_name)

    if not os.path.exists(data_path):
        print(f"Ошибка: Файл '{data_path}' не найден. Убедитесь, что он находится в папке 'data' внутри Project_GameDataAnalysis.")
        return None

    try:
        df = pd.read_csv(data_path)
        print(f"Данные '{file_name}' успешно загружены. Количество строк: {len(df)}, Количество столбцов: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла '{file_name}': {e}")
        return None

if __name__ == "__main__":

    game_df = load_game_data()

    if game_df is not None:
        print("\nПервые 5 строк данных:")
        print(game_df.head())
        print("\nИнформация о столбцах:")
        game_df.info()