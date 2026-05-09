from vectorstore.retriever import ContextRetriever

retriever = ContextRetriever()

def retrieve_context(state):
    query = state["query"]

    context = retriever.retrieve(query)

    state["context"] = context

    return state


def generate_response(state):

    context = state["context"]

    query = state["query"]

    if not context.strip():
        state["response"] = (
            "No relevant information found."
        )

    else:
        state["response"] = f"""
Context:
{context}

User Query:
{query}

Generated Response:
Based on the uploaded documents,
here is the relevant answer:

{context}
"""

    return state