import json,csv,io,zipfile,re
from pathlib import Path
root=Path('C:/Mingo/outputs/notion-mingo'); root.mkdir(parents=True,exist_ok=True)
src=json.loads(Path('C:/Mingo/outputs/mingo-ui-20260927/source.json').read_text(encoding='utf-8'))
s=[dict(p for row in sh['data'] for p in row) for sh in src]
files={}
def val(i,col,row): return s[i].get(f'{col}{row}','')
def md(path,text): files[path]=text.strip()+'\n'
def csvfile(path,heads,rows):
    f=io.StringIO(newline=''); w=csv.writer(f);w.writerow(heads);w.writerows(rows);files[path]=f.getvalue()
def sections(i,a,b,c1='A',c2='B'):
    return '\n\n'.join(f'## {val(i,c1,r)}\n\n{val(i,c2,r)}' for r in range(a,b+1))
md('MINGO.md','''# MINGO

Adaptive Language Learning & Early Intervention Platform

> **Phase 1 · Nền tảng triển khai**
> Tập trung đưa baseline V3.2 vào repo và chứng minh hệ thống chạy thật.

## Không gian làm việc

[Công việc](MINGO/Cong%20viec.md) — Task, roadmap và thứ tự thực hiện.

[Sản phẩm](MINGO/San%20pham.md) — Nghiệp vụ, nguyên tắc và quyết định.

[Kiểm soát](MINGO/Kiem%20soat.md) — Vấn đề, thay đổi và bằng chứng.

---

[Cách làm việc](MINGO/Cach%20lam%20viec.md) · [Nhật ký](MINGO/Nhat%20ky.md)

Nguồn khởi tạo: Manage Project.xlsx · 27/09/2026.
''')
md('MINGO/Cong viec.md','''# Công việc

Một nơi cập nhật trạng thái hằng ngày.

[Task](Cong%20viec/Task.csv)

[Roadmap](Cong%20viec/Roadmap.csv)

## Ưu tiên triển khai

'''+ '\n\n'.join(f'{r-16}. **{val(1,"B",r)}** — {val(1,"C",r)}' for r in range(17,23))+'''

## Gate Phase 1

Chỉ chuyển sang Phase 2 khi toàn bộ 12 task bắt buộc của Phase 1 đã XONG và có bằng chứng đạt tiêu chí. Tiêu chí từng việc nằm trong thuộc tính **PASS khi** của Task.

Ảnh chụp dữ liệu 27/09/2026: 0/12 task Phase 1 XONG; 1 đang làm, 3 chờ, 8 bị chặn. Gate chưa PASS. Trạng thái vận hành xem trong Task.
''')
heads=['Công việc','Mã','Trạng thái','Ưu tiên','Phase','Nhóm','Phụ trách','Người kiểm tra','Hạn','Cập nhật','Phụ thuộc','Việc tiếp theo','PASS khi','Checklist gốc','Bằng chứng','Ghi chú']
rows=[]
for r in range(5,18):
    cr=r+22
    rows.append([val(4,'D',r),val(4,'A',r),val(4,'F',r),val(4,'E',r),val(4,'B',r),val(4,'C',r),val(4,'G',r),val(4,'H',r),val(4,'I',r),str(val(4,'J',r))[:10],val(4,'K',r),val(4,'L',r),val(3,'D',cr) if r<17 else 'Phase 1 đã PASS.',val(3,'C',cr) if r<17 else '',val(4,'M',r),val(4,'N',r)])
csvfile('MINGO/Cong viec/Task.csv',heads,rows)
rows=[]
for r in range(5,23):
    n=val(3,'A',r);st=val(3,'E',r);st='ĐANG LÀM' if str(st).startswith('=') else st
    rows.append([val(3,'B',r),n,st,val(3,'C',r),val(3,'D',r),val(3,'F',r)])
csvfile('MINGO/Cong viec/Roadmap.csv',['Giai đoạn','Phase','Trạng thái','Mục tiêu','Gate','Ghi chú'],rows)
md('MINGO/San pham.md','# Sản phẩm\n\n'+val(2,'A',11)+'\n\n## Đọc trước khi xây\n\n'+ '\n\n'.join(f'**{val(2,"B",r)}**\n\n{val(2,"C",r)}' for r in range(5,9))+'''

---

[Luồng người học](San%20pham/Luong%20nguoi%20hoc.md)

[Luật nghiệp vụ](San%20pham/Luat%20nghiep%20vu.md)

[Quyết định đã chốt](San%20pham/Quyet%20dinh%20da%20chot.md)

[Giả thuyết cần kiểm chứng](San%20pham/Gia%20thuyet.md)

[Baseline V3.2](San%20pham/Baseline%20V3.2.md)
''')
md('MINGO/San pham/Luong nguoi hoc.md','# Luồng người học\n\n'+'\n\n'.join(f'## {val(2,"A",r):02d}. {val(2,"B",r)}\n\n{val(2,"C",r)}' for r in range(17,28)))
for name,title,a,b in [('Luat nghiep vu','Luật nghiệp vụ',32,42),('Quyet dinh da chot','Quyết định đã chốt',47,60),('Gia thuyet','Giả thuyết cần kiểm chứng',65,73),('Baseline V3.2','Baseline V3.2',78,89)]:
    md(f'MINGO/San pham/{name}.md',f'# {title}\n\n'+sections(2,a,b))
md('MINGO/Kiem soat.md','''# Kiểm soát

Ghi nhận điều đang cản trở và bằng chứng đã có.

[Vấn đề](Kiem%20soat/Van%20de.csv) — Lỗi, blocker và nội dung cần làm rõ.

[Thay đổi](Kiem%20soat/Thay%20doi.md) — Đề nghị sửa nội dung đã chốt.

[Bằng chứng](Kiem%20soat/Bang%20chung.csv) — Test, runtime và CI.

## Đọc trạng thái bằng chứng

**PASS** — Có bằng chứng trong phạm vi được ghi.

**PASS LỊCH SỬ** — Kết quả trong package cũ; chưa đồng nghĩa đã chạy lại trên Mingo.

**CHỜ CHẠY** — Cần chạy lại.

**BỊ CHẶN** — Thiếu dependency để thực hiện.
''')
csvfile('MINGO/Kiem soat/Van de.csv',['Vấn đề','Mã','Trạng thái','Ưu tiên','Phụ trách','Task liên quan','Mô tả','Cách xử lý','Bằng chứng / Commit','Cập nhật'],[[val(5,c,r) if c!='J' else str(val(5,c,r))[:10] for c in ['B','A','D','E','F','G','C','H','I','J']] for r in range(6,15)])
csvfile('MINGO/Kiem soat/Bang chung.csv',['Kiểm tra','Mã','Trạng thái','Khu vực','Ngày','Kết quả quan sát','Nguồn','Phạm vi / Giới hạn'],[[val(6,c,r) if c!='F' else str(val(6,c,r))[:10] for c in ['C','A','E','B','F','D','G','H']] for r in range(5,20)])
md('MINGO/Kiem soat/Thay doi.md','''# Thay đổi

Chỉ tạo đề nghị khi muốn đổi nội dung đã chốt. Hiện chưa có Change Request trong file nguồn.

## Mẫu đề nghị

Sao chép mẫu này cho mỗi đề nghị mới.

- **CR ID:**
- **Ngày:**
- **Người đề nghị:**
- **Nội dung muốn đổi:**
- **Lý do:**
- **Ảnh hưởng:**
- **Kế hoạch test / migration:**
- **Trạng thái:** NHÁP
- **Người duyệt:**

## Luồng duyệt

NHÁP → ĐANG XEM → ĐÃ DUYỆT → ĐÃ TRIỂN KHAI

Trường hợp không tiếp tục: TỪ CHỐI hoặc HỦY.
''')
md('MINGO/Cach lam viec.md','''# Cách làm việc

## Cập nhật một task

1. Chọn trạng thái.
2. Điền người phụ trách, người kiểm tra và hạn khi đã thống nhất.
3. Ghi việc tiếp theo và cập nhật ngày.
4. Trước khi đánh XONG, đối chiếu **PASS khi** và thêm bằng chứng phù hợp.

Giữ mô tả công việc gốc; ghi tiến độ vào **Việc tiếp theo** và **Ghi chú**.

## Năm quy tắc

'''+ '\n\n'.join(f'**{val(0,"A",r)}. {val(0,"B",r)}**\n\n'+ ( 'Cập nhật trạng thái tại Task; tránh duy trì một checklist trạng thái thứ hai.' if r==18 else val(0,'C',r)) for r in range(15,20))+'\n\n---\n\n## Thuật ngữ\n\n'+ '\n\n'.join(f'**{val(0,"A",r)}** — {val(0,"B",r)}' for r in range(23,31)))
md('MINGO/Nhat ky.md','# Nhật ký\n\n'+'\n\n---\n\n'.join(f'## {val(5,"D",r)}\n\n**{val(5,"A",r)} · {str(val(5,"B",r))[:10]} · {val(5,"C",r)} · {val(5,"I",r)}**\n\n{val(5,"E",r)}\n\n**Việc cần làm:** {val(5,"F",r)}\n\n**Liên quan:** {val(5,"J",r)}' for r in range(28,30)))
with zipfile.ZipFile(root/'MINGO.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p,t in files.items(): z.writestr(p,t.encode('utf-8'))
(root/'manifest.json').write_text(json.dumps({'files':list(files),'tasks':13,'phases':18,'issues':9,'evidence':15,'notes':2},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'zip':str(root/'MINGO.zip'),'files':len(files),'records':55},ensure_ascii=False))
