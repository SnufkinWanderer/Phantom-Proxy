from datetime import datetime

def generate_report(logs, format='md'):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if format == 'md':
        with open(f"report_{timestamp}.md", "w") as f:
            f.write("# PhantomProxy Report\n\n")
            for line in logs:
                f.write(f"- {line}\n")
    elif format == 'html':
        with open(f"report_{timestamp}.html", "w") as f:
            f.write("<html><body><h2>Report</h2><ul>")
            for line in logs:
                f.write(f"<li>{line}</li>")
            f.write("</ul></body></html>")