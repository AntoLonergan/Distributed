from waitress import serve
from app import run

serve(run, host='localhsot', port=8080, url_scheme='RTMP', threads=6)

