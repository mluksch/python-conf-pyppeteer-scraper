import asyncio

import processor

asyncio.get_event_loop().run_until_complete(processor.process())
