import base64
from pathlib import Path
from xml.sax.saxutils import escape

BASE = Path(__file__).resolve().parent
chart_png = BASE / 'cpu-chart.png'
chart_b64 = base64.b64encode(chart_png.read_bytes()).decode('ascii')
chart_uri = 'data:image/png%3Bbase64,' + chart_b64


def esc(s):
    return escape(str(s), {'"': '&quot;'})


def rect(cell_id, x, y, w, h, value='', style='rounded=0;whiteSpace=wrap;html=1;', parent='1'):
    return (
        f'<mxCell id="{esc(cell_id)}" value="{esc(value)}" style="{esc(style)}" vertex="1" parent="{esc(parent)}">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        f'</mxCell>'
    )


def text(cell_id, x, y, w, h, value, style='text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;'):
    return rect(cell_id, x, y, w, h, value, style)


def edge(cell_id, source=None, target=None, style='', points=None, source_point=None, target_point=None, value=''):
    attrs = [f'id="{esc(cell_id)}"', f'style="{esc(style)}"', 'edge="1"', 'parent="1"']
    if source:
        attrs.append(f'source="{esc(source)}"')
    if target:
        attrs.append(f'target="{esc(target)}"')
    geom = ['<mxGeometry relative="1" as="geometry">']
    if source_point:
        geom.append(f'<mxPoint x="{source_point[0]}" y="{source_point[1]}" as="sourcePoint"/>')
    if target_point:
        geom.append(f'<mxPoint x="{target_point[0]}" y="{target_point[1]}" as="targetPoint"/>')
    if points:
        geom.append('<Array as="points">')
        for px, py in points:
            geom.append(f'<mxPoint x="{px}" y="{py}"/>')
        geom.append('</Array>')
    geom.append('</mxGeometry>')
    return f'<mxCell {' '.join(attrs)} value="{esc(value)}">' + ''.join(geom) + '</mxCell>'


def build():
    cells = []
    cells.append(rect('bg', 0, 0, 1416, 668, '', 'rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=none;'))
    panel_style = 'rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#7b2fb9;strokeWidth=2;dashed=1;dashPattern=8 8;arcSize=12;'
    cells.append(rect('p_top', 15, 39, 1374, 240, '', panel_style))
    cells.append(rect('p_bl', 15, 300, 687, 347, '', panel_style))
    cells.append(rect('p_br', 734, 301, 656, 345, '', panel_style))

    top_box = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#e9dfb7;strokeColor=#000000;strokeWidth=1.5;fontSize=18;fontFamily=Times New Roman;'
    white_box = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#edf0f7;strokeColor=#000000;strokeWidth=1.2;fontSize=16;fontFamily=Times New Roman;'
    pink_box = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#f5e9e5;strokeColor=#000000;strokeWidth=1.2;fontSize=16;fontFamily=Times New Roman;'
    cells += [
        rect('frontend', 180, 62, 135, 37, '前端', top_box),
        rect('order', 42, 136, 196, 36, '订单/API', white_box),
        rect('recommend', 260, 136, 196, 36, '推荐/API', white_box),
        rect('inventory', 42, 209, 196, 35, '库存/API', pink_box),
        rect('profile', 260, 209, 196, 35, '画像/API', pink_box),
    ]
    arrow_style = 'edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.8;endArrow=classic;endFill=1;endSize=10;'
    cells += [
        edge('e1', 'frontend', 'order', arrow_style + 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;'),
        edge('e2', 'frontend', 'recommend', arrow_style + 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;'),
        edge('e3', 'order', 'inventory', arrow_style + 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;'),
        edge('e4', 'recommend', 'profile', arrow_style + 'exitX=0.5;exitY=1;entryX=0.5;entryY=0;'),
    ]

    cells.append(text('call_title', 611, 45, 170, 40, '调用链数据', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=23;fontStyle=1;fontFamily=SimSun;'))

    icon_bg_style = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#f5a04a;strokeColor=none;arcSize=25;'
    cloud_style = 'shape=cloud;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#ffffff;'
    text_style = 'text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=16;fontFamily=Times New Roman;whiteSpace=wrap;'
    icon_data = [
        ('i1', 526, 100, 'c1', 531, 106, 't1', 558, 103, 250, 30, '前端'),
        ('i2', 553, 132, 'c2', 558, 138, 't2', 586, 131, 460, 34, '订单/API: {“sku”: “A370”, “city”: “hz”, ... }'),
        ('i3', 586, 164, 'c3', 591, 170, 't3', 620, 161, 470, 34, '库存/API: {“sku”: “A370”, “warehouse”: “east-1”, ... }'),
        ('i4', 526, 196, 'c4', 531, 202, 't4', 558, 193, 470, 34, '推荐/API: {“user”: “u1024”, “scene”: “detail”, ... }'),
        ('i5', 553, 228, 'c5', 558, 234, 't5', 586, 225, 500, 34, '画像/API: {“segment”: “outdoor”, “score”: 0.83, ... }'),
    ]
    for iid, ix, iy, cid, cx, cy, tid, tx, ty, tw, th, val in icon_data:
        cells.append(rect(iid, ix, iy, 26, 26, '', icon_bg_style))
        cells.append(rect(cid, cx, cy, 16, 10, '', cloud_style))
        cells.append(text(tid, tx, ty, tw, th, val, text_style))
    dotted_style = 'edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#000000;strokeWidth=1.5;dashed=1;dashPattern=2 2;endArrow=none;'
    cells += [
        edge('dc1', None, None, dotted_style, [(539, 126)], (539, 114), (566, 145)),
        edge('dc2', None, None, dotted_style, [(566, 157)], (566, 145), (599, 177)),
        edge('dc3', None, None, dotted_style, [(539, 209)], (539, 126), (539, 209)),
        edge('dc4', None, None, dotted_style, [(566, 221)], (539, 209), (566, 241)),
    ]

    cells.append(text('timeline_title', 1058, 54, 240, 35, 'Trace 时间线', 'text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=16;fontFamily=Times New Roman;'))
    cells.append(edge('timeline_arrow', None, None, 'endArrow=classic;strokeColor=#000000;strokeWidth=1.6;endSize=8;html=1;', None, (1054, 89), (1314, 89)))
    vstyle = 'endArrow=none;strokeColor=#000000;strokeWidth=1.2;dashed=1;dashPattern=4 2;html=1;'
    cells += [
        edge('tv1', None, None, vstyle, None, (1054, 89), (1054, 246)),
        edge('tv2', None, None, vstyle, None, (1121, 89), (1121, 246)),
        edge('tv3', None, None, vstyle, None, (1210, 89), (1210, 179)),
        edge('tv4', None, None, vstyle, None, (1188, 159), (1188, 246)),
    ]
    bar_blue = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#c8d4eb;strokeColor=none;fontSize=13;fontFamily=Times New Roman;'
    bar_green = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#b8d793;strokeColor=none;fontSize=13;fontFamily=Times New Roman;'
    bar_orange = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#ebc39f;strokeColor=none;fontSize=13;fontFamily=Times New Roman;'
    cells += [
        rect('tb1', 1054, 104, 67, 20, '0.9s', bar_blue),
        rect('tb2', 1121, 126, 108, 20, '2.8s', bar_green),
        rect('tb3', 1210, 159, 118, 20, '1.4s', bar_orange),
        rect('tb4', 1121, 191, 67, 20, '0.7s', bar_green),
        rect('tb5', 1188, 216, 95, 20, '1.1s', bar_orange),
    ]

    cells.append(rect('chart', 76, 321, 577, 262, '', f'shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;image={chart_uri};strokeColor=none;fillColor=none;'))
    cells.append(text('metrics_title', 273, 606, 170, 42, '指标数据', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=25;fontStyle=1;fontFamily=SimSun;'))

    cells.append(rect('log_box', 791, 344, 545, 205, '', 'rounded=1;whiteSpace=wrap;html=1;fillColor=#d8d3e8;strokeColor=#000000;strokeWidth=1.5;arcSize=8;'))
    log_html = (
        '<div style=&quot;font-family:Times New Roman;font-size:14px;line-height:1.32;&quot;>'
        '<font color=&quot;#e46c0a&quot;>2025-07-02T16:41:12Z</font> '
        '<font color=&quot;#6a9e42&quot;>[INFO]</font> Gateway: Calling<br/>'
        'OrderService with params {&quot;sku&quot;:&quot;A370&quot;}<br/>'
        '<font color=&quot;#e46c0a&quot;>2025-07-02T16:41:13Z</font> '
        '<font color=&quot;#c49a00&quot;>[WARN]</font> InventoryService:<br/>'
        'cache miss on key &quot;stock:A370&quot;<br/>'
        '<font color=&quot;#e46c0a&quot;>2025-07-02T16:41:13Z</font> '
        '<font color=&quot;#ff0000&quot;>[ERROR]</font> InventoryService/check:<br/>'
        'RedisTimeoutError'
        '</div>'
    )
    cells.append(text('log_text', 802, 371, 507, 148, log_html, 'text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacing=0;fontSize=14;fontFamily=Times New Roman;whiteSpace=wrap;'))
    cells.append(text('logs_title', 998, 607, 170, 42, '日志数据', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=25;fontStyle=1;fontFamily=SimSun;'))

    root = '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + ''.join(cells) + '</root>'
    return f'<mxGraphModel dx="1416" dy="668" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1416" pageHeight="668" math="0" shadow="0">{root}</mxGraphModel>'

xml = build()
(BASE / 'source.drawio').write_text(xml)
print(BASE / 'source.drawio')
print(len(xml))
