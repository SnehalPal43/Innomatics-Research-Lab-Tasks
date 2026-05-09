from langgraph.graph import StateGraph, END

from workflows.workflow_nodes import (
    retrieve_context,
    generate_response
)

def build_graph():

    workflow = StateGraph(dict)

    workflow.add_node(
        "retrieve_context",
        retrieve_context
    )

    workflow.add_node(
        "generate_response",
        generate_response
    )

    workflow.set_entry_point(
        "retrieve_context"
    )

    workflow.add_edge(
        "retrieve_context",
        "generate_response"
    )

    workflow.add_edge(
        "generate_response",
        END
    )

    return workflow.compile()