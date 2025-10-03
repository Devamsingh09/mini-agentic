import os
from pathlib import Path
import random

DOCS_DIR = Path("data/docs")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

# Finance-related topics
TOPICS = [
    "Stock Market Basics",
    "Cryptocurrency Overview",
    "Banking and Interest Rates",
    "Inflation and Monetary Policy",
    "Personal Finance and Budgeting",
    "Investment Strategies",
    "Financial Regulations and Compliance",
    "Global Economic Indicators",
]

# Sample sentences for content generation
SENTENCES = {
    "Stock Market Basics": [
        "The stock market is a platform where investors buy and sell shares of publicly traded companies.",
        "Investing in stocks allows individuals to potentially earn returns through capital gains and dividends.",
        "Stock prices are influenced by company performance, market sentiment, and broader economic factors.",
        "Diversification across multiple sectors can reduce risk in a stock portfolio.",
        "Market indices such as the S&P 500 and NASDAQ track overall market performance.",
        "Stock exchanges provide transparency and liquidity for buying and selling shares.",
        "Long-term investing often helps mitigate short-term market volatility.",
        "Technical analysis and fundamental analysis are common methods to evaluate stocks."
    ],
    "Cryptocurrency Overview": [
        "Cryptocurrencies are digital assets that use cryptography to secure transactions and control supply.",
        "Bitcoin, launched in 2009, was the first cryptocurrency and remains the most widely recognized.",
        "Ethereum introduced smart contracts, allowing decentralized applications to run on blockchain networks.",
        "Crypto markets are highly volatile and require careful risk management.",
        "Blockchain technology ensures transparency, immutability, and decentralized record keeping.",
        "Investors should consider security practices such as cold wallets and two-factor authentication.",
        "Initial Coin Offerings (ICOs) are used by startups to raise funds, though they carry high risk.",
        "Regulatory approaches for cryptocurrencies vary across countries, impacting adoption and trading."
    ],
    "Banking and Interest Rates": [
        "Banks provide financial services including loans, deposits, and payment processing.",
        "Interest rates are set by central banks to influence economic activity and inflation.",
        "Loans can be fixed-rate or floating-rate, impacting repayment amounts over time.",
        "Savings accounts allow customers to earn interest while keeping funds accessible.",
        "Commercial banks are regulated to ensure solvency, liquidity, and depositor protection.",
        "The interbank lending rate affects borrowing costs for financial institutions.",
        "Monetary policy decisions directly impact lending rates, credit availability, and economic growth.",
        "Digital banking and fintech have transformed how customers access banking services."
    ],
    "Inflation and Monetary Policy": [
        "Inflation is the rate at which the general level of prices for goods and services rises.",
        "Central banks use tools such as repo rates, reserve requirements, and open market operations to manage inflation.",
        "Moderate inflation encourages spending and investment, while hyperinflation erodes purchasing power.",
        "Consumer Price Index (CPI) and Wholesale Price Index (WPI) are commonly used to measure inflation.",
        "Monetary policy can be expansionary or contractionary depending on economic conditions.",
        "Inflation expectations influence wage negotiations, pricing strategies, and investment decisions.",
        "Deflation, a decrease in prices, can lead to reduced consumption and economic stagnation.",
        "Central banks aim for price stability while supporting sustainable economic growth."
    ],
    "Personal Finance and Budgeting": [
        "Personal finance involves managing income, expenses, savings, and investments to achieve financial goals.",
        "Budgeting helps individuals track spending, plan for emergencies, and allocate funds effectively.",
        "Emergency funds are recommended to cover unexpected expenses without incurring debt.",
        "Debt management includes strategies such as consolidating loans or prioritizing high-interest debt repayment.",
        "Investing in retirement accounts like 401(k) or IRAs helps ensure long-term financial security.",
        "Insurance products provide protection against risks such as illness, accidents, or property damage.",
        "Understanding taxes and leveraging deductions can optimize personal wealth.",
        "Financial literacy is crucial to make informed decisions and avoid common pitfalls."
    ],
    "Investment Strategies": [
        "Investment strategies vary based on risk tolerance, time horizon, and financial goals.",
        "Equity investing focuses on buying shares in companies to earn dividends and capital appreciation.",
        "Fixed income investing involves bonds and other debt instruments that pay interest over time.",
        "Diversification reduces risk by spreading investments across asset classes, sectors, and geographies.",
        "Active management involves frequent trading to outperform market benchmarks, while passive management tracks indices.",
        "Value investing seeks undervalued assets, whereas growth investing targets high-potential companies.",
        "Portfolio rebalancing helps maintain target asset allocation as market values change.",
        "Investors should consider fees, tax implications, and liquidity when making investment decisions."
    ],
    "Financial Regulations and Compliance": [
        "Financial regulations ensure transparency, accountability, and protection for investors and consumers.",
        "Compliance involves adhering to laws, rules, and guidelines set by regulatory authorities.",
        "Anti-money laundering (AML) and know your customer (KYC) policies help prevent financial crimes.",
        "Securities regulators oversee stock exchanges, brokerage firms, and investment products.",
        "Regulatory frameworks evolve to address emerging risks such as cybersecurity and fintech innovation.",
        "Failure to comply with regulations can result in fines, sanctions, or reputational damage.",
        "Audits and reporting requirements maintain integrity and public confidence in financial systems.",
        "Global coordination among regulators helps manage cross-border financial activities."
    ],
    "Global Economic Indicators": [
        "Economic indicators are statistics that provide insights into a country's economic performance.",
        "Gross Domestic Product (GDP) measures the total value of goods and services produced.",
        "Unemployment rate indicates the percentage of the labor force that is jobless and seeking work.",
        "Consumer confidence reflects household sentiment about the economy and spending willingness.",
        "Trade balances show the difference between exports and imports of goods and services.",
        "Inflation rates, interest rates, and fiscal policies influence macroeconomic stability.",
        "Leading, lagging, and coincident indicators help economists predict trends and guide policy.",
        "Global economic indicators are monitored by investors, governments, and central banks for decision making."
    ],
}

def generate_doc_content(topic, min_words=400):
    """Generate content for a given topic with at least min_words words."""
    sentences = SENTENCES[topic]
    content = ""
    while len(content.split()) < min_words:
        content += " ".join(random.sample(sentences, k=len(sentences))) + " "
    return content.strip()

def generate_documents():
    print(f"Generating {len(TOPICS)} finance-related documents in '{DOCS_DIR}'...")
    for idx, topic in enumerate(TOPICS, 1):
        content = generate_doc_content(topic)
        file_path = DOCS_DIR / f"doc_{idx}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Topic: {topic}\n\n{content}")
        print(f"✅ Generated {file_path} ({len(content.split())} words)")
    print("All documents generated successfully.")

if __name__ == "__main__":
    generate_documents()
