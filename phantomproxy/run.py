from core.proxy import run_proxy
from dashboards.flask_ui import start_dashboard
import threading

def run_all():
    threading.Thread(target=run_proxy).start()
    threading.Thread(target=start_dashboard).start()

if __name__ == "__main__":
    run_all()