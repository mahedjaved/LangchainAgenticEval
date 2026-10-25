# langchain-refund-agent

## Quickstart

- `python -m agent.models` - Initialize the LangChain model (requires `KILO_API_KEY` in `.env`)
- `python -m main` - Run the simple CLI entry point
- Project uses Python 3.12 (per `.python-version`)

## Environment

- Copy `.env.example` to `.env` and set `KILO_API_KEY`
- `.env` is gitignored; never commit real keys
- `load_dotenv()` is called in `agent/models.py` line 6

## Architecture

- `agent/models.py` - LangChain model initialization with `nvidia/nemotron-3.5-lightling:free` via `openai` provider at `https://ai-gateway.kilo.ai/api/v1`
- `agent/tools.py` - LangChain tools; imports `user_data` from `agent/data.py`
- `agent/data.py` - Static user purchase data dictionary (the "source of truth" for refund eligibility)
- `agent/objects.py` - Pydantic models: `Answer`, `PurchaseItem`
- `agent/prompts.py` - System prompt for the refund agent role

## Development

- No lint/typecheck/config found in this repo
- No test framework or CI configured
- `uv.lock` and `pyproject.toml` define dependencies: `dotenv`, `langchain`, `langchain-openai`