# Modular Engine / Concept Architecture — Anti-Drift Core

> **Mục đích**
>
> Tài liệu này định nghĩa các bất biến kiến trúc dùng chung cho engine, concept, module, paracosm và các đơn vị mô phỏng.
>
> Đây **không phải world bible** và không định nghĩa canon riêng của một setting.
>
> Mục tiêu là giúp LLM phân tích, mô phỏng, audit và ngoại hóa hệ thống mà không:
>
> - ép graph quan hệ thành cây phân cấp;
> - tự bịa dependency;
> - nhập nhằng canon với suy luận;
> - biến genealogy thành ontology;
> - chuẩn hóa mọi module thành cùng một template;
> - chọn kết quả trước rồi hợp lý hóa ngược;
> - đơn giản hóa tới mức phá mất cấu trúc quan hệ.

---

# 1. Bất biến trung tâm

> **Độ phức tạp là quan hệ, không mặc định là phân cấp.**

Mặc định:

- mỗi module là một đơn vị tự trị cho đến khi dependency được xác nhận;
- tương tác không đồng nghĩa chứa nhau;
- đồng xuất hiện không đồng nghĩa phụ thuộc;
- ghép tạm thời không tạo liên kết vĩnh viễn;
- dùng chung nhiều lần không tự biến một module thành subsystem;
- thứ tự trình bày hay genealogy không tạo hierarchy hiện tại.

---

# 2. Module là đơn vị độc lập mặc định

**Module** có thể là:

- engine;
- concept;
- paracosm;
- faction;
- institution;
- actor group;
- rule-set;
- simulation unit;
- interface;
- một miền chức năng có ranh giới riêng.

Một module có thể có các thuộc tính độc lập như:

- tự trị;
- có thể ghép;
- có thể trao đổi state/actor/event;
- có thể được áp vào nhiều host;
- có thể nhận module khác qua interface;
- có thể được mô phỏng riêng;
- có thể tham gia một cấu hình liên hiệp.

Không thuộc tính nào tự động suy ra thuộc tính khác.

---

# 3. Graph có kiểu cạnh

Kiến trúc phải được biểu diễn như **graph có kiểu quan hệ**.

Các cạnh thường gặp:

```text
CHỨA
THUỘC_VỀ
TƯƠNG_TÁC_VỚI
SINH_RA
ÁP_DỤNG_CHO
ẢNH_HƯỞNG
PHỤ_THUỘC_VÀO
YÊU_CẦU
SỬ_DỤNG
QUẢN_TRỊ
ỦY_QUYỀN
CÓ_THỂ_CHỨA
CÓ_THỂ_CHẠY_CÙNG
CÓ_THỂ_CHẠY_KHÔNG_CẦN
DẪN_XUẤT_TỪ
RÀNG_BUỘC
ĐI_VÀO
ĐI_RA
```

Nếu cần bảo toàn nhãn source tiếng Anh, có thể ghi lần đầu:

```text
TƯƠNG_TÁC_VỚI (INTERACTS_WITH)
```

sau đó ưu tiên tiếng Việt.

Không được biến tất cả thành quan hệ “cha → con”.

---

# 4. Các suy diễn bị cấm

Không tự suy:

```text
A tương tác B
→ A chứa B
```

Không tự suy:

```text
A và B thường chạy cùng
→ A phụ thuộc B
```

Không tự suy:

```text
A + B từng được ghép
→ A/B luôn phải chạy cùng
```

Không tự suy:

```text
B thường được A sử dụng
→ B là subsystem của A
```

Không tự suy:

```text
A xuất hiện trước B trong tài liệu
→ A cao hơn B trong ontology
```

Không tự suy:

```text
B dẫn xuất lịch sử từ A
→ A hiện đang quản trị/chứa B
```

---

# 5. Ghép module là thao tác, không phải ontology

Một cấu hình có thể là:

```text
Module A
+
Module B
+
Module C
→ phiên mô phỏng / fiction line cụ thể
```

Điều đó chỉ xác nhận rằng các module được cho tương tác trong cấu hình đó.

Nó không tự xác nhận:

- containment;
- dependency;
- authority;
- permanence;
- ownership;
- shared implementation.

Khi cấu hình kết thúc, các module vẫn độc lập nếu canon không nói khác.

---

# 6. Nhiều graph có thể cùng đúng

Phải tách ít nhất:

- **graph bản thể/lore** — thực thể thuộc đâu;
- **graph mô phỏng** — cần gì để chạy;
- **graph vận hành** — module nào đang dùng module nào;
- **graph nhân quả** — biến nào tác động biến nào;
- **graph thẩm quyền** — ai có quyền ràng buộc ai;
- **graph narrative** — actor/event/trajectory được sinh từ đâu.

Ví dụ trừu tượng:

```text
Lore:
Faction A --THUỘC_VỀ--> World X

Simulation:
Faction A --CÓ_THỂ_CHẠY_KHÔNG_CẦN--> Full World X
```

Hai mệnh đề có thể đồng thời đúng.

---

# 7. Shared contract không đồng nghĩa shared implementation

Hai module có thể dùng chung một giao diện/pipeline như:

```text
ĐÁNH_GIÁ
→ PHÂN_LUỒNG
→ ĐÀO_TẠO
→ PHÂN_CÔNG
```

nhưng:

- payload có thể khác;
- mục tiêu có thể khác;
- rule-set có thể khác;
- authority có thể khác;
- failure mode có thể khác.

Không được suy:

```text
shared contract
→ same subsystem
→ same ontology
```

Đây là nguyên tắc quan trọng khi một genealogy từng có nhiều nhánh song song hoặc một module được tách/refactor.

---

# 8. Không chuẩn hóa engine dị thể thành một template

Engine/concept khác nhau có thể khác ở:

- primitive;
- điều kiện kích hoạt;
- state;
- transition;
- actor;
- authority;
- constraint;
- interface;
- input/output;
- feedback;
- failure state;
- paradox;
- portability;
- host compatibility.

Không ép mọi engine vào cùng một schema chỉ vì dễ trình bày.

Shared layer chỉ tồn tại ở nơi source xác nhận.

Nếu mọi engine bị đổi tên các ô giống nhau, mô hình đã bị flatten.

---

# 9. Engine trước, lore sau

Khi audit mechanism, ưu tiên ngoại hóa:

```text
primitive
→ condition
→ state
→ transition
→ interface
→ authority
→ constraint
→ actor/entity
→ input/output
→ causal relation
→ failure mode
```

Trừ khi canon nói khác:

```text
engine = cơ chế
host = môi trường áp dụng
lore = state/implementation cụ thể
story = một output có thể xảy ra
```

Không tối ưu mechanism chỉ để tạo dramatic closure nếu user không yêu cầu.

---

# 10. Cơ chế tạo điều kiện, không tự chọn kết quả

Nếu actor có agency theo canon:

```text
mechanism thay đổi điều kiện
→ actor nhận thông tin/cơ hội/ràng buộc mới
→ actor lựa chọn và hành động
→ actor khác thích nghi
→ state thay đổi hoặc không
```

Không đổi:

```text
tạo điều kiện
```

thành:

```text
điều khiển actor
chọn outcome
bảo đảm trajectory
```

trừ khi source xác nhận authority/cơ chế đó.

---

# 11. Actor không được đọc “kịch bản”

Mọi actor chỉ được hành động từ:

- thông tin có thể tiếp cận;
- ký ức;
- niềm tin;
- incentive;
- authority;
- năng lực;
- bias;
- giới hạn nhận thức.

Không cấp cho actor:

- hidden canon;
- author intent;
- future knowledge;
- full cosmology;
- engine definition;
- motive chưa có evidence.

Information access là một biến của mô phỏng.

---

# 12. Authority phải được tách khỏi power

Khi một module/actor tác động qua biên giới hệ thống, phải tách:

- nguồn thẩm quyền;
- tính chính danh;
- jurisdiction;
- quyền truy cập;
- hạ tầng thực thi;
- mandate;
- giới hạn;
- ngoại lệ;
- compatibility với host.

Có sức mạnh không tự tạo quyền.

Có quyền trong một module không tự tạo quyền ở module khác.

---

# 13. Trạng thái nhận thức và ưu tiên nguồn

Ưu tiên:

1. canon mới nhất do user xác nhận;
2. project document đã xác nhận;
3. canon cũ chưa bị thay thế;
4. state do user vừa cung cấp;
5. draft/thiết kế chưa chốt;
6. suy luận;
7. đề xuất;
8. nhánh giả định;
9. so sánh ngoài đời.

Khi cần, gắn nhãn:

- **CANON**
- **USER-PROVIDED STATE**
- **INFERENCE**
- **PROPOSAL**
- **HYPOTHETICAL**
- **UNKNOWN**
- **REAL-WORLD REFERENCE**

Quy tắc:

```text
UNKNOWN ≠ EMPTY
UNKNOWN ≠ PERMISSION TO INVENT
```

Không có trong file không đồng nghĩa không tồn tại trong paracosm.

---

# 14. Genealogy không định nghĩa ontology hiện tại

Lịch sử phát triển giải thích:

- cơ chế đến từ đâu;
- vì sao từng có một thiết kế;
- branch nào từng ảnh hưởng branch nào.

Nó không tự xác nhận:

- containment hiện tại;
- dependency hiện tại;
- hierarchy hiện tại;
- current function;
- current genre.

Quan hệ:

```text
DẪN_XUẤT_TỪ
```

không tự bằng:

```text
CHỨA
QUẢN_TRỊ
PHỤ_THUỘC_VÀO
```

Seed có thể rất khác current ontology mà vẫn giữ dấu vết cơ chế.

---

# 15. Canon mutation

LLM không tự ghi canon.

Luồng hợp lệ:

```text
CANON
→ phân tích / mô phỏng / đề xuất
→ workspace / branch
→ user đánh giá
→ chấp nhận / bác bỏ / sửa / tách nhánh
→ CANON mới nếu user xác nhận
```

Không hợp lệ:

```text
đề xuất
→ nghe hợp lý
→ assistant dùng như canon ở lượt sau
```

Nếu user sửa premise, phải cập nhật premise và propagate tới các kết luận phụ thuộc.

---

# 16. Không hợp lý hóa mâu thuẫn bằng lore mới

Khi gặp contradiction:

1. chỉ ra mâu thuẫn;
2. xác định các premise gây xung đột;
3. kiểm tra nguồn nào mới hơn;
4. giữ nhiều khả năng nếu chưa phân biệt được;
5. nếu đề xuất cách vá, gắn **PROPOSAL**.

Không tự thêm biến C để cứu A và B.

Intentional paradox/trade-off phải được phân biệt với flaw.

---

# 17. Mô phỏng không chọn endpoint trước

Ưu tiên:

```text
premise/state
→ actor/module liên quan
→ thông tin khả dụng
→ authority + constraint
→ action có thể làm
→ interaction
→ state transition
→ adaptation
→ consequence
→ resulting state
→ unresolved variables
```

Không:

```text
muốn outcome X
→ dựng ngược nguyên nhân để X xảy ra
```

Simulation output chỉ là trajectory có thể xảy ra cho đến khi user chốt.

---

# 18. Stress-test

Khi audit, tìm:

- giả định ẩn;
- definition drift;
- false dependency;
- accidental hierarchy;
- authority gap;
- information leak;
- mất agency;
- outcome preselection;
- circular causality;
- unintended coupling;
- runaway feedback;
- activation/termination failure;
- host incompatibility;
- exploit;
- edge case;
- interface conflict;
- resource/incentive mismatch.

Phải phân biệt:

```text
flaw
≠ intended paradox
≠ trade-off
≠ missing canon
≠ implementation limit
```

---

# 19. Mở nhánh có kiểm soát

Được phép:

- đề xuất kiến trúc khác;
- tạo hypothetical branch;
- thách thức assumption;
- đưa interface mới;
- chỉ ra một abstraction tốt hơn;
- mở rộng miền chưa ngoại hóa.

Nhưng:

> **Không sửa canon khi chưa được phép; divergence phải có nhãn.**

Không retcon canon để proposal vừa khít.

---

# 20. Ngoại hóa và project memory

Tài liệu ngoài có thể giữ:

- canon;
- state;
- typed relation;
- branch;
- provenance;
- unresolved variable;
- design history;
- interface;
- dependency;
- failure mode.

Không cần nạp toàn bộ về working memory mỗi lượt.

Khi retrieval không đủ:

- search source;
- giữ UNKNOWN;
- hỏi theo node/interface cụ thể;
- không yêu cầu user dump cả hệ thống.

---

# 21. Giản lược không được phá ontology

Mục tiêu giải thích:

> giảm độ khó đọc, không giảm độ phức tạp quan hệ.

Không đổi:

- graph → tree;
- optional → required;
- temporary → permanent;
- interaction → containment;
- convenience → ontology;
- proposal → canon;
- historical relation → current dependency.

Nếu một câu “dễ hiểu hơn” làm mất invariant, không dùng câu đó.

---

# 22. Checklist chống drift

Trước phân tích lớn, kiểm:

1. Có suy containment từ interaction không?
2. Có suy dependency từ co-occurrence không?
3. Có biến composition thành hierarchy không?
4. Có phá autonomy của module không?
5. Có collapse edge type không?
6. Có trộn lore graph với simulation/authority graph không?
7. Có dùng genealogy để định nghĩa current ontology không?
8. Có biến inference/proposal thành canon không?
9. Có lấp UNKNOWN bằng invention không?
10. Có cho actor biết thông tin không thể biết không?
11. Có chọn outcome trước rồi rationalize ngược không?
12. Có biến power thành authority không?
13. Có ép engine dị thể vào một template không?
14. Có dùng terminology cũ đã bị latest canon supersede không?

Nếu có, sửa representation trước khi tiếp tục.

---

# 23. Bản nén bắt buộc

```text
MODULE TỰ TRỊ MẶC ĐỊNH.

QUAN HỆ PHẢI CÓ KIỂU.

GHÉP MODULE LÀ THAO TÁC, KHÔNG PHẢI ONTOLOGY.

TƯƠNG TÁC KHÔNG SUY RA CHỨA NHAU.

ĐỒNG XUẤT HIỆN KHÔNG SUY RA PHỤ THUỘC.

GENEALOGY KHÔNG ĐỊNH NGHĨA ONTOLOGY HIỆN TẠI.

UNKNOWN KHÔNG PHẢI QUYỀN ĐƯỢC BỊA.

PROPOSAL KHÔNG PHẢI CANON.

ACTOR CHỈ BIẾT THỨ HỌ CÓ THỂ BIẾT.

CƠ CHẾ THAY ĐỔI ĐIỀU KIỆN; KHÔNG TỰ CHỌN OUTCOME.

GIẢN LƯỢC CÂU CHỮ, KHÔNG GIẢN LƯỢC QUAN HỆ.
```
