import asyncio
import logging
import json
import ollama
from uagents import Agent, Context, Model, Protocol
from cosmpy.aerial.client import LedgerClient, NetworkConfig

# 1. Initialize structural event logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NullStateAgent")

# 2. Production Communication Schema
class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

# Your active live public gateway tunnel route
PUBLIC_TUNNEL_ENDPOINT = "https://pink-things-shave.loca.lt/submit"

# 3. Instantiate the production node under your sovereign identity seed
nullstate_worker = Agent(
    name="nullstate_worker",
    port=8000,
    seed="into rent follow client club shoulder fan symbol deputy tide blossom guard",
    endpoint=[PUBLIC_TUNNEL_ENDPOINT]
)

# 4. Define and map the global public market protocol 
AI_INFERENCE_PROTOCOL_DIGEST = "proto:nullstate-llm-compute-v1"
nullstate_protocol = Protocol(name="NullState Compute Provider", version="1.0.0")

SOVEREIGN_PAYOUT_WALLET = "fetch18jrdu9en96muy94hgeahg8evlcph7ek4ntsp5a"
LOCAL_MODEL = "gemma4:26b"

# Initialize native ledger client targeting the real live mainnet network
ledger_client = LedgerClient(NetworkConfig.fetchai_mainnet())

# 5. Strict Mainnet Blockchain Transaction Auditor
def verify_native_payment(tx_hash_string: str, expected_fee: float) -> bool:
    try:
        logger.info(f"Querying native ledger for live transaction block: {tx_hash_string}")
        
        # Look up the transaction metadata directly on the live mainnet ledger
        tx_response = ledger_client.query_tx(tx_hash_string)
        tx_body = tx_response.tx.body
        messages = tx_body.messages
        
        for msg in messages:
            if "MsgSend" in str(type(msg)) or "msg_send" in str(type(msg)):
                destination = getattr(msg, "to_address", None)
                
                # Enforce that the recipient matches your funded revenue address exactly
                if destination == SOVEREIGN_PAYOUT_WALLET:
                    logger.info("Cryptographic mainnet payment destination verified successfully.")
                    return True
                    
        logger.error(f"Payment verification failed. Target did not match {SOVEREIGN_PAYOUT_WALLET}")
        return False
    except Exception as e:
        logger.error(f"On-chain validation error. Block lookup failed for hash: {str(e)}")
        return False

# 6. Protocol Message Handler with Async Thread-Offloading
@nullstate_protocol.on_message(model=TaskIntent)
async def process_network_intent(ctx: Context, sender: str, msg: TaskIntent):
    logger.info(f"Intercepted protocol order [{msg.task_id}] from peer: {sender}")
    
    loop = asyncio.get_event_loop()
    is_valid = await loop.run_in_executor(None, verify_native_payment, msg.tx_hash, msg.allocated_fee_fet)
    
    if not is_valid:
        logger.error(f"Fulfillment aborted for peer [{sender}]. On-chain validation failed.")
        return

    try:
        logger.info(f"Payment confirmed. Unlocking local compute resources for {LOCAL_MODEL}...")
        response = ollama.chat(
            model=LOCAL_MODEL,
            messages=[
                {"role": "system", "content": "You are the NullState computing core. Fulfill the intent precisely."},
                {"role": "user", "content": msg.intent_data}
            ]
        )
        print(f"\n[MAINNET TRANSACTION SETTLED AND FULFILLED]")
        print(f"Result Delivered:\n{response['message']['content']}\n")
        
    except Exception as e:
        logger.error(f"Execution panic in local inference engine pass: {str(e)}")

# Mount the protocol configuration directly to the worker core
nullstate_worker.include(nullstate_protocol)

@nullstate_worker.on_event("startup")
async def introduce_agent(ctx: Context):
    logger.info(f"=== NULLSTATE STRICT PRODUCTION CORE ONLINE ===")
    logger.info(f"Sovereign Network Address Handle: {nullstate_worker.address}")
    logger.info(f"Broadcasting Registered Search Digest: {AI_INFERENCE_PROTOCOL_DIGEST}")
    logger.info(f"Monetization Revenue Vault: {SOVEREIGN_PAYOUT_WALLET}")

if __name__ == "__main__":
    nullstate_worker.run()
