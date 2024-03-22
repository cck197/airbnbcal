from flask import Flask, Response

from airbnbcal.cal import generate_updated_ical_content, get_ical_fname

app = Flask(__name__)


@app.route("/")
def serve_ical_file():
    return Response(
        generate_updated_ical_content(),
        mimetype="text/calendar",
        headers={"Content-Disposition": f"attachment;filename={get_ical_fname()}"},
    )


if __name__ == "__main__":
    app.run(debug=True)
