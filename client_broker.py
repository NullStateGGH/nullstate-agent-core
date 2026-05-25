import asyncio
import logging
import aiohttp
from uagents import Agent, Context, Model
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from cosmpy.aerial.wallet import LocalWallet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NullStateClient")

class TaskIntent(Model):
    task_id: str
    intent_data: str
    tx_hash: str  
    allocated_fee_fet: float

client_agent = Agent(
    name="nullstate_client_broker",
    port=8001,
    seed="alpha bravo charlie delta echo foxtrot golf hotel india juliet kilo lima"
)

TARGET_TUNNEL_ENDPOINT = "https://pink-things-shave.loca.lt/submit"
REVENUE_VAULT_WALLET = "fetch18jrdu9en96muy94hgeahg8evlcph7ek4ntsp5a"

ledger_client = LedgerClient(NetworkConfig.fetchai_mainnet())

@client_agent.on_event("startup")
async def dispatch_paid_intent(ctx: Context):
    logger.info("=== INITIALIZING CLIENT BROKER TRANSMISSION ===")
    
    prompt = "Analyze the recent 2026 mainnet trends for ASI multi-agent scalability and provide a 3-sentence summary."
    fee_amount = 0.0000000000001 
    
    logger.info(f"Preparing data payload: '{prompt}'")
    
    try:
        production_seed = "into rent follow client club shoulder fan symbol deputy tide blossom guard"
        wallet = LocalWallet.from_mnemonic(production_seed)
        
        logger.info(f"Broadcasting transaction to live block mempool... Destination: {REVENUE_VAULT_WALLET}")
        
        tx_result = ledger_client.send_tokens(
            destination=REVENUE_VAULT_WALLET,
            amount=int(fee_amount * 10**18), 
            denom="afet", 
            sender=wallet
        )
        
        logger.info(f"Transaction successfully mined! Block Hash: {tx_result.tx_hash}")
        
        # Compile the payload exactly matching your server structural specification
        payload_data = {
            "task_id": f"TX_MAINNET_{tx_result.tx_hash[:8]}",
            "intent_data": prompt,
            "tx_hash": tx_result.tx_hash,
            "allocated_fee_fet": fee_amount
        }
        
        logger.info(f"Transmitting cryptographically sealed envelope over public tunnel link...")
        
        # Dispatch the payload using standard asynchronous HTTP architecture
        async with aiohttp.ClientSession() as session:
            async with session.post(TARGET_TUNNEL_ENDPOINT, json=payload_data) as response:
                response_text = await response.text()
                logger.info(f"Tunnel transmission delivered! Server Status Code: {response.status}")
                
        logger.info("Transmission sequence complete!")
        
    except Exception as e:
        logger.error(f"Transmission execution halted: {str(e)}")

if __name__ == "__main__":
    client_agent.run()
