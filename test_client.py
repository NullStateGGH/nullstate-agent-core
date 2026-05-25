import asyncio
import logging
from uagents import Agent, Context, Model, Bureau

# 1. Initialize system tracing loops
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NullStateClient")

# 2. Match the exact data model protocol schema of the worker node
class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

# 3. Create a distinct client agent identity instance
client_agent = Agent(name="nullstate_client_driver", seed="temporary_client_driver_seed_2026")

# Target address pointing explicitly to your live refactored worker seed address
TARGET_WORKER_ADDRESS = "agent1qdnk0e6r0x59nfluh7fljccu2k6l9lmlfeymgj2rcaamenl7d3k92yutvam"

@client_agent.on_event("startup")
async def broadcast_paid_intent(ctx: Context):
    logger.info("Client node initialization completed.")
    
    test_payload = TaskIntent(
        task_id="TX_MAINNET_SEED_LIVE_01",
        intent_data="Compile a 3-step execution plan for an AI agent to arbitrage liquidity between pool X and pool Y on a DEX.",
        tx_hash="mock_fai_tx_hash_verification_pass_2026",
        allocated_fee_fet=0.1
    )
    
    logger.info(f"Transmitting intent payload natively upstream to: {TARGET_WORKER_ADDRESS}")
    
    # Use the clean, core-native fire-and-forget messaging route
    await ctx.send(TARGET_WORKER_ADDRESS, test_payload)
    logger.info("Payload packet successfully pushed into the socket pool.")

# 4. Use a Bureau cluster wrapper to manage the underlying event runtime loops flawlessly
if __name__ == "__main__":
    bureau = Bureau(port=8001, endpoint=["http://127.0.0.1:8001/submit"])
    bureau.add(client_agent)
    bureau.run()
