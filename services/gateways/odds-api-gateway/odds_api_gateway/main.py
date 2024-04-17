from app import create_rest_app, setup
import asyncio

async def main():
    api_client, worker_task = await setup()
    rest_app = create_rest_app(api_client)
    await worker_task
    rest_app.run(host="localhost", port="5000", debug=True)

if __name__ == "__main__":
    asyncio.run(main())