# quiz_generator.py
from langchain_community.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Step 1: Load .env variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL_NAME")

# Step 2: Validate API key and model name
print("🔍 Checking env values:")
print("✅ API Key:", "Loaded" if api_key else "❌ Not found")
print("✅ Model Name:", model_name if model_name else "❌ Not found")

if not api_key or not model_name:
    print("❌ Missing environment variables. Check your .env file.")
    exit()

# Step 3: Setup OpenAI model
llm = ChatOpenAI(
    model=model_name,
    openai_api_key=api_key,
    temperature=0.5  # Optional: Controls creativity
)

# Step 4: Create quiz generation prompt
prompt = PromptTemplate(
    input_variables=["topic"],
    template=(
        "Generate 3 multiple choice questions for high school students "
        "on the topic: {topic}. For each question, provide:\n"
        "- Question\n- Four options (A–D)\n- Correct answer letter\n"
        "Format the output as numbered questions."
    )
)

# Step 5: Create LangChain LLMChain
quiz_chain = LLMChain(llm=llm, prompt=prompt)

# Step 6: Run the chain
topic = "Photosynthesis"  # You can change this
print(f"\n🧠 Generating quiz on: {topic}...\n")

quiz_output = quiz_chain.run(topic)

# Step 7: Display result
print("📋 Quiz Output:\n")
print(quiz_output)
