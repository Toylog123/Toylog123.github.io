"""统一 honors/ 证书文件名为 `年份_赛事_级别_奖次`，并把"国家级"→"全国"。"""
import os, sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

HONORS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'honors'))

# 初始历史规则：去掉"年"字、把"全国一等奖"统一为最终格式
EXPLICIT_RENAMES = {
    '2024年_集成电路创新创业大赛_全国三等奖.jpg': '2024_集成电路创新创业大赛_全国三等奖.jpg',
    '2024_C4网络技术挑战赛_全国一等奖.jpg':         '2024_C4网络技术挑战赛_全国一等奖.jpg',
}

# 通用规则：把"国家级"替换成"全国"
GENERAL_REPLACE = ('_国家级', '_全国')

print(f'HONORS_DIR = {HONORS_DIR}')

for old, new in EXPLICIT_RENAMES.items():
    old_path = os.path.join(HONORS_DIR, old)
    new_path = os.path.join(HONORS_DIR, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f'OK  {old}  ->  {new}')
    else:
        print(f'SKIP (already done or not found): {old}')

print('--- general pass: replace _国家级 -> _全国 in remaining files ---')
for name in sorted(os.listdir(HONORS_DIR)):
    full = os.path.join(HONORS_DIR, name)
    if not os.path.isfile(full):
        continue
    if GENERAL_REPLACE[0] in name:
        new_name = name.replace(GENERAL_REPLACE[0], GENERAL_REPLACE[1])
        new_full = os.path.join(HONORS_DIR, new_name)
        os.rename(full, new_full)
        print(f'OK  {name}  ->  {new_name}')

print('--- final ---')
for name in sorted(os.listdir(HONORS_DIR)):
    full = os.path.join(HONORS_DIR, name)
    if os.path.isfile(full):
        print(f'{os.path.getsize(full):>8}  {name}')
