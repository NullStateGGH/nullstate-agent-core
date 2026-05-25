import asyncio
from uagents import Model
from uagents.query import send_sync_message

# Match the worker node schema parameters
class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

TARGET_WORKER_ADDRESS = "agent1q0pzh3etywtylwygyfytuae2gtsrymkk4gugsnvvj788hp4g5jgt77m805q"

async def send_paid_intent():
    test_payload = TaskIntent(
        task_id="TX_MAINNET_8831",
        intent_data="Compile a 3-step execution plan for an AI agent to arbitrage liquidity between pool X and pool Y on a DEX.",
        tx_hash="mock_fai_tx_hash_verification_pass_2026",
        allocated_fee_fet=0.1
    )
    
    print(f"Transmitting intent payload directly to target worker: {TARGET_WORKER_ADDRESS}")
    
    # Unified Async-Await Protocol Adjustment
    response = await send_sync_message(
        TARGET_WORKER_ADDRESS,
        test_payload,
        "http://127.0.0.1:8000/submit"
    )
    print("Task request packet successfully routed and connection closed cleanly.")

if __name__ == "__main__":
    asyncio.run(send_paid_intent())
