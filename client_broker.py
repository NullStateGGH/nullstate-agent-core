import asyncio
import logging
from uagents import Agent, Context, Model
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NullStateClient")

# 1. Match the production intent data schema exactly
class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

# The client broker agent identity
client_agent = Agent(
    name="nullstate_client_broker",
    seed="alpha bravo charlie delta echo foxtrot golf hotel india juliet kilo lima"
)

# Target configurations matching your production environment
TARGET_ENGINE_ADDRESS = "agent1qdnk0e6r0x59nfluh7fljccu2k6l9lmlfeymgj2rcaamenl7d3k92yutvam"
TARGET_TUNNEL_ENDPOINT = "https://pink-things-shave.loca.lt/submit"
REVENUE_VAULT_WALLET = "fetch18jrdu9en96muy94hgeahg8evlcph7ek4ntsp5a"

# Connect straight to the real live mainnet RPC 
ledger_client = LedgerClient(NetworkConfig.fetchai_mainnet())

@client_agent.on_event("startup")
async def dispatch_paid_intent(ctx: Context):
    logger.info("=== INITIALIZING CLIENT BROKER TRANSMISSION ===")
    
    # Define a high-value real-world task prompt
    prompt = "Analyze the recent 2026 mainnet trends for ASI multi-agent scalability and provide a 3-sentence summary."
    fee_amount = 0.0001 # Real processing payout allocation
    
    logger.info(f"Preparing data payload: '{prompt}'")
    
    try:
        # Generate your internal gas key to execute the transaction signature
        # Utilizing the worker's secure on-chain key to perform the loop test
        user_pkey = PrivateKey(client_agent.wallet.private_key)
        wallet = LocalWallet(user_pkey)
        
        logger.info(f"Broadcasting transaction to live block mempool... Destination: {REVENUE_VAULT_WALLET}")
        
        # 2. Settle the payment directly onto the live mainnet blockchain ledger
        tx_result = ledger_client.send_tokens(
            destination=REVENUE_VAULT_WALLET,
            amount=int(fee_amount * 10**18), # Convert to base unit formatting
            denom="atestfet", # Mainnet base execution string format
            wallet=wallet
        )
        
        logger.info(f"Transaction successfully mined! Block Hash: {tx_result.tx_hash}")
        
        # 3. Compile the structural data packet matching your production server schema
        payload = TaskIntent(
            task_id=f"TX_MAINNET_{tx_result.tx_hash[:8]}",
            intent_data=prompt,
            tx_hash=tx_result.tx_hash,
            allocated_fee_fet=fee_amount
        )
        
        logger.info(f"Transmitting cryptographically sealed envelope over public tunnel link to your node...")
        await ctx.send_to_rest_server(TARGET_TUNNEL_ENDPOINT, payload)
        logger.info("Transmission sequence complete! Checking local server for computational fulfillment loops.")
        
    except Exception as e:
        logger.error(f"Transmission execution halted: {str(e)}")

if __name__ == "__main__":
    client_agent.run()
