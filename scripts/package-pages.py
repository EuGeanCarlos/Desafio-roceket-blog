"""Empacota apenas os recursos públicos versionados do projeto original."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.'
FILES = ['img/arrow-right.svg', 'img/featured-image.png', 'img/logo.svg', 'img/post-1.png', 'img/post-2.png', 'img/post-3.png', 'img/post-4.png', 'img/search.svg', 'index.html', 'jquery.js', 'slick.min.js', 'style.css']
DEST = ROOT / "_site"
DEST.mkdir(exist_ok=True)
for name in FILES:
    target = DEST / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / name, target)
assert (DEST / "index.html").is_file(), "Entrada index.html ausente"
(DEST / ".nojekyll").touch()
