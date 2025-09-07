import asyncio
import os
from .core import Configuration, Server, LLMClient, ChatSession


async def main() -> None:
    """Initialize and run the chat session."""
    config = Configuration()
    
    # Look for servers_config.json in current directory or package directory
    config_path = 'servers_config.json'
    if not os.path.exists(config_path):
        # Try in the package directory
        package_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(package_dir, 'servers_config.json')
    
    server_config = config.load_config(config_path)
    servers = [Server(name, srv_config) for name, srv_config in server_config['mcpServers'].items()]
    llm_client = LLMClient(config.llm_api_key, config.llm_url, config.llm_model)
    chat_session = ChatSession(servers, llm_client)
    await chat_session.start()


def run() -> None:
    """Entry point for the CLI."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
