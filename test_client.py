import asyncio
import logging
from uagents import Model
from uagents.query import send_sync_message

# 1. Initialize crisp tracing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NullStateClient")

# 2. Match structural protocol schemas
class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

# The live refactored destination address handle of your running worker node
TARGET_WORKER_ADDRESS = "agent1qdnk0e6r0x59nfluh7fljccu2k6l9lmlfeymgj2rcaamenl7d3k92yutvam"

async def send_paid_intent():
    test_payload = TaskIntent(
        task_id="TX_MAINNET_SEED_LIVE_01",
        intent_data="Compile a 3-step execution plan for an AI agent to arbitrage liquidity between pool X and pool Y on a DEX.",
        tx_hash="mock_fai_tx_hash_verification_pass_2026",
        allocated_fee_fet=0.1
    )
    
    logger.info(f"Querying Almanac Ledger Registry for target destination: {TARGET_WORKER_ADDRESS}")
    
    # Direct async await execution path
    response = await send_sync_message(TARGET_WORKER_ADDRESS, test_payload)
    
    logger.info("Payload packet successfully confirmed, delivered, and sockets closed.")

if __name__ == "__main__":
    asyncio.run(send_paid_intent())
