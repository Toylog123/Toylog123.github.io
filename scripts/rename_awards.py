"""统一 honors/ 证书文件名为 `年份_赛事名称_级别_奖次` 格式。"""
import os, sys

# 让 stdout 用 UTF-8 输出，避免 Windows GBK 乱码
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HONORS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'honors'))
print(f'HONORS_DIR = {HONORS_DIR}')
print('actual files:')
for f in sorted(os.listdir(HONORS_DIR)):
    print('  ', repr(f))

RENAMES = {
    '2024年_集成电路创新创业大赛_全国三等奖.jpg':   '2024_集成电路创新创业大赛_国家级三等奖.jpg',
}
print('RENAMES keys (repr):')
for k in RENAMES:
    print('  ', repr(k))

for old, new in RENAMES.items():
    old_path = os.path.join(HONORS_DIR, old)
    new_path = os.path.join(HONORS_DIR, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f'OK  {old}  ->  {new}')
    else:
        print(f'SKIP not found: {old}')

print('---')
for name in sorted(os.listdir(HONORS_DIR)):
    full = os.path.join(HONORS_DIR, name)
    if os.path.isfile(full):
        print(f'{os.path.getsize(full):>8}  {name}')
