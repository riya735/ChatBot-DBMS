from llm import generate_sql


question = input("Ask: ")

sql = generate_sql(question)

print(sql)
