from waitress import serve
from app import run

serve(run, host='0.0.0.0', port=8080, url_scheme='RTMP', threads=6)

