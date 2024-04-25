from server import create_app
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["DEBUG"] = True
    app.run(host="0.0.0.0", port=port)