import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN = Path(__file__).resolve().parents[1] / "starter" / "main.py"


def test_end_to_end(tmp_path):
        import socket
        with socket.socket() as sock:
            sock.bind(("127.0.0.1",0))
            port=sock.getsockname()[1]
        env=dict(os.environ,PORT=str(port))
        proc=subprocess.Popen([sys.executable,str(MAIN)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
        try:
            import time,urllib.request,urllib.error
            url=f"http://127.0.0.1:{port}"
            for _ in range(40):
                try:
                    with urllib.request.urlopen(url+"/health",timeout=0.2) as response:
                        assert response.status == 200
                        assert response.headers.get_content_type() == "application/json"
                        assert json.load(response) == {"status":"ok"}
                        break
                except (OSError,TimeoutError): time.sleep(0.05)
            else: pytest.fail("server did not start")
            with urllib.request.urlopen(url+"/echo?message=hello+world",timeout=1) as response:
                assert json.load(response) == {"message":"hello world"}
            with pytest.raises(urllib.error.HTTPError) as err:
                urllib.request.urlopen(url+"/missing",timeout=1)
            assert err.value.code == 404
            assert json.load(err.value) == {"error":"not found"}
        finally:
            proc.terminate()
            try: proc.wait(timeout=3)
            except subprocess.TimeoutExpired: proc.kill();proc.wait(timeout=3)
