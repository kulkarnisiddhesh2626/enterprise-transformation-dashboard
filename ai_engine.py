import time
import random

def get_atk_justification(category, architecture):
    """
    Cloud-safe AI engine for Streamlit deployment.
    Bypasses the local Ollama requirement to prevent server crashes.
    """
    # Simulate the AI "thinking" for a realistic user experience
    time.sleep(1.5) 
    
    # Dynamic, professional business case templates
    templates = [
        f"Based on the **{category}** workflow parameters, implementing a **{architecture}** solution will yield an immediate reduction in manual touchpoints. This aligns with enterprise GRC standards and accelerates our digital transformation KPIs while maintaining strict data governance.",
        
        f"Transitioning the **{category}** operational process to a **{architecture}** framework removes critical operational bottlenecks. Process mining indicates a high ROI within the first two quarters of deployment, effectively neutralizing the current labor sink.",
        
        f"The targeted **{category}** nodes exhibit exceptional automation potential. Deploying **{architecture}** securely within our internal enterprise sandbox will directly offset run-rate financial costs and reallocate human capital to higher-value strategic tasks."
    ]
    
    return random.choice(templates)
