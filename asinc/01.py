import asyncio
import os
import time

COEFF = 0.01


async def job(name, prep1, work1, prep2, work2):
    print(f"{name} started the 1 task.")
    await asyncio.sleep(prep1 * COEFF)
    print(f"{name} moved on to the defense of the 1 task.")
    time.sleep(work1 * COEFF)
    print(f"{name} completed the 1 task.")
    print(f"{name} is resting.")
    await asyncio.sleep(5 * COEFF)
    print(f"{name} started the 2 task.")
    await asyncio.sleep(prep2 * COEFF)
    print(f"{name} moved on to the defense of the 1 task.")
    time.sleep(work2 * COEFF)
    print(f"{name} completed the 2 task.")


async def interviews(*args):
    peoples = args[:]
    tasks = []
    for people in peoples:
        tasks.append(asyncio.create_task(job(people[0], people[1], people[2], people[3], people[4])))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
