from anthropic import Anthropic
from pathlib import Path
import yaml

client = Anthropic()
CFG = yaml.safe_load(Path("config/llm.yaml").read_text())
SYSTEM = Path("prompts/support_system.md").read_text()

def answer(question: str) -> str:
    msg = client.messages.create(
        model=CFG["model"], max_tokens=800, temperature=CFG["temperature"],
        system=SYSTEM, messages=[{"role": "user", "content": question}],
    )
    return msg.content[0].text
