import streamlit as st
import aiohttp
import asyncio

async def send_prompt(prompt: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/agent", json={"prompt": prompt}) as response:
            return await response.json()

st.title("AI Agent Interface")
prompt = st.text_area("Enter your prompt:", height=100)
if st.button("Submit"):
    if prompt:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(send_prompt(prompt))
        st.write("**Response:**")
        st.write(result["response"])
        st.write("**Tools Used:**")
        st.write(", ".join(result["tools_used"]))
        st.write("**Metadata:**")
        st.json(result["metadata"])
    else:
        st.error("Please enter a prompt.")