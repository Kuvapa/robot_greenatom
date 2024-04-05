import asyncio


stop_count = False

async def robot_count(start=0):
    global stop_count
    current_number = start
    while not stop_count:
        print(current_number)
        current_number += 1
        await asyncio.sleep(1)


async def switch_count(bool_flag):
    global stop_count
    stop_count = bool_flag


if __name__ == "__main__":
    start_point = input("Введите стартовое значение для отсчета, нажмите "
                        "Enter, для начала отсчета с 0: ")
    try:
        if start_point == '':
            start_point = 0
        else:
            start_point = int(start_point)
    except ValueError:
        raise ValueError('Некорректно введенные данные')
    asyncio.run(robot_count(start_point))