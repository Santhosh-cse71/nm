import eel
import os
import platform
import webbrowser
import subprocess

# Path to the React build directory (Vite default is 'dist')
web_dir = 'dist'

# Initialize eel with the web directory
eel.init(web_dir)

# Example backend function to be called from JS
@eel.expose
def backend_predict(location, date):
    # Mock prediction logic similar to app.py
    if not location:
        return {"error": "Please enter a location."}
    return {
        "message": f"Generated mock prediction for {location} on {date}",
        "key_indicators": {
            "Current Flood Risk": "Moderate",
            "7-Day Earthquake Probability": "Low (2.1%)",
            "Air Quality Index (AQI)": "Good (35)"
        }
    }

@eel.expose
def send_test_alert():
    return "Test Alert Sent! You've received a simulated emergency alert. Stay informed!"

@eel.expose
def send_critical_alert():
    return "CRITICAL ALERT! This is a simulated CRITICAL emergency alert. Evacuate immediately!"

@eel.expose
def upload_file(file_path):
    # For demo, just return file info
    if not os.path.exists(file_path):
        return {"error": "File not found."}
    size = os.path.getsize(file_path)
    return {"file_path": file_path, "size": size}   

if __name__ == "__main__":
    # Use eel's built-in mode to open MS Edge browser 
    # Remove manual open_edge function
    eel.start('index.html', port=8000, block=True, size=(900, 600), mode='edge') 
