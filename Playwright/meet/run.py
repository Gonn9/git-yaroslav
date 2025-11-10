import asyncio
import subprocess
import os


async def run_test_async(test_script):
    print(f"Запуск {test_script}...")

    if not os.path.exists(test_script):
        print(f"Файл не найден: {test_script}")
        return -1

    try:
        test_dir = os.path.dirname(test_script) or "."
        test_file = os.path.basename(test_script)

        process = await asyncio.create_subprocess_exec(
            "python", test_file,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=test_dir
        )

        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"{test_script} завершен успешно")
        else:
            print(f"Ошибка в {test_script}")

        return process.returncode
    except Exception as e:
        print(f"Исключение в {test_script}: {e}")
        return -1

def run_test_sync(test_script):
    print(f"Запуск {test_script}...")

    if not os.path.exists(test_script):
        print(f"Файл не найден: {test_script}")
        return None

    try:
        test_dir = os.path.dirname(test_script) or "."
        test_file = os.path.basename(test_script)

        result = subprocess.run(
            ["python", test_file],
            cwd=test_dir
        )
        print(f"{test_script} завершен успешно")
        return result
    except Exception as e:
        print(f"Ошибка в {test_script}: {e}")
        return None

async def main():
    print("Запуск тестовой последовательности...")

    tasks = [
        run_test_async("modul_1/test_1_login.py"),
        run_test_async("modul_2/test_inv_1_login.py")
    ]
    await asyncio.gather(*tasks)

    tasks = [
        run_test_async("modul_1/test_2.1_newmeet.py"),
        run_test_async("modul_1/test_2.2_shedule.py"),
        run_test_async("modul_1/test_2.3_create_rooms.py")
    ]
    await asyncio.gather(*tasks)

    tasks = [
        run_test_async("modul_1/Test_3.1_invite_in_blocked_room.py"),
        run_test_async("modul_2/Test_inv_2.1_invite_in_blocked_room.py")
    ]
    await asyncio.gather(*tasks)

    tasks = [
        run_test_async("modul_1/Test_3.2_invite_in_free_room.py"),
        run_test_async("modul_2/Test_inv_2.2_invite_in_free_room.py")
    ]
    await asyncio.gather(*tasks)

    run_test_sync("modul_1/test_4_change_rooms.py")
    run_test_sync("modul_1/test_5_delete_rooms.py")

    tasks = [
        run_test_async("modul_1/test_6_logout.py"),
        run_test_async("modul_2/test_inv_3_logout.py")
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())