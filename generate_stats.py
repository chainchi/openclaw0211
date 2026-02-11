import csv
import json
import re
from datetime import datetime

# Read the CSV file
results = []
try:
    with open('fvt_batch_analysis.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit(1)

# Categorization logic
categories = {
    "BMC/ILOM 相關失敗": 0,
    "ROT IP 尋找失敗": 0,
    "Fabric Test 驗證失敗": 0,
    "Firmware 更新進度逾時": 0,
    "其他錯誤": 0
}

for row in results:
    error_text = row.get('錯誤主因', '').upper()
    if "BMC" in error_text or "ILOM" in error_text:
        categories["BMC/ILOM 相關失敗"] += 1
    elif "ROT" in error_text:
        categories["ROT IP 尋找失敗"] += 1
    elif "FABRIC TEST" in error_text:
        categories["Fabric Test 驗證失敗"] += 1
    elif "FIRMWARE" in error_text or "POLL BKC" in error_text:
        categories["Firmware 更新進度逾時"] += 1
    else:
        categories["其他錯誤"] += 1

total = len(results)
stats = []
for name, count in categories.items():
    if count > 0:
        stats.append({
            'error_reason': name,
            'count': count,
            'percentage': round((count / total * 100), 2)
        })

# Sort by count descending
stats.sort(key=lambda x: x['count'], reverse=True)

# Convert to JSON for the HTML file
data_json = json.dumps(stats, ensure_ascii=False)

# HTML template
now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FVT 錯誤主因統計報告 (修正版)</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            max-width: 900px;
            width: 100%;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
        }}
        .subtitle {{
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }}
        .stats-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 40px;
        }}
        .stats-table th, .stats-table td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        .stats-table th {{
            background-color: #2c3e50;
            color: white;
        }}
        .stats-table tr:hover {{
            background-color: #f9f9f9;
        }}
        .chart-container {{
            position: relative;
            height: 400px;
            width: 100%;
        }}
        .footer {{
            margin-top: 30px;
            font-size: 0.9em;
            color: #7f8c8d;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 FVT 錯誤主因統計分析</h1>
        <p class="subtitle">根據 8 筆 Log 檔案歸納之統計結果</p>
        
        <table class="stats-table">
            <thead>
                <tr>
                    <th>錯誤類別</th>
                    <th>數量 (台)</th>
                    <th>百分比 (%)</th>
                </tr>
            </thead>
            <tbody id="table-body">
            </tbody>
        </table>

        <div class="chart-container">
            <canvas id="errorChart"></canvas>
        </div>

        <div class="footer">
            修正版本產生時間: {now_str} | 由 阿琪 (moltbot) 💁‍♀️ 提供
        </div>
    </div>

    <script>
        const data = {data_json};
        
        // Populate Table
        const tableBody = document.getElementById('table-body');
        data.forEach(row => {{
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${{row.error_reason}}</td><td>${{row.count}}</td><td>${{row.percentage}}%</td>`;
            tableBody.appendChild(tr);
        }});

        // Render Chart
        const ctx = document.getElementById('errorChart').getContext('2d');
        new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: data.map(d => d.error_reason),
                datasets: [{{
                    label: '錯誤數量',
                    data: data.map(d => d.count),
                    backgroundColor: [
                        'rgba(52, 152, 219, 0.8)',
                        'rgba(231, 76, 60, 0.8)',
                        'rgba(46, 204, 113, 0.8)',
                        'rgba(241, 196, 15, 0.8)'
                    ],
                    borderWidth: 0
                }}]
            }},
            options: {{
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    x: {{
                        beginAtZero: true,
                        ticks: {{ stepSize: 1 }}
                    }}
                }},
                plugins: {{
                    legend: {{ display: false }},
                    title: {{
                        display: true,
                        text: '各類別錯誤分佈'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

with open('fvt_stats_report.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML_RECREATED_WITH_FIXED_STATS")
