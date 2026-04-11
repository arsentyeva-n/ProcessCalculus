from sample_sync import sync_main
from sample_async import async_main
import asyncio

n = 3
res_sync = [sync_main() for _ in range(n)]
res_async = [(asyncio.run(async_main())) for _ in range(n)]

print(f"Среднее время:")
print(f"Синхронные запросы {sum(res_sync)/n:.2f} секунд")
print(f"Асинхронные запросы {sum(res_async)/n:.2f} секунд")