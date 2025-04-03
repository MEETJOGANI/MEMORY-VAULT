import os
import sys

# Create .streamlit directory if it doesn't exist
os.makedirs(".streamlit", exist_ok=True)

# Create config.toml file with necessary settings
config_content = """
[server]
headless = true
port = 5000
address = "0.0.0.0"
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
"""

with open(".streamlit/config.toml", "w") as f:
    f.write(config_content)

# Run the Streamlit app directly
os.system(f"{sys.executable} -m streamlit run app.py")