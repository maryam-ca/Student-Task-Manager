from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Task Manager</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e3a8a);
                color: white;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .card {
                width: 500px;
                padding: 40px;
                background: rgba(255,255,255,0.10);
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            }

            h1 {
                margin-bottom: 10px;
            }

            p {
                color: #dbeafe;
                line-height: 1.6;
            }

            .status {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #16a34a;
                border-radius: 25px;
                font-weight: bold;
            }

            .docker {
                margin-top: 25px;
                font-size: 14px;
                color: #bfdbfe;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Student Task Manager</h1>

            <p>
                A simple Flask web application
                containerized using Docker.
            </p>

            <div class="status">
                ✓ Application Running
            </div>

            <div class="docker">
                Docker Lab Assignment 1
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)