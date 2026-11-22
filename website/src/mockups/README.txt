Hinh minh hoa theo ngon ngu (public/img/<lang>/*.jpg, ban vi o public/img/*.jpg)
- Man hinh TV (home, theme-*, entertain): python3 home.py vi,en,ja,ko,fr,zh home,theme-kids,theme-elder,theme-women,theme-tech ; python3 ent.py vi,en,ja,ko,fr,zh
  (xoa chu goc trong src/*.jpg roi ve chu moi; can opencv-python-headless, font Inter + Noto CJK)
- App dien thoai (phone, translate, fitness): chup that tu lambo-remote/web/index.html?demo=1 bang Playwright, thay chu theo dict-<lang>.json:
  cp -r lambo-remote/web app; node cap2.js <lang>; python3 compose.py  (sua chu trong dicts.py roi chay python3 dicts.py)
Ket qua o out/<lang>/ -> chep vao public/img/<lang>/ (vi -> public/img/).
