# 三角洲行动 Delta Force Wiki 数据

## 数据来源
- 枪械武器: https://wiki.bittopup.com/zh/deltaforce/guns
- 防护装备: https://wiki.bittopup.com/zh/deltaforce/protect

## 文件结构

```
delta-trade/
├── guns_data.json       # 枪械数据 (51把武器)
├── protect_data.json    # 防具数据 (92件装备)
├── download_wiki.py     # 下载脚本
├── README.md            # 本文件
└── picture/             # 图片文件夹 (272张图片)
    ├── guns_*.png       # 枪械缩略图
    ├── protect_*.png    # 防具缩略图
    └── *.png            # 高清大图
```

## 数据统计

### 枪械武器 (51把)
| 类型 | 数量 |
|------|------|
| 步槍 | 17 |
| 衝鋒槍 | 9 |
| 霰彈槍 | 3 |
| 輕機槍 | 3 |
| 精確射手步槍 | 8 |
| 狙擊步槍 | 4 |
| 手槍 | 7 |

### 防护装备 (92件)
| 类型 | 数量 |
|------|------|
| 頭盔 | 24 |
| 護甲 | 24 |
| 胸掛 | 20 |
| 背囊 | 24 |

### 防弹等级分布
- 6级防弹: 10件
- 5级防弹: 18件  
- 4级防弹: 18件
- 3级防弹: 18件
- 2级防弹: 16件
- 1级防弹: 12件

## 数据字段说明

### 枪械数据 (guns_data.json)
- `name`: 武器名称
- `type`: 武器类型
- `desc`: 武器描述
- `damage`: 伤害值
- `rpm`: 射速 (每分钟发射数)
- `id`: 武器ID

### 防具数据 (protect_data.json)
- `name`: 装备名称
- `type`: 装备类型 (頭盔/護甲/胸掛/背囊)
- `level`: 防弹等级 (1-6)
- `desc`: 装备描述
- `id`: 装备ID

## 下载日期
2026年3月16日
