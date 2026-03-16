import requests
import json
import os
import time
import re
from urllib.parse import urljoin

BASE_DIR = r"C:\Users\fanzhenxing\.claude\delta-trade"
PIC_DIR = os.path.join(BASE_DIR, "picture")

os.makedirs(PIC_DIR, exist_ok=True)

BASE_URL = "https://wiki.bittopup.com"

def sanitize_filename(name):
    """清理文件名，移除特殊字符"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_image_from_list_page():
    """从列表页获取所有图片"""
    guns_url = f"{BASE_URL}/zh/deltaforce/guns"
    protect_url = f"{BASE_URL}/zh/deltaforce/protect"
    
    downloaded = []
    
    for url, category in [(guns_url, "guns"), (protect_url, "protect")]:
        print(f"\n正在处理 {category} 页面...")
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                # 查找所有图片
                # 匹配 <img alt="名称" src="URL"> 模式
                pattern = r'<img[^>]*alt="([^"]+)"[^>]*src="([^"]+)"'
                matches = re.findall(pattern, resp.text)
                
                # 也匹配 src在前的情况
                pattern2 = r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"'
                matches2 = re.findall(pattern2, resp.text)
                
                # 合并结果
                all_matches = [(name, src) for name, src in matches]
                all_matches += [(name, src) for src, name in matches2]
                
                for name, img_src in all_matches:
                    if not img_src or 'logo' in img_src.lower():
                        continue
                    
                    # 构建完整URL
                    if img_src.startswith('//'):
                        img_url = 'https:' + img_src
                    elif img_src.startswith('/'):
                        img_url = BASE_URL + img_src
                    elif not img_src.startswith('http'):
                        img_url = urljoin(url, img_src)
                    else:
                        img_url = img_src
                    
                    # 确定文件扩展名
                    ext = 'png'
                    for e in ['png', 'jpg', 'jpeg', 'webp', 'gif']:
                        if f'.{e}' in img_url.lower():
                            ext = e
                            break
                    
                    filename = f"{category}_{sanitize_filename(name)}.{ext}"
                    filepath = os.path.join(PIC_DIR, filename)
                    
                    if os.path.exists(filepath):
                        print(f"已存在: {filename}")
                        continue
                    
                    try:
                        img_resp = requests.get(img_url, timeout=30)
                        if img_resp.status_code == 200 and len(img_resp.content) > 1000:
                            with open(filepath, 'wb') as f:
                                f.write(img_resp.content)
                            print(f"下载成功: {filename}")
                            downloaded.append(filename)
                            time.sleep(0.3)
                    except Exception as e:
                        print(f"下载失败 {name}: {e}")
                        
        except Exception as e:
            print(f"获取页面失败 {url}: {e}")
    
    return downloaded

def main():
    print("=" * 50)
    print("三角洲行动 Wiki 数据下载器")
    print("=" * 50)
    
    # 检查数据文件
    guns_file = os.path.join(BASE_DIR, "guns_data.json")
    protect_file = os.path.join(BASE_DIR, "protect_data.json")
    
    if os.path.exists(guns_file):
        print(f"✓ 枪械数据已保存: {guns_file}")
    if os.path.exists(protect_file):
        print(f"✓ 防具数据已保存: {protect_file}")
    
    print(f"\n图片保存目录: {PIC_DIR}")
    
    # 下载图片
    downloaded = get_image_from_list_page()
    
    print("\n" + "=" * 50)
    print(f"下载完成! 共下载 {len(downloaded)} 张图片")
    print("=" * 50)

if __name__ == "__main__":
    main()