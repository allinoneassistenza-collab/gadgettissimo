"""Avvio locale: python run.py. Nessuna credenziale predefinita."""
from pathlib import Path
import os,sys,threading,webbrowser

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'backend'))
from app.config import Config
import uvicorn

if __name__=='__main__':
    host=os.getenv('GADGET_HOST','127.0.0.1')
    port=int(os.getenv('GADGET_PORT','8765'))
    if not (ROOT/'frontend'/'dist'/'index.html').exists():
        raise SystemExit('Interfaccia assente. Esegui Installa-Windows.cmd oppure npm ci e npm run build in frontend.')
    if '--no-browser' not in sys.argv:
        def open_when_ready():
            import time,urllib.request
            url=f'http://127.0.0.1:{port}'
            for _ in range(60):
                try:
                    urllib.request.urlopen(url+'/api/health',timeout=1)
                    webbrowser.open(url);return
                except Exception:time.sleep(.5)
        threading.Thread(target=open_when_ready,daemon=True).start()
    print(f'Gadgettissimo Gestionale: http://127.0.0.1:{port}')
    print('Per arrestare il gestionale chiudi questa finestra o premi Ctrl+C.')
    uvicorn.run('app.main:app',host=host,port=port,workers=1,proxy_headers=False)
