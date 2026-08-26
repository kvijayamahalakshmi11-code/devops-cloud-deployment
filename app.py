from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DevOps Cloud App")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }}

            .container {{
                background-color: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            }}

            h1 {{
                color: #333;
            }}

            p {{
                font-size: 18px;
                color: #555;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 {APP_NAME}</h1>

            <p>Welcome to my DevOps Web Application!</p>

            <p class="status">Application is running successfully.</p>

            <p>Environment: {APP_ENV}</p>

            <p>Powered by Python Flask + Docker</p>

        </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "environment": APP_ENV
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)