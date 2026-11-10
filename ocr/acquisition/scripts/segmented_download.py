"""Download one large file with many parallel HTTP range requests (resumable).

usage: python -I segmented_download.py URL DEST [--workers 16] [--chunk-mb 32]
A DEST.parts.json file records finished chunks so the download can be restarted.
"""
import json, os, sys, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

url, dest = sys.argv[1], sys.argv[2]
a = sys.argv
workers = int(a[a.index('--workers') + 1]) if '--workers' in a else 16
chunk = (int(a[a.index('--chunk-mb') + 1]) if '--chunk-mb' in a else 32) << 20
UA = {'User-Agent': 'Mozilla/5.0'}

size = int(urllib.request.urlopen(urllib.request.Request(url, method='HEAD', headers=UA), timeout=60).headers['Content-Length'])
state_p = dest + '.parts.json'
done = set(json.load(open(state_p))) if os.path.exists(state_p) else set()
if not os.path.exists(dest) or os.path.getsize(dest) != size:
    with open(dest, 'wb') as f:
        f.truncate(size)
    done = set() if not os.path.exists(state_p) else done
lock = threading.Lock()
chunks = [(s, min(size, s + chunk) - 1) for s in range(0, size, chunk)]
todo = [c for c in chunks if c[0] not in done]
print(f'size={size} chunks={len(chunks)} todo={len(todo)}', flush=True)
t0 = time.time(); got = [0]


def work(c):
    s, e = c
    for k in range(10):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={**UA, 'Range': f'bytes={s}-{e}'}), timeout=300)
            b = r.read()
            if len(b) != e - s + 1:
                raise IOError('short read')
            with lock:
                with open(dest, 'r+b') as f:
                    f.seek(s); f.write(b)
                done.add(s); got[0] += len(b)
                json.dump(sorted(done), open(state_p, 'w'))
            return
        except Exception as ex:
            time.sleep(5 * (k + 1))
    print(f'chunk {s} failed - rerun to resume', flush=True)


with ThreadPoolExecutor(workers) as ex:
    for i, _ in enumerate(ex.map(work, todo)):
        if i % 10 == 0:
            el = time.time() - t0
            print(f'{len(done)}/{len(chunks)} chunks, {got[0] / el / 1e6:.2f} MB/s', flush=True)
if len(done) == len(chunks):
    print('complete', dest, size, flush=True)
else:
    print(f'INCOMPLETE {len(done)}/{len(chunks)} - rerun to resume', flush=True); sys.exit(1)
