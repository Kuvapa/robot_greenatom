import asyncio
import sys


async def robot_count(start: int = 0) -> None:
    current_number = start
    while True:
        print(current_number)
        current_number += 1
        await asyncio.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            start_number = int(sys.argv[1])
        except ValueError:
            raise ValueError('Введен неправильный формат данных')
    else:
        start_number = 0
    asyncio.run(robot_count(start_number))