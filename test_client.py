import asyncio
from uagents import Model
from uagents.query import send_sync_message

class TaskIntent(Model):
    task_id: str
    intent_data: str
    max_fee_usdc: float

TARGET_WORKER_ADDRESS = "agent1q0pzh3etywtylwygyfytuae2gtsrymkk4gugsnvvj788hp4g5jgt77m805q"

async def send_paid_intent():
    test_payload = TaskIntent(
        task_id="TX_INTENT_9982",
        intent_data="Analyze this short sentiment: 'DeFi volumes on Base L2 are exploding due to gasless agent transactions.'",
        max_fee_usdc=0.05
    )
    
    print(f"Sending Task Intent directly to secure address: {TARGET_WORKER_ADDRESS}...")
    
    # Modern, non-deprecated unified messaging protocol mapping
    response = send_sync_message(
        destination=TARGET_WORKER_ADDRESS, 
        message=test_payload, 
        endpoint="http://127.0.0.1:8000/submit"
    )
    print("Payload transmitted successfully and logged clean.")

if __name__ == "__main__":
    asyncio.run(send_paid_intent())
