# AetherFire — Current Status & Ontology Map

> Chỉ gồm ontology hiện hành đã resolve trong cụm Citizen–Civil–Undie. Mọi khoảng trống được ghi `UNKNOWN`; file này không tạo canon mới.
>
> **Truth-status rule:** `ABSENCE OF CANON ≠ CANONICAL NEGATION`; `NOT ESTABLISHED ≠ FALSE`; hai trục độc lập không tự cho biết các giá trị của chúng có thể kết hợp hoặc ánh xạ thế nào.

## 1. STATUS

**Definition:** trạng thái pháp lý/civic đang chi phối subject; không đồng nhất với class, job, rank, zone hay economic variable.

**Known values trong phạm vi:**

- `Citizen` — citizen status.
- `Civil Slave` — Slave legal status với civic standing ngang Citizen trong phạm vi đã chốt.
- `Yellow` — temporary disciplinary status của Citizen, một tuần ở first offense, mặc Undi, rồi trở lại Citizen.
- `POW` — public status; backend dùng Slave security category nhưng không kéo POW vào Civil/Criminal/Undie ontology.
- `Slave` — umbrella legal/status category có các class riêng như Civil, Undie và Criminal trong source hiện hành.

**Known transitions:**

```text
Citizen
→ accepted real Civil billet + final confirmation
→ Civil Slave

Civil Slave
→ review bắt đầu từ năm 5
→ nếu tới năm 10 chưa được duyệt/xét: Citizen trực tiếp

Citizen → Undie                 [one-way entry]
Civil Slave → Undie             [one-way]
White/Undie → Citizen           [conditional exit path]

Citizen → first offense → Yellow → 1 tuần → Citizen
repeat Yellow-rule offense → Red / Undie [vĩnh viễn + quota ×2: older unsuperseded detail]

death-sentence exposure → plea → Criminal Slave
```

**UNKNOWN:** exact Yellow repeat timing; full Citizen→Undie admission law; exact Civil year-5 criteria/authority/exceptions; unilateral right to quit Civil; exact White→Citizen legal mechanism.

## 1A. SOCIAL HIERARCHY / CIVIC STANDING

Social hierarchy là trục riêng với legal status và class.

```text
Hoàng gia > Quý tộc > Sĩ quan quân đội = POW > Thượng lưu > Trung lưu > Trí thức > Citizen = Civil Slave > Undie > Criminal
```

`Citizen = Civil Slave` chỉ ở civic standing/social tier, không phải legal-status identity. Purple/Hazel vẫn thuộc class Undie nhưng được đặt ở social tier Trí thức.

## 2. CLASS / COLOR

### Class

- `Civil Slave` — source xác nhận đây là legal status/labor line; exact separate class-field label không được tự suy.
- `Undie` — class bên trong Slave umbrella; không phải một job đơn lẻ.
- `Criminal` — Slave class riêng, dưới Undie trong official social hierarchy.

### Color / visual-functional labels

- `Brown` — current confirmed use: màu jumpsuit đồng nhất của Civil; không phải rank Undie.
- `Black` — màu nhận dạng của Criminal; `Criminal` mới là class.
- `Red`, `Scarlet`, `Pink`, `Gray`, `Purple`, `Hazel`, `White` — functional color labels trong class Undie, mã hóa function/track/cấp nghề; không tạo class mới.

**Relations:** Purple/Hazel vẫn thuộc class Undie nhưng có social tier `Trí thức`. White vẫn thuộc Undie cho đến khi transition sang Citizen hoàn tất. Yellow mặc Undi nhưng được map là disciplinary status; không tự suy full Undie-class membership.

**UNKNOWN:** full color/function matrix; exact one-to-one relation giữa color, function và track; current existence của một penal class Brown ngoài các source hiện hành; full Criminal color/class mobility.

## 3. JOB / LABOR REGIME

### Civil

- Civil = labor buffer 5–10 năm.
- Không có billet thật thì không conversion.
- Billet phải có job, location, receiving unit, start time và deployment conditions.
- Applicant có thể từ chối trước conversion; sau conversion, accepted assignment là nghĩa vụ.
- Placement kết thúc → reserve/transitional duty → reassignment; unplaced Civil không phải unemployed Civil.
- Sau assignment, Civil hưởng labor law như Citizen trong phạm vi đã chốt.

### Undie

- Undie class không đồng nghĩa một job duy nhất.
- Legal status/class ≠ legality của current activity ≠ works at brothel.
- Work có thể ở trong/ngoài red-light district, facility hoặc independent, legal hoặc illegal.
- Functional colors/tracks điều chỉnh assignment, specialization, agency, consent profile và responsibility.

### Criminal

- Current confirmed regime: cực thấp/bẩn/nguy hiểm/không đáng dùng robot; ví dụ waste, hospital cleaning, sewer cleaning.
- `UNKNOWN / NEEDS USER RESOLUTION:` metallurgy/construction/factory list trong merged source có còn current hay không.

## 3A. CIVIL AUDIT MATRIX

| Dimension | Latest confirmed canon | Status |
| --- | --- | --- |
| Entry | Apply → real billet → accept → final confirmation → conversion | CANON |
| Admission | Right to apply ≠ right to be admitted; no billet means no conversion | CANON |
| Legal status | Civil Slave; civic standing ngang Citizen nhưng legal status không đồng nhất | CANON |
| Labor allocation | Accepted assignment bắt buộc sau conversion | CANON |
| Right to quit | Có quyền từ chối billet trước conversion; unilateral exit khỏi Civil sau conversion chưa được định nghĩa | PARTIAL / UNKNOWN |
| Employer relation | Receiving unit nhận labor; labor law như Citizen; exact employer powers/liability chưa có | PARTIAL / UNKNOWN |
| State role | Receiving agency tạo demand; Civil authority kiểm tra/fill/allocate; hai authority không đồng nhất | CANON |
| Tax/fee | Former Civil có tax reduction/exemption tốt hơn Citizen thường; Civil có preferential Undie fee; exact rate/duration unknown | PARTIAL / UNKNOWN |
| Relocation cost | Chi phí cần thiết để placement xảy ra thuộc Civil system theo billet; exact reimbursement/housing unknown | PARTIAL / UNKNOWN |
| Public-service access | Quyền Citizen-equivalent “trong phạm vi đã chốt”; full service/access matrix chưa có | PARTIAL / UNKNOWN |
| Marriage | Current supplied sources chưa xác nhận Civil-specific marriage rule | UNKNOWN / NOT ESTABLISHED |
| Citizenship pathway | Review bắt đầu năm 5; tới năm 10 chưa được xét/duyệt thì lên Citizen trực tiếp | CANON |
| Resident pathway | Current supplied sources chưa xác nhận có hoặc không có resident-status pathway riêng | UNKNOWN / NOT ESTABLISHED |
| Exceptions | Exact year-5 criteria/authority/exceptions chưa chốt | UNKNOWN |
| Placement loss | Reserve/transitional duty rồi reassignment; không thành unemployed Civil | CANON |
| Mobility | Empire-wide billet pool; pre-conversion refusal; post-conversion location obligation; Civil→Undie one-way; Civil→Citizen 5–10y | CANON + bounded UNKNOWN |

## 4. CAREER RANK

**Definition:** trục tiến trình nghề nghiệp dùng để mở facility/shopping/necessities và điều chỉnh Credits; không phải class hoặc color.

**Known values:** `Entry`, `Intermediate`, `Support`, `Advanced`, `Ultimate`.

**Relation:** Career Rank và functional color labels Red/Scarlet/Pink/Gray/Purple/Hazel/White là hai trục không đồng nhất. Distinct axes không xác nhận hoặc phủ định một combination cụ thể.

**UNKNOWN / NOT ESTABLISHED:** full rank rules; promotion formula; cross-mapping và compatibility giữa Career Rank với từng Undie color/function/track.

## 5. ZONE

**Definition:** operational geography, không phải status/class/rank.

**Known values:** Industrial, Commercial, Auctions, Entertainment. Capital có nhiều vòng; class/color có thể liên quan vùng hoạt động.

**Relations:** Undie có thể rời red-light district và đi trong đô thị; restriction nhắm vào disruptive activity hoặc specialized restricted points, không phải blanket presence ban. Capital có full/near-full Undie infrastructure; satellite cities có partial system.

**UNKNOWN:** full zone map, full access matrix, exact barrier/collar permission rules.

## 6. CREDITS

**Definition:** tiền điện tử nhận sau công việc, dùng cho sức mua/hàng hóa/dịch vụ và một số quyền tiêu dùng.

**Properties:** money; không phải Credit Score, Contribution Points, Career Rank, status hay class.

**Known uses của normal Credits:** ordinary consumption trong phạm vi được phép.

Facility proposals/upgrades và một số room/customization eligibility dùng source wording `credits` hoặc `credits nội bộ`; exact relation của chúng với normal personal Credits chưa chốt.

**UNKNOWN:** quan hệ kế toán chính xác giữa personal Credits và “credits nội bộ” của facility; exact variable ở uniform unlock, terminal field, Pink contact cost và các bonus +50%; full credit economy.

## 7. CONTRIBUTION POINTS

**Definition:** vốn trách nhiệm/độ tin cậy theo vị trí.

**Properties:** không phải tiền, Credit Score hay morality score. Có thể reset khi tiến/lùi/đổi nghề trong các trường hợp đã chốt.

**UNKNOWN:** formula, authority và exact reset matrix.

## 8. OTHER ECONOMIC VARIABLES

### Credit Score

- Performance/progression/eligibility variable trong Undie career graph.
- Ghi nhận thành tích tại functional position hiện tại.
- Dùng làm điều kiện mobility; reset khi chuyển local functional track/cấp nghề theo dedicated source.
- Không tự động tạo White; White còn cần self-application, external nomination và selection/placement.

### Credit Line / tín dụng nội bộ

- Borrowing facility riêng, không phải cash đa dụng.
- Chỉ dùng cho nhóm high-risk/high-reward shop đã nêu ví dụ.
- Có thể dùng status làm collateral.
- Default có thể dẫn đến private red-light facility điều phối giờ làm/pay cho tới khi trả nợ, với current caps `work time ≤ 16h/day` và `basic wage ≤ 20% minimum-wage range` của nghề tương ứng.

### Citizen credit profile / bad credit

- Financial/eligibility profile của Citizen; bad debt có thể làm giảm cơ hội việc làm.
- Quan hệ với Undie Credit Line hoặc Credit Score là `UNKNOWN`; không đồng nhất.

### Legacy black credit

- Design history; không phải current canon.

## 9. ACCESS PROFILE

**Definition:** quyền truy cập/di chuyển/dịch vụ được xác nhận qua collar/backend và rules; không phải class hay Career Rank.

**Known relations:**

- Career Rank có thể mở facility/shopping/necessities.
- Functional track/color và zone có thể ảnh hưởng access nhưng không phải cùng một trục.
- Collar là administrative terminal cho ID, access, movement, task và enforcement links.
- Undie status không cho phép công quyền tùy tiện chặn subject.
- Civil applicant chưa conversion không có Civil benefit.

**UNKNOWN:** full access matrix; exact permission changes của từng Career Rank và functional color; public-service matrix của Civil.

## 10. BACKGROUND / PROVENANCE

**Definition:** nguồn gốc/hồ sơ lịch sử; không phải current operational classification.

**Known rules:**

- Sau voluntary Civil conversion, background vẫn ở hồ sơ nhưng không còn là biến vận hành chính.
- Không tạo Refugee/Nomad/Unemployed/Deserter Civil caste chỉ từ provenance.
- Former Undie trở thành Citizen không bị xóa lịch sử; provenance thường bị ẩn nhưng có thể được truy xuất trong một số ngành chưa xác định.
- Genealogy của Yellow từ fake-Undie/impersonation không biến genealogy thành current class ontology.

**UNKNOWN:** exact provenance access law, ngành được truy xuất former-Undie history, và treatment của non-voluntary Civil provenance ngoài phần đã chốt.
