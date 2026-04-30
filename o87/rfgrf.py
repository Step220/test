import logging
import datetime
import os
import multiprocessing
import time
tasks_file = "dddd.txt"
log_file = "log.txt"
logging.basicConfig(
    filename= log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"

)
def write_task_to_file():
    while True:
        try:
            print("добавление задачи: ")
            task_time = input("Введите время (HH:MM): ").strip()
            date = input("введите дату (YYYY-MM-DD):").strip()
            desc = input("введите описание:").strip()
            fulltime = datetime.datetime.strptime(f"{date} {task_time}", "%Y-%m-%d %H:%M")
            with open(tasks_file, "a", encoding="utf-8") as file:
                file.write(f"{fulltime.strftime("%Y-%m-%d %H:%M")} -> {desc}\n")
            print("задача добавлена успешно")
            logging.info(f"Пользоватедь добавил задачу {desc}")
        except ValueError:
            print(f" Ошибка даты и времени! {ValueError}")
            logging.error(f"Пользователь ввел неверно дату и время для задачи ")
        except Exception as e:
            print(f"Ошибка:s {e}")
            logging.error(f" Ошибка при добавление задачи: {e}")
def show_tasks():
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        try:
            with open(tasks_file, "r", encoding="utf-8") as file:
                if file:
                    tasks = file.readlines()
                    for task in tasks:
                        task_data = task.split(" -> ")[0]
                        if task_data == now:
                            print("\n"+task)
                            time.sleep(30)
                else:
                    pass
        except Exception as e:
            print(f"Ошибка: {e}")
            logging.error(f" Ошибка при чтение файла")
def main():
    logging.info("програма заупущена")
    if not os.path.exists(tasks_file):
        open(tasks_file, "w", encoding="utf-8").close()
        logging.info("Файл создан успешно!")
    show_process = multiprocessing.Process(target=show_tasks, daemon=True)
    show_process.start()
    write_task_to_file()
if __name__ == "__main__":
    main()
class Baran:
    def __init__(self):
        self.baran = Baran()