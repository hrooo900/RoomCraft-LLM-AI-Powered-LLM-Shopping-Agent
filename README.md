# What are LLM Agents ?
LLM Agents are like intelligent virtual assistants powered by large language models (LLMs) that can understand and process natural language to perform specific tasks. Imagine having a smart assistant that not only answers questions but can also make decisions, handle complex queries, and interact with different tools or systems to get things done for you. For example, an LLM Agent could help you book a product, calculate costs, answer customer queries, or even provide delivery estimates, all within a single conversation. The real power of LLM Agents lies in their ability to manage multiple tasks efficiently, saving time and effort by automating processes that would normally require human intervention. They are necessary because they enable businesses and individuals to streamline operations, enhance customer service, and handle repetitive tasks more effectively, all while providing accurate, real-time responses.

## Project Explaination Video

[Click here to watch the video](https://drive.google.com/file/d/1MlIpbHg1HTQaJkXxy8YVgTK20Gjus_NU/view?usp=sharing)


# RoomCraft LLM: AI-Powered LLM Shopping Agent

**RoomCraft** is an AI-powered LLM agent designed to assist customers in exploring, booking, and calculating shipping costs for furniture products. Built using Mistral AI, LangChain, LangGraph memory and OpenCage API, RoomCraft provides a seamless shopping experience by offering product details, handling customer queries, and calculating delivery estimates.

## Features

- **Product Display:** Shows all available products, including images and detailed descriptions.
- **Customer Information Collection:** Gathers essential details such as name, address, phone number, and email.
- **Shipping Cost Calculation:** Calculates shipping costs based on product weight, dimensions, customer location, and preferred shipping speed (standard, expedited, two-day).
- **Cost Breakdown:** Explains total cost, including the product price and shipping charges, with clear breakdowns of any extra fees.
- **Delivery Estimation:** Automatically calculates the expected delivery date based on the current date and selected shipping speed.
- **Error Handling:** Professionally handles miscommunications and resolves customer queries.
- **Creative Descriptions:** Generates engaging, customized descriptions for each product.

## Technologies Used

- **Mistral AI LLM:** Provides natural language processing and understanding to interact with customers.
- **LangChain:** Used to build the logic and conversational flows of the LLM agent.
- **OpenCage API:** Enables real-time location services to calculate the distance between customers and the nearest seller.
- **LangGraph Memory:** Provides memory for storing conversational chat history
- **Python:** Core programming language for project development.

## How It Works

1. **Product Exploration:**
   - Users can explore all available furniture products or request details for a specific item.
2. **Customer Information Input:**
   - The system collects user details such as name, address, and contact information.
3. **Shipping Calculation:**
   - After the user provides their address, RoomCraft identifies the nearest metro city and calculates the exact shipping distance and costs.
4. **Total Cost Calculation:**
   - Based on the product weight, dimensions, and chosen shipping speed, the total cost (product price + shipping charges) is calculated and explained to the user.
5. **Delivery Date Estimation:**
   - RoomCraft estimates the delivery date based on the selected shipping speed and current date.
6. **Order Management:**
   - The system can book products and handle customer queries, resolving any issues that arise.

## Important
- I have kept some files hidden to avoid misuse for now including environement variables.
- Create `.env` file and add environment variables `MISTRAL_API_KEY` and `OPENCAGE_APIKEY` after cloning.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent.git


2. Create `.env` file and install requirements.txt file
   ```bash
   pip install -r requirements.txt

3. Run `streamlit` instance on file `main.py`
   ```bash
   streamlit run main.py

## Future Upgrade

- Integrate with Weaviate Vector Data Base Python Client v4 to store Chat History and Booking information.
- Add a text to audio model which will read response to customer



## Screenshots

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s1.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s2.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s3.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s4.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s5.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s6.png)

![App Screenshot](https://github.com/hrooo900/RoomCraft-LLM-AI-Powered-LLM-Shopping-Agent/blob/main/Screenshots/s7.png)
