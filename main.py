import loguru
import sys

from utils.pentest_gpt import pentestGPT

logger = loguru.logger

if __name__ == "__main__":
    pentestGPTHandler = pentestGPT()
    pentestGPTHandler.main()

    # the previous example
    """
    chatGPTAgent = ChatGPT(ChatGPTConfig())
    # request user's input to create a new chat.
    question = Prompt.ask("What do you want to ask ChatGPT?")
    # the title of this conversation will be new-chat. We can delete it later.
    text, conversation_id = chatGPTAgent.send_new_message(question)
    print(text, conversation_id)
    # get history id
    history = chatGPTAgent.get_conversation_history()
    print(history)
    for uuid in history:
        print(uuid)
        if history[uuid].lower() == "new chat":
            result = chatGPTAgent.delete_conversation(uuid)
            print(result)
    history = chatGPTAgent.get_conversation_history()
    print(history)
    """
