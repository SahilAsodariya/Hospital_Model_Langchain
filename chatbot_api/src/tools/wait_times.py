import os
from typing import Any
from dotenv import load_dotenv
import numpy as np
from langchain_community.graphs.neo4j_graph import Neo4jGraph
load_dotenv()

URL= os.getenv("NEO4J_URI")

# Detect if running in Docker or local
# Optional: Use an environment variable to force self-signed mode
use_self_signed = os.getenv("NEO4J_USE_SELF_SIGNED", "false").lower() == "true"

if use_self_signed:
    # Use self-signed cert mode for Docker/local testing
    neo4j_uri = URL.replace("neo4j+s://", "neo4j+ssc://")

def _get_current_hospitals() -> list[str]:
    """Fetch a list of current hospital names from a Neo4j database."""
    graph = Neo4jGraph(
        url=neo4j_uri,
        # url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
    )

    current_hospitals = graph.query(
        """
        MATCH (h:Hospital)
        RETURN h.name AS hospital_name
        """
    )
    
    
    return [d["hospital_name"].lower() for d in current_hospitals]


def _get_current_wait_time_minutes(hospital: str) -> int:
    """Get the current wait time at a hospital in minutes."""
    current_hospitals = _get_current_hospitals()

    if hospital.lower() not in current_hospitals:
        return -1

    return np.random.randint(low=0, high=600)


def get_current_wait_times(hospital: str) -> str:
    """Get the current wait time at a hospital formatted as a string."""
    wait_time_in_minutes = _get_current_wait_time_minutes(hospital)

    if wait_time_in_minutes == -1:
        return f"Hospital '{hospital}' does not exist."

    hours, minutes = divmod(wait_time_in_minutes, 60)

    if hours > 0:
        return f"{hours} hours {minutes} minutes"
    else:
        return f"{minutes} minutes"
    
    
# ...

def get_most_available_hospital(_: Any) -> dict[str, float]:
    """Find the hospital with the shortest wait time."""
    current_hospitals = _get_current_hospitals()

    current_wait_times = [
        _get_current_wait_time_minutes(h) for h in current_hospitals
    ]

    best_time_idx = np.argmin(current_wait_times)
    best_hospital = current_hospitals[best_time_idx]
    best_wait_time = current_wait_times[best_time_idx]

    return {best_hospital: best_wait_time}