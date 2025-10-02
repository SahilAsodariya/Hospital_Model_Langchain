import dotenv
from chatbot_api.src.agents.hospital_rag_agent import hospital_rag_agent_executor

dotenv.load_dotenv()

response = hospital_rag_agent_executor.invoke({"input": "What is the wait time at Wallace-Hamilton?"})
print("*" * 100)
print("What is the wait time at Wallace-Hamilton?")
print("#" * 30)
print(response.get("output"))
print("*" * 100)



response2 = hospital_rag_agent_executor.invoke(
     {"input": "Which hospital has the shortest wait time?"}
 )

print("*" * 100)
print("Which hospital has the shortest wait time?")
print("#" * 30)
print(response2.get("output"))
print("*" * 100)



response3 = hospital_rag_agent_executor.invoke(
     {
         "input": (
             "What have patients said about their "
             "quality of rest during their stay?"
         )
     }
 )


print("*" * 100)
print("What have patients said about their "
     "quality of rest during their stay?")
print("#" * 30)
print(response3.get("output"))
print("*" * 100)



response4 = hospital_rag_agent_executor.invoke(
     {
         "input": (
             "Which physician has treated the "
             "most patients covered by Cigna?"
         )
     }
 )


print("*" * 100)
print("Which physician has treated the "
             "most patients covered by Cigna?")
print("#" * 30)
print(response4.get("output"))
print("*" * 100)



response5 = hospital_rag_agent_executor.invoke(
     {"input": "Show me reviews written by patient 7674."}
 )


print("*" * 100)
print("Show me reviews written by patient 7674.")
print("#" * 30)
print(response5.get("output"))
print("*" * 100)



response = hospital_rag_agent_executor.invoke(
     {
         "input": (
             "Query the graph database to show me "
             "the reviews written by patient 7674"
         )
     }
 )


print("*" * 100)
print("Query the graph database to show me "
             "the reviews written by patient 7674")
print("#" * 30)
print(response5.get("output"))
print("*" * 100)

